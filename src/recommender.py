import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song(self, user: UserProfile, song: Song) -> float:
        score = 0.0

        # Strong weight for exact genre match
        if song.genre == user.favorite_genre:
            score += 3.0
        # Partial credit for related genre names like "pop" and "indie pop"
        elif user.favorite_genre in song.genre or song.genre in user.favorite_genre:
            score += 1.5

        # Strong weight for exact mood match
        if song.mood == user.favorite_mood:
            score += 2.5

        # Smooth energy scoring instead of all-or-nothing
        energy_difference = abs(song.energy - user.target_energy)
        energy_score = max(0.0, 2.0 - (energy_difference * 4))
        score += energy_score

        # Acoustic preference as a gradual score
        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += (1.0 - song.acousticness)

        # Small bonus from other useful song features
        if user.favorite_mood in ["happy", "intense"]:
            score += song.valence * 0.3
            score += song.danceability * 0.2

        if user.favorite_mood in ["chill", "relaxed", "focused"]:
            score += song.acousticness * 0.2

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = self._score_song(user, song)
            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("it matches your favorite genre exactly")
        elif user.favorite_genre in song.genre or song.genre in user.favorite_genre:
            reasons.append("it is close to your favorite genre")

        if song.mood == user.favorite_mood:
            reasons.append("it matches your preferred mood")

        energy_difference = abs(song.energy - user.target_energy)
        if energy_difference <= 0.10:
            reasons.append("its energy level is a very close match")
        elif energy_difference <= 0.25:
            reasons.append("its energy level is fairly close to what you like")

        if user.likes_acoustic and song.acousticness >= 0.60:
            reasons.append("it fits your acoustic preference")
        elif not user.likes_acoustic and song.acousticness <= 0.40:
            reasons.append("it fits your non-acoustic preference")

        if song.danceability >= 0.75:
            reasons.append("it has strong danceability")
        if song.valence >= 0.75:
            reasons.append("it has an upbeat feel")

        if not reasons:
            return "This song was recommended because it has a somewhat similar overall vibe."

        return "This song was recommended because " + ", ".join(reasons) + "."



def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    recommendations = []

    for song in songs:
        score = 0.0
        reasons = []

        # Genre scoring
        if song["genre"] == user_prefs["genre"]:
            score += 3.0
            reasons.append("matches your genre exactly")
        elif user_prefs["genre"] in song["genre"] or song["genre"] in user_prefs["genre"]:
            score += 1.5
            reasons.append("is close to your genre")

        # Mood scoring
        if song["mood"] == user_prefs["mood"]:
            score += 2.5
            reasons.append("matches your mood")

        # Smooth energy scoring
        energy_difference = abs(song["energy"] - user_prefs["energy"])
        energy_score = max(0.0, 2.0 - (energy_difference * 4))
        score += energy_score

        if energy_difference <= 0.10:
            reasons.append("has very similar energy")
        elif energy_difference <= 0.25:
            reasons.append("has fairly similar energy")

        # Small bonus features
        if user_prefs["mood"] in ["happy", "intense"]:
            score += song["valence"] * 0.3
            score += song["danceability"] * 0.2

        if user_prefs["mood"] in ["chill", "relaxed", "focused"]:
            score += song["acousticness"] * 0.2

        if song["danceability"] >= 0.75:
            reasons.append("has strong danceability")

        if song["valence"] >= 0.75:
            reasons.append("feels upbeat")

        explanation = ", ".join(reasons) if reasons else "has a somewhat similar overall vibe"
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda item: item[1], reverse=True)
    return recommendations[:k]