"""Tests for team-owned-inputs seeding and the Scrum stage sequence."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from aidlc_runner.agents.executor import (
    EXECUTOR_SYSTEM_PROMPT,
    _EXECUTOR_PROMPT_NO_EXEC,
)
from aidlc_runner.cli import build_parser, main
from aidlc_runner.config import RunnerConfig
from aidlc_runner.runner import seed_team_inputs, write_run_meta


# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------


class TestCliTeamInputsArgument:
    def test_team_inputs_accepted(self, tmp_path: Path):
        vision = tmp_path / "vision.md"
        vision.write_text("# Vision")
        team = tmp_path / "team-inputs"
        team.mkdir()

        parser = build_parser()
        args = parser.parse_args(["--vision", str(vision), "--team-inputs", str(team)])

        assert args.team_inputs == team

    def test_team_inputs_defaults_to_none(self, tmp_path: Path):
        vision = tmp_path / "vision.md"
        vision.write_text("# Vision")

        parser = build_parser()
        args = parser.parse_args(["--vision", str(vision)])

        assert args.team_inputs is None

    def test_team_inputs_validation_in_main(self, tmp_path: Path):
        """main() should exit(1) when --team-inputs directory doesn't exist."""
        vision = tmp_path / "vision.md"
        vision.write_text("# Vision")

        with pytest.raises(SystemExit) as exc:
            main(["--vision", str(vision), "--team-inputs", str(tmp_path / "missing")])
        assert exc.value.code == 1


# ---------------------------------------------------------------------------
# Runner: seed_team_inputs copies into aidlc-docs/team-inputs/
# ---------------------------------------------------------------------------


class TestSeedTeamInputs:
    def _make_team_inputs(self, tmp_path: Path) -> Path:
        src = tmp_path / "team-inputs"
        src.mkdir()
        (src / "product-vision.md").write_text("# Vision")
        (src / "product-backlog.md").write_text("# Backlog")
        (src / "architecture.md").write_text("# Arch")
        return src

    def test_seeds_files_into_aidlc_docs(self, tmp_path: Path):
        src = self._make_team_inputs(tmp_path)
        run_folder = tmp_path / "run"
        (run_folder / "aidlc-docs").mkdir(parents=True)

        dest = seed_team_inputs(run_folder, src)

        assert dest == run_folder / "aidlc-docs" / "team-inputs"
        assert (dest / "product-vision.md").is_file()
        assert (dest / "product-backlog.md").is_file()
        assert (dest / "architecture.md").read_text() == "# Arch"

    def test_seeding_is_idempotent(self, tmp_path: Path):
        """Re-seeding (e.g. a brownfield continuation) must not error."""
        src = self._make_team_inputs(tmp_path)
        run_folder = tmp_path / "run"
        (run_folder / "aidlc-docs").mkdir(parents=True)

        seed_team_inputs(run_folder, src)
        dest = seed_team_inputs(run_folder, src)  # second call

        assert (dest / "product-vision.md").is_file()

    def test_missing_source_raises(self, tmp_path: Path):
        run_folder = tmp_path / "run"
        (run_folder / "aidlc-docs").mkdir(parents=True)

        with pytest.raises(FileNotFoundError):
            seed_team_inputs(run_folder, tmp_path / "nope")


# ---------------------------------------------------------------------------
# Runner: write_run_meta records the team-inputs directory
# ---------------------------------------------------------------------------


class TestRunMetaTeamInputs:
    def test_meta_includes_team_inputs_dir(self, tmp_path: Path):
        vision = tmp_path / "vision.md"
        vision.write_text("# Vision")
        team = tmp_path / "team-inputs"
        team.mkdir()

        run_folder = tmp_path / "run"
        run_folder.mkdir()

        write_run_meta(run_folder, RunnerConfig(), vision, team_inputs_path=team)

        meta = yaml.safe_load((run_folder / "run-meta.yaml").read_text())
        assert meta["team_inputs_dir"] == str(team.resolve())

    def test_meta_team_inputs_null_when_omitted(self, tmp_path: Path):
        vision = tmp_path / "vision.md"
        vision.write_text("# Vision")

        run_folder = tmp_path / "run"
        run_folder.mkdir()

        write_run_meta(run_folder, RunnerConfig(), vision)

        meta = yaml.safe_load((run_folder / "run-meta.yaml").read_text())
        assert meta["team_inputs_dir"] is None


# ---------------------------------------------------------------------------
# Executor: the system prompt encodes the Scrum stage sequence
# ---------------------------------------------------------------------------


class TestExecutorScrumStages:
    @pytest.mark.parametrize(
        "stage",
        [
            "Backlog Refinement",
            "Sprint Planning",
            "Daily Standup",
            "Research / Spike",
            "Sprint Review",
            "Sprint Retrospective",
        ],
    )
    def test_prompt_mentions_scrum_ceremony(self, stage: str):
        assert stage in EXECUTOR_SYSTEM_PROMPT

    @pytest.mark.parametrize(
        "rule",
        [
            "inception/backlog-refinement.md",
            "construction/research-spike.md",
            "construction/sprint-review.md",
            "construction/sprint-retrospective.md",
            "common/team-inputs.md",
        ],
    )
    def test_prompt_references_new_rule_files(self, rule: str):
        assert rule in EXECUTOR_SYSTEM_PROMPT

    def test_prompt_mentions_team_inputs_source_of_truth(self):
        assert "aidlc-docs/team-inputs/" in EXECUTOR_SYSTEM_PROMPT
        assert "Input Intake Gate" in EXECUTOR_SYSTEM_PROMPT

    def test_no_exec_variant_still_strips_run_command(self):
        """The no-exec prompt transform must still apply after the rewrite."""
        assert _EXECUTOR_PROMPT_NO_EXEC != EXECUTOR_SYSTEM_PROMPT
        assert "run_command" not in _EXECUTOR_PROMPT_NO_EXEC
        # Build and Test stage is still present, just without the exec bullets
        assert "Build and Test" in _EXECUTOR_PROMPT_NO_EXEC
