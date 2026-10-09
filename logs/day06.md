# Day 6 — Similarity Calculations

Date: October 9, 2026
Time spent: 138 mins

## Goal

Build the full similarity-scoring pipeline by combining the player datasets and comparing each candidate against Kobe Bryant across the project's 10 categories.

## Work completed

- Combined traditional, advanced, shooting tendency, and physical datasets for the 70-player candidate pool.
- Added Kobe's career reference values.
- Added height and weight to the Stature category.
- Implemented metric-level percentage similarity.
- Calculated category-level similarity scores.
- Calculated the overall similarity score using an equal-weight average across the 10 categories.
- Added the remaining three categories to complete the 10-category framework.
- Saved the unified dataset and similarity outputs.

## Categories

1. Stature
2. Usage & Creation
3. Shooting Tendencies
4. Portability
5. Passing
6. Defense
7. Athleticism
8. Dominance
9. Shooting Ability
10. Play Style

## Current top 10

| Rank | Player | Similarity |
|---|---|---:|
| 1 | Jaylen Brown | 82.82 |
| 2 | Devin Booker | 81.48 |
| 3 | Stephen Curry | 80.23 |
| 4 | Julius Randle | 79.07 |
| 5 | Austin Reaves | 77.86 |
| 6 | Anthony Edwards | 77.84 |
| 7 | Pascal Siakam | 77.72 |
| 8 | Donovan Mitchell | 76.58 |
| 9 | Franz Wagner | 76.53 |
| 10 | Paolo Banchero | 75.96 |

## Notes

All 70 candidates now receive scores across all 10 categories.

Some categories use project-defined proxy metrics where the exact specialized source metric was not available in the current data pipeline. These proxies will be documented as a limitation during validation.

The ranking is therefore the current model output and will be subjected to validation and cleanup before the final project conclusion.