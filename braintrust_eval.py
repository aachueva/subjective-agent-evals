"""Run the sample playlist evaluation as a real Braintrust experiment."""

from __future__ import annotations

from braintrust import Eval

from src.scoring import deterministic_score


DATA = [
    {
        "input": {
            "request": "Create a 3-track upbeat playlist under 15 minutes with no repeated artists.",
            "track_count": 3,
            "max_minutes": 15,
            "max_tracks_per_artist": 1,
        },
        "expected": None,
    }
]


def demo_agent(input: dict) -> list[dict]:
    """Deterministic stand-in agent so the eval runs without a model API key."""
    return [
        {"title": "First Light", "artist": "Artist One", "genre": "indie pop", "duration_seconds": 240},
        {"title": "Momentum", "artist": "Artist Two", "genre": "electronic", "duration_seconds": 250},
        {"title": "Open Road", "artist": "Artist Three", "genre": "indie pop", "duration_seconds": 230},
    ]


def constraints(output, expected, input):
    scores = deterministic_score(output, input)
    return scores["overall"]


Eval(
    "subjective-agent-evals",
    data=lambda: DATA,
    task=demo_agent,
    scores=[constraints],
    metadata={"portfolio_project": True, "evaluation_type": "deterministic-baseline"},
)
