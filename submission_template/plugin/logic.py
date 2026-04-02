"""Preferred plugin entrypoint.

The platform calls run(payload) directly — no CLI needed.
Replace this template with your tool implementation.
"""


def run(payload: dict) -> dict:
    # deterministic work here
    return {
        "tool": "team_name_tool",
        "summary": "Tool executed successfully.",
        "artifacts": {},
        "provenance": {
            "tool_version": "0.1.0",
            "received_keys": sorted(payload.keys()),
        },
    }
