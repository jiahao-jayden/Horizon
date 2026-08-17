"""Shared AI utility functions."""

import asyncio
import json
import re
from collections.abc import Awaitable, Callable, Sequence
from typing import Optional, TypeVar

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
)


T = TypeVar("T")
R = TypeVar("R")


async def run_with_progress(
    items: Sequence[T],
    worker: Callable[[T, int], Awaitable[R]],
    *,
    concurrency: int,
    description: str,
) -> list[R]:
    """Run async work with bounded concurrency and a shared progress display."""
    semaphore = asyncio.Semaphore(max(concurrency, 1))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task(description, total=len(items))

        async def process(item: T, index: int) -> R:
            async with semaphore:
                result = await worker(item, index)
            progress.advance(task)
            return result

        return list(
            await asyncio.gather(
                *(process(item, index) for index, item in enumerate(items))
            )
        )


def parse_json_response(response: str) -> Optional[dict]:
    """Try multiple strategies to extract a JSON object from an AI response.

    Returns the parsed dict, or None if all strategies fail.
    """
    text = response.strip()

    # Strategy 1: direct parse
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Strategy 2: extract from ```json ... ``` code block
    if "```json" in text:
        try:
            json_str = text.split("```json")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 3: extract from ``` ... ``` code block
    if "```" in text:
        try:
            json_str = text.split("```")[1].split("```")[0].strip()
            return json.loads(json_str)
        except (json.JSONDecodeError, ValueError, IndexError):
            pass

    # Strategy 4: find the first { ... } block using brace matching
    start = text.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except (json.JSONDecodeError, ValueError):
                        break

    # Strategy 5: regex extraction as last resort
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except (json.JSONDecodeError, ValueError):
            pass

    return None
