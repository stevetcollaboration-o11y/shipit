"""shipit: tiny release-notes helper."""

def format_note(kind: str, text: str) -> str:
    """Format one changelog line, e.g. '- [feat] add login page'."""
    return f"- [{kind}] {text}"

if __name__ == __main__":
    print(format_note("feat", "initial shipit skeleton"))