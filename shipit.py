"""shipit: tiny release-notes helper."""

from datetime import date

def format_note(kind: str, text: str) -> str:
    """Format one changelog line, e.g. '- [feat] add login page'."""
    return f"- [{kind}] {text}"

def today():
    return date.today().isoformat()

if __name__ == __main__":
    print(format_note("feat", "initial shipit skeleton"))