"""Simple deterministic scorers for agent-output evaluation."""

from collections import Counter


def score_track_count(tracks: list[dict], expected: int) -> float:
    return 1.0 if len(tracks) == expected else 0.0


def score_duration(tracks: list[dict], max_minutes: float) -> float:
    total_seconds = sum(float(track.get("duration_seconds", 0)) for track in tracks)
    return 1.0 if total_seconds <= max_minutes * 60 else 0.0


def score_artist_variety(tracks: list[dict], max_tracks_per_artist: int = 1) -> float:
    artists = [str(track.get("artist", "")).strip().lower() for track in tracks]
    if not artists or any(not artist for artist in artists):
        return 0.0
    counts = Counter(artists)
    violations = sum(max(0, count - max_tracks_per_artist) for count in counts.values())
    return max(0.0, 1.0 - violations / len(tracks))


def score_required_genres(
    tracks: list[dict], required_genres: list[str], minimum_per_genre: int
) -> float:
    if not required_genres:
        return 1.0
    genres = [str(track.get("genre", "")).strip().lower() for track in tracks]
    passed = 0
    for genre in required_genres:
        if sum(item == genre.lower() for item in genres) >= minimum_per_genre:
            passed += 1
    return passed / len(required_genres)


def deterministic_score(tracks: list[dict], case: dict) -> dict[str, float]:
    scores = {
        "track_count": score_track_count(tracks, int(case["track_count"])),
        "artist_variety": score_artist_variety(
            tracks, int(case.get("max_tracks_per_artist", len(tracks) or 1))
        ),
    }
    if "max_minutes" in case:
        scores["duration"] = score_duration(tracks, float(case["max_minutes"]))
    if "required_genres" in case:
        scores["genre_balance"] = score_required_genres(
            tracks,
            list(case["required_genres"]),
            int(case.get("min_tracks_per_required_genre", 1)),
        )
    scores["overall"] = sum(scores.values()) / len(scores)
    return scores
