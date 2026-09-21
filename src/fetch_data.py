from pathlib import Path

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


# Find Kobe Bryant in the NBA player database
matches = players.find_players_by_full_name("Kobe Bryant")

if not matches:
    raise ValueError("Kobe Bryant was not found in the NBA player database.")

kobe = matches[0]
kobe_id = kobe["id"]

print(f"Found {kobe['full_name']} — NBA player ID: {kobe_id}")


# Retrieve season-by-season career statistics
career = playercareerstats.PlayerCareerStats(player_id=kobe_id)

kobe_seasons = career.get_data_frames()[0]


# Inspect the returned dataset
print("\nFirst five seasons:")
print(kobe_seasons.head())

print("\nDataset shape:")
print(kobe_seasons.shape)

print("\nColumns:")
print(kobe_seasons.columns.tolist())


# Save the untouched API response
output_path = Path("data/raw/kobe_career_stats.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

kobe_seasons.to_csv(output_path, index=False)

print(f"\nSaved raw data to: {output_path}")