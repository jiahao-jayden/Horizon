from __future__ import annotations

from src.ai.utils import parse_json_response


def test_direct_json_object() -> None:
    assert parse_json_response('{"a": 1, "b": "x"}') == {"a": 1, "b": "x"}


def test_direct_json_with_surrounding_whitespace() -> None:
    assert parse_json_response('  \n {"ok": true} \n ') == {"ok": True}


def test_json_fenced_code_block() -> None:
    text = 'Here is the result:\n```json\n{"score": 5}\n```\nThanks!'
    assert parse_json_response(text) == {"score": 5}


def test_generic_fenced_code_block() -> None:
    text = 'Result:\n```\n{"value": [1, 2, 3]}\n```'
    assert parse_json_response(text) == {"value": [1, 2, 3]}


def test_brace_matching_with_leading_and_trailing_prose() -> None:
    text = 'The answer is {"nested": {"deep": true}} and nothing more.'
    assert parse_json_response(text) == {"nested": {"deep": True}}


def test_brace_matching_ignores_trailing_garbage() -> None:
    text = 'prefix {"a": 1} suffix } extra {'
    assert parse_json_response(text) == {"a": 1}


def test_regex_fallback_when_brace_match_fails() -> None:
    # Brace-matching counts the "}" inside the string and closes early, so
    # json.loads on the truncated block fails; the greedy regex fallback then
    # recovers the whole valid object.
    text = 'result: {"a": "}"}'
    assert parse_json_response(text) == {"a": "}"}


def test_returns_none_for_non_json() -> None:
    assert parse_json_response("just some plain text, no json here") is None


def test_returns_none_for_empty_string() -> None:
    assert parse_json_response("") is None


def test_fenced_block_preferred_over_direct_parse_failure() -> None:
    text = 'blah blah ```json {"picked": "yes"} ``` blah'
    assert parse_json_response(text) == {"picked": "yes"}


def test_all_strategies_exhausted_returns_none() -> None:
    # A truly malformed object that no strategy can repair.
    text = '```json\n{"broken": }\n```'
    assert parse_json_response(text) is None
