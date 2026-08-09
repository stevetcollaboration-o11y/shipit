"""shipit: tiny release-notes helper."""

"""Import date"""
from datetime import date

def format_note(kind: str, text: str) -> str:
    """Format one changelog line, e.g. '- [feat] add login page'."""
    return f"- [{kind}] {text}"

def today() -> str:
    """Return today's date as an ISO string, e.g. '2026-08-08'."""
    return date.today().isoformat()

if __name__ == "__main__":
    print(format_note("feat", "initial shipit skeleton"))