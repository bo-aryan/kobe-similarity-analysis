from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

kobe = players.find_players_by_full_name("Kobe Bryant")

print(kobe)
from nba_api.stats.endpoints import playercareerstats

kobe_id = 977

career = playercareerstats.PlayerCareerStats(player_id=kobe_id)

kobe_seasons = career.get_data_frames()[0]

print(kobe_seasons.head())
print("\nColumns:")
print(kobe_seasons.columns.tolist())