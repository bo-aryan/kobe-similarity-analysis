# Kobe Similarity Analysis

## Question

Which current NBA player is most statistically and stylistically similar to Kobe Bryant?

I've followed basketball for years, and player comparisons have always interested me because the box score can make two players look similar while their actual styles are very different.

I want to turn that question into a quantitative analysis using Python and publicly available NBA data.

## What I'm comparing

The model looks at 10 parts of a player's game:

- stature
- shooting tendencies
- portability
- passing
- usage and creation
- defense
- athleticism
- dominance
- shooting ability
- play style

The idea is to measure both:

1. what a player produces
2. how that production is generated

## Current approach

Kobe Bryant's full regular-season career is the reference profile. The current comparison pool contains 70 NBA players, using their 2025–26 regular-season data.

The project uses a category-based similarity score. I'm keeping the metrics as simple and reproducible as possible, and documenting limitations instead of filling gaps with estimates.

## Tools

- Python
- pandas
- Jupyter
- Git/GitHub
- nba_api

## Repository structure

- data/raw/ — raw API data
- data/processed/ — cleaned datasets used by the analysis
- data/manual/ — manually defined inputs such as the candidate pool
- docs/ — methodology and research notes
- logs/ — session-by-session project notes
- notebooks/ — analysis work
- src/ — reusable Python code

This is a work-in-progress project, so the logs also record decisions and problems I ran into while building it.
