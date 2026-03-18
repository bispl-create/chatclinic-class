import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))

    result = {
        "summary": "Tool executed successfully.",
        "artifacts": {},
        "provenance": {
            "tool_version": "0.1.0",
            "received_keys": sorted(payload.keys()),
        },
    }

    Path(args.output).write_text(json.dumps(result), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
