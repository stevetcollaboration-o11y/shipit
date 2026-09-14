"""shipit: tiny release-notes helper."""

"""Import date"""
from datetime import date

KINDS = ["feat","fix", "docs", "chore"]

def today() -> str:
    """Return today's date as an ISO string, e.g. '2026-08-08'."""
    return date.today().isoformat()


def format_note(kind: str, text: str) -> str:
    """Format one changelog line. kind is a short tag such as feat or fix."""
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {KINDS}, got {kind!r}")
    return f"✨ - [{kind.upper()}] {text}"

def write_notes(notes: list[str], path: str = "CHANGELOG.md") -> None:
    """Append formatted note lines to the changelog file."""
    if not notes:
        raise ValueError("notes must not be empty")
    with open(path, "a") as fh:
        for n in notes:
            fh.write(n + "\n")

if __name__ == "__main__":
    print(format_note("feat", "initial shipit skeleton"))