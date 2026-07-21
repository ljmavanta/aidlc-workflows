"""Tests for scenario loading, including team-inputs support."""

from __future__ import annotations

from pathlib import Path

from shared.scenario import load_scenario


def _write_scenario(dir_path: Path, body: str) -> None:
    (dir_path / "scenario.yaml").write_text(body, encoding="utf-8")
    (dir_path / "vision.md").write_text("# Vision", encoding="utf-8")


class TestTeamInputsField:
    def test_default_team_inputs(self, tmp_path: Path):
        _write_scenario(tmp_path, "name: demo\n")
        scenario = load_scenario(tmp_path)
        assert scenario.team_inputs == "team-inputs/"
        assert scenario.team_inputs_path == (tmp_path.resolve() / "team-inputs")

    def test_custom_team_inputs(self, tmp_path: Path):
        _write_scenario(tmp_path, "name: demo\nteam_inputs: inputs/\n")
        scenario = load_scenario(tmp_path)
        assert scenario.team_inputs == "inputs/"
        assert scenario.team_inputs_path == (tmp_path.resolve() / "inputs")

    def test_team_inputs_path_optional_presence(self, tmp_path: Path):
        """team_inputs_path resolves even when the directory is absent."""
        _write_scenario(tmp_path, "name: demo\n")
        scenario = load_scenario(tmp_path)
        # Not required to exist — the workflow's intake gate handles absence.
        assert not scenario.team_inputs_path.exists()
