# Data Sources

## NBA Stats

Access method: nba_api

The NBA API is the main source used so that Kobe's historical data and current-player data can be collected using consistent metric definitions where possible.

### PlayerCareerStats

Used to retrieve Kobe Bryant's season-by-season NBA career statistics.

Kobe Bryant NBA Player ID: 977

Raw output:

data/raw/kobe_career_stats.csv

The raw API output is kept unchanged. Calculations and transformations are stored separately.

### LeagueDashPlayerStats

Used for:

- 2025–26 traditional statistics for the 70-player candidate pool
- 2025–26 advanced statistics for the candidate pool
- Kobe Bryant's season-level advanced statistics across his career

The advanced endpoint required measure_type_detailed_defense="Advanced" with the installed nba_api version.

### LeagueDashPlayerShotLocations

Used to build the shooting-tendency profiles for Kobe and the current-player pool.

Six non-overlapping zones were used:

- Restricted Area
- In The Paint (Non-RA)
- Mid-Range
- Corner 3
- Above the Break 3
- Backcourt

The resulting frequencies are stored in the processed data directory.

## Access issues

I initially tried to pull some specialized metrics from CraftedNBA, but the request returned a 403 response. I switched away from that direct scrape instead of building the project around a source I could not reliably access.

Some specialized metrics therefore remain a limitation of the final model.
