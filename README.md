# Kobe Similarity Analysis

The Kobe jersey that hangs above my table always served as a constant reminder of the work one needs to put in to reach greatness. But my curiosity for NBA analytics took me on a journey to find Kobe's modern match.
<img width="1064" height="1600" alt="image" src="https://github.com/user-attachments/assets/700be13f-f46d-4794-b62b-1449ddc9bd79" />

> Which current NBA player is most statistically and stylistically similar to Kobe Bryant?

This project tests a simple question: if Kobe Bryant's full career profile is treated as the reference, which current player comes out closest across a broad set of statistical and stylistic attributes?

The model compares 70 players across 10 categories and produces a single similarity score from 0–100.

## The result

### Jaylen Brown — 82.82% similarity

Under the validated Day 7 model, Jaylen Brown ranks #1.



The result is not meant to say that Brown is "the next Kobe." It means that, within this model and its selected metrics, his profile is the closest match among the 70-player candidate pool.

## Top 10



| Rank | Player           | Similarity |
| ---: | ---------------- | ---------: |
|    1 | Jaylen Brown     |     82.82% |
|    2 | Devin Booker     |     81.48% |
|    3 | Stephen Curry    |     80.23% |
|    4 | Julius Randle    |     79.07% |
|    5 | Austin Reaves    |     77.86% |
|    6 | Anthony Edwards  |     77.84% |
|    7 | Pascal Siakam    |     77.72% |
|    8 | Donovan Mitchell |     76.58% |
|    9 | Franz Wagner     |     76.53% |
|   10 | Paolo Banchero   |     75.96% |

## Category profiles

Each radar chart shows how closely a player matches Kobe across the 10 model categories.

The dashed outer boundary represents Kobe's reference value of 100. The green polygon represents the candidate's category-level similarity.

\<table>
\<tr>
\<td>\<img src="assets/radars/jaylen_brown_radar.png" width="420">\</td>
\<td>\<img src="assets/radars/devin_booker_radar.png" width="420">\</td>
\</tr>
\<tr>
\<td>\<img src="assets/radars/stephen_curry_radar.png" width="420">\</td>
\<td>\<img src="assets/radars/julius_randle_radar.png" width="420">\</td>
\</tr>
\<tr>
\<td>\<img src="assets/radars/austin_reaves_radar.png" width="420">\</td>
\<td>\</td>
\</tr>
\</table>

## How the model works

The project uses Kobe's full career as the reference rather than selecting a single season or a "prime" window.

Players are compared across 10 categories:

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

For each metric, the candidate receives a percentage similarity to Kobe's reference value:

```text
similarity = 100 × (1 − |candidate − reference| / |reference|)
```

Scores are floored at 0. Metrics within each category are averaged, and the 10 category scores are then averaged equally to produce the final score.

## Data pipeline

```text
NBA data
   ↓
Kobe career reference
   ↓
70-player candidate pool
   ↓
Traditional + advanced + shot-location + physical data
   ↓
Metric-level similarity
   ↓
Category-level similarity
   ↓
Overall ranking
```

### Data used

- Kobe reference: full NBA career
- Candidate pool: 70 current players
- Candidate season: 2025–26 regular season
- Data source: NBA statistics through `nba_api`
- Final validated output: `candidate_ranking_validated_2025_26.csv`

## Important limitations

This model is intentionally simple enough to inspect and reproduce.

Some of the original specialized metrics were not available through the current data pipeline, so several categories use project-defined proxy metrics. These proxies are documented in the methodology rather than presented as official versions of the unavailable metrics.

The percentage-deviation formula also behaves differently for metrics near zero or with negative values. This is one reason the final score should be interpreted as a model-specific similarity measure, not an objective measurement of player identity or playing style.

The candidate pool is also limited to the 70 players selected for this project, so the ranking is conditional on that pool.

## Why I built it

Basketball comparisons often start with the eye test: a player's movement, shot selection, role, or scoring style can make them feel similar to another player.

I wanted to test how much of that similarity survives when the comparison is turned into data.

The goal was not to build the most complicated possible model. It was to build a transparent one, understand every step, and see where the numbers agree — or disagree — with basketball intuition.

## Repository structure

```text
kobe-similarity-analysis/
├── data/
│   ├── raw/
│   ├── manual/
│   └── processed/
├── docs/
├── logs/
├── notebooks/
├── src/
├── assets/
└── README.md
```

## Reproducibility

The analysis was built incrementally and documented in daily logs.

The repository contains the raw/processed data, analysis notebook, methodology documentation, similarity outputs, and visualization assets needed to follow the workflow from data collection to final ranking.

## Project status

- [x] Research question
- [x] Data pipeline
- [x] Kobe reference profile
- [x] 70-player candidate pool
- [x] 10-category similarity model
- [x] Validation
- [x] Final ranking
- [x] Visualizations
- [ ] Final README cleanup
