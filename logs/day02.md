# Day 2 — Building the First Data Pipeline

Date: September 21, 2026
Time spent: 79 minutes

## Goal

Move from a conceptual similarity model to a reproducible data pipeline using real NBA data.

## Work completed

- Set up and activated the project virtual environment.
- Installed and tested `nba_api`.
- Used the NBA player directory to identify Kobe Bryant's NBA player ID (`977`).
- Used the `PlayerCareerStats` endpoint to retrieve his season-by-season career statistics.
- Loaded the API response into a pandas DataFrame and inspected its shape, columns, and first few rows.
- Saved the untouched API output to `data/raw/kobe_career_stats.csv`.
- Created an initial working structure for the metrics that will eventually feed the similarity model.
- Began separating raw data from manually collected or processed metrics.

## Main idea

I wanted the project to move beyond manually copying statistics into a table.

By pulling Kobe's career data programmatically, I can regenerate the same dataset whenever needed and keep the raw source separate from later calculations.

This also made it clear that traditional box-score statistics only capture part of a player's game. If I want to compare style as well as production, I will need to combine this dataset with more advanced metrics and other reliable sources.

## Coding

I used `nba_api` to search for Kobe Bryant in the NBA player database, retrieve his player ID, call the `PlayerCareerStats` endpoint, and convert the result into a pandas DataFrame.

I also saved the result as a CSV so the raw dataset can be reused and checked independently of the API call.

## Problem I hit

When I checked the installed packages in Windows PowerShell, FINDSTR caused a Unicode/encoding issue with the generated requirements output. I switched to PowerShell's Select-String and saved the file using UTF-8.

## What I still don't know

- Whether the final Kobe reference should use his full career or a defined prime period
- Which advanced metrics are available consistently for both Kobe and current players
- Which playing-style metrics can be calculated directly from NBA data
- Which additional data sources will be needed
- How many current players should be included in the initial comparison pool

## Next session

Analyze Kobe's season-by-season career data and decide how the reference version of Kobe should be defined before building the current-player comparison pool.