import pytest
from shipit import format_note, release_header

def test_format_note_happy():
    assert format_note("feat", "x") == "- ✨ [FEAT] x"

def test_format_note_rejects_unknown_kind():
    with pytest.raises(ValueError):
        format_note("banana", "x")

def test_release_header_contains_version():
    assert "1.2.3" in release_header("1.2.3")

def test_release_header_rejects_empty():
    with pytest.raises(ValueError):
        release_header("")