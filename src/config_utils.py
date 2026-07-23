"""Shared configuration helpers."""

import os
import re


_ENV_VAR_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


def expand_env_vars(value: object, *, strip_values: bool = False) -> object:
    """Recursively expand ``${VAR}`` references in string values.

    Unset variables remain unchanged. ``strip_values`` supports contexts such
    as URLs where surrounding whitespace in environment values is invalid.
    """
    if isinstance(value, str):

        def replace(match: re.Match[str]) -> str:
            replacement = os.environ.get(match.group(1))
            if replacement is None:
                return match.group(0)
            return replacement.strip() if strip_values else replacement

        return _ENV_VAR_PATTERN.sub(replace, value)
    if isinstance(value, dict):
        return {
            key: expand_env_vars(item, strip_values=strip_values)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [expand_env_vars(item, strip_values=strip_values) for item in value]
    if isinstance(value, tuple):
        return tuple(
            expand_env_vars(item, strip_values=strip_values)
            for item in value
        )
    return value
