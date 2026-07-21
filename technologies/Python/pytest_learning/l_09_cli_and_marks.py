"""
Lesson 09: System Reports Processing Service.

This module provides a report generator that behaves differently based 
on the execution environment (dev vs prod) and provides both quick summary 
methods and heavy, time-consuming data crunching operations.
"""


class EnvironmentError(Exception):
    pass


class ReportService:
    def __init__(self, env: str = "dev"):
        self.env = env.lower()
        if self.env not in ["dev", "stage", "prod"]:
            raise EnvironmentError(f"Unsupported environment: {env}")

    def generate_quick_summary(self) -> dict:
        return {"status": "ok", "env": self.env, "items_processed": 10}

    def run_heavy_analytics(self) -> dict:
        if self.env == "prod":
            raise EnvironmentError("Heavy analytics prohibited on production!")
        return {"status": "completed", "records_analyzed": 1_000_000}