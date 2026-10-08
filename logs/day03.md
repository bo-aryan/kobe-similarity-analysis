# Day 3 — Kobe Reference and Candidate Pool

Date: September 23, 2026
Time spent: 68 minutes

This session established the statistical foundation for the similarity analysis.

I used Kobe Bryant's complete NBA career as the initial reference rather than selecting a specific subset of seasons. Career totals were converted into career per-game and shooting-efficiency reference values.

I also created a candidate pool of 70 current NBA players and retrieved their 2025–26 regular-season statistics through `nba_api`.

A preliminary similarity calculation was tested using traditional box-score and shooting metrics. This is not the final model; it is a validation step before adding the additional categories needed to capture playing style.

### Candidate pool issue

Two players I had originally considered did not play in 2025–26, so they could not be used as current-player comparisons for this version of the project. I replaced them with Nikola Jokic and Jalen Williams and kept the pool at 70 players.

### What I learned

Traditional statistics can identify players with similar production, but they do not fully describe how that production is generated. This reinforces the original research question: the final model needs to combine production with stylistic and role-based metrics.

### Next session

Build the additional metric dataset needed to compare playing style, then organize the metrics into the project's ten similarity categories.