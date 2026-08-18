from src.scoring import (
    deterministic_score,
    score_artist_variety,
    score_duration,
    score_required_genres,
    score_track_count,
)


TRACKS = [
    {"title": "A", "artist": "One", "genre": "indie pop", "duration_seconds": 240},
    {"title": "B", "artist": "Two", "genre": "electronic", "duration_seconds": 250},
    {"title": "C", "artist": "Three", "genre": "indie pop", "duration_seconds": 230},
]


def test_track_count():
    assert score_track_count(TRACKS, 3) == 1.0


def test_duration():
    assert score_duration(TRACKS, 15) == 1.0


def test_artist_variety():
    assert score_artist_variety(TRACKS) == 1.0


def test_artist_variety_detects_repeat():
    repeated = TRACKS + [{"title": "D", "artist": "One", "genre": "electronic"}]
    assert score_artist_variety(repeated) < 1.0


def test_required_genres():
    assert score_required_genres(TRACKS, ["indie pop", "electronic"], 1) == 1.0


def test_composite_score():
    case = {"track_count": 3, "max_minutes": 15, "max_tracks_per_artist": 1}
    assert deterministic_score(TRACKS, case)["overall"] == 1.0
