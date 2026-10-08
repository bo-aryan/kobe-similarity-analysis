# Day 5 — Metric Mapping

Date: October 8, 2026
Time spent: 107 minutes

## Goal

Map the ten comparison categories to reproducible metrics and collect the additional data required to measure shooting tendencies.

## Work completed

- Reviewed the ten-category structure used as the project's reference methodology.
- Confirmed the distinction between shooting tendencies and shooting ability.
- Tested the NBA API shot-location endpoint.
- Collected 2025–26 shot-location data for the 70-player candidate pool.
- Converted shot-location attempts into percentage-based shooting tendencies.
- Used six non-overlapping shot zones:
  - Restricted Area
  - In The Paint (Non-RA)
  - Mid-Range
  - Corner 3
  - Above the Break 3
  - Backcourt
- Collected Kobe Bryant's shot-location data across all 20 NBA seasons.
- Created a career shooting-tendency profile for Kobe using season-level shot attempts weighted by games played.
- Verified that the shooting-tendency percentages sum to 100%.
- Saved the candidate and Kobe shooting-tendency datasets.
- Established the metric mapping for all ten similarity categories.

## Ten comparison categories

1. Stature
2. Shooting Tendencies
3. Portability
4. Passing
5. Usage & Creation
6. Defense
7. Athleticism
8. Dominance
9. Shooting Ability
10. Play Style

## Main methodological decision

The project will reproduce the structure of the reference methodology while keeping the implementation transparent and reproducible.

Specialized metrics that cannot be reproduced reliably from the available NBA API data will not be replaced with arbitrary estimates. Any limitations will be documented before the final similarity model is constructed.

## Main idea

Traditional statistics describe what a player produces, while shooting tendencies help describe how that production is generated.

Keeping shot selection separate from shooting efficiency allows the final model to distinguish between players who shoot similarly and players who simply make shots at similar rates.

## Data outputs

- `data/processed/candidate_shot_profile_2025_26.csv`
- `data/processed/kobe_shot_profile_career.csv`

## What I learned

The NBA API provides enough consistent data to reproduce several parts of the comparison framework, but some specialized metrics require additional sources or may not be reproducible in exactly the same form.

This makes data availability an important part of the final methodology rather than something to work around with unsupported assumptions.

## Next session

Complete the remaining metric collection, resolve the availability of specialized metrics, and begin constructing the unified Kobe-versus-candidate dataset for similarity scoring.