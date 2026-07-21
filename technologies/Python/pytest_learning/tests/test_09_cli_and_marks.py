"""
Lesson 09: Testing CLI Options, Conditional Skips, and Custom Markers.

This test suite validates environment-dependent reporting logic using 
CLI flags, conditional pytest skips, and the custom `slow` test filter.
"""

import sys
import pytest
from l_09_cli_and_marks import EnvironmentError, ReportService


class TestReportServiceWork:
    def test_quick_summary(self, report_service: ReportService, target_env: str):
        summary = report_service.generate_quick_summary()
        assert summary["status"] == "ok"
        assert summary["env"] == target_env

    @pytest.mark.slow
    def test_heavy_analytics_processing(self, report_service: ReportService):
        result = report_service.run_heavy_analytics()
        assert result["status"] == "completed"
        assert result["records_analyzed"] == 1_000_000

    @pytest.mark.skipif(sys.platform != "win32", reason="Windows-only file formatting check")
    def test_windows_path_export(self):
        assert True


class TestReportServiceSkipsAndErrors:
    def test_skip_on_production_environment(self, target_env: str, report_service: ReportService):
        if target_env == "prod":
            pytest.skip("Heavy checks disabled on production environment")

        summary = report_service.generate_quick_summary()
        assert summary["items_processed"] > 0

    def test_invalid_environment_raises_error(self):
        with pytest.raises(EnvironmentError):
            ReportService(env="invalid_env")