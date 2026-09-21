# Day 2

Date: September 21, 2026

Time spent: 79 minutes

## What I did

- Set up and activated the project virtual environment.
- Installed and tested `nba_api`.
- Found Kobe Bryant's NBA player ID (`977`).
- Used the NBA API's `PlayerCareerStats` endpoint to retrieve his season-by-season career statistics.
- Converted the API response into a pandas DataFrame and inspected its structure and available columns.
- Saved the untouched career dataset to `data/raw/kobe_career_stats.csv`.
- Created the initial structure for `player_metrics.csv`, which will eventually contain the metrics used in the similarity model.

## What I learned

- NBA Stats identifies players through unique player IDs, which makes it possible to retrieve data programmatically rather than downloading individual tables manually.
- `nba_api` returns data that can be converted directly into pandas DataFrames, making it easy to inspect, filter, and save for later analysis.
- Kobe's career data gives me plenty of traditional and some advanced statistics, but these alone will not describe playing style well enough for the final comparison.
- Metrics involving shot selection, offensive role, defensive versatility, and play style will require additional sources or calculations.

## Observations

- Kobe's career spans enough seasons that using a simple career average could hide major changes in his role and style over time.
- I will eventually need to decide whether the reference should represent his entire career or a defined prime period.

## Problems / Decisions

- The NBA API does not contain every metric I want for the project.
- I decided to keep the raw NBA API data untouched and build separate processed datasets later instead of manually editing the downloaded CSV.

## Next

- Research the advanced metrics needed for Kobe's reference profile.
- Decide which metrics can be calculated from existing NBA data and which require another reliable source.
- Begin defining the comparison-player pool.