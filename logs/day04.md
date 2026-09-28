# Day 4 — Advanced Metrics

Date: September 28, 2026
Time spent: 57 minutes

## Goal

Expand the comparison beyond traditional box-score statistics by collecting advanced metrics for Kobe Bryant and the 70-player candidate pool.

## Work completed

- Tested NBA API advanced statistics using `LeagueDashPlayerStats`.
- Retrieved 2025–26 advanced statistics for the 70-player candidate pool.
- Retrieved Kobe Bryant's advanced statistics for all 20 seasons of his NBA career.
- Verified that all selected advanced metrics were available for all 20 Kobe seasons.
- Created a minute-weighted career reference for Kobe.
- Saved the cleaned candidate advanced-stat dataset.
- Saved Kobe's career advanced-stat reference dataset.

## Advanced metrics collected

- Offensive Rating
- Defensive Rating
- Net Rating
- Assist Percentage
- Assist-to-Turnover Ratio
- Rebound Percentage
- Estimated Turnover Percentage
- Usage Percentage
- True Shooting Percentage
- Effective Field Goal Percentage
- Pace
- Player Impact Estimate

## Kobe reference

The career reference uses all 20 NBA seasons rather than selecting a specific prime period.

Because the advanced statistics are season-level values, career reference values were calculated using total minutes as the weighting factor.

## Main idea

The traditional statistics from the previous session describe what Kobe produced. The advanced statistics add information about efficiency, usage, passing, rebounding, turnovers, and overall impact.

Using the same NBA API source for Kobe's historical data and the current-player data also keeps the metric definitions consistent within the project.

## What I learned

Advanced statistics provide more context than traditional box-score numbers, but not every available metric necessarily belongs in the final similarity model.

The next step is therefore to map the available data to the ten categories used in the comparison methodology rather than simply including every statistic collected.

## Data outputs

- `data/processed/candidate_advanced_clean_2025_26.csv`
- `data/processed/kobe_advanced_reference.csv`

## Next session

Map the project's available statistics to the ten comparison categories and determine which metrics can be reproduced consistently.