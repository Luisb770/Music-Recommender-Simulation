"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

It uses:
- load_songs to load the dataset
- recommend_songs to generate recommendations
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    # Load songs from CSV
    songs = load_songs("data/songs.csv")

    # Example user profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "likes_acoustic": False
    }

    # Get recommendations
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations:\n")

    for song, score, explanation in recommendations:
        print(f"{song['title']} by {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Because: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()