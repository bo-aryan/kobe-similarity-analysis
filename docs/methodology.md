# Methodology

## Research Question

Which current NBA player is most statistically and stylistically similar to Kobe Bryant?

## Overall Approach

The project uses a category-based similarity model.

The analysis begins with a broad pool of current NBA players who have at least some plausible resemblance to Kobe's playing profile. The pool is then narrowed before the final scoring stage.

Each remaining player is evaluated across 10 categories:

1. Stature
2. Shot selection
3. Portability
4. Passing
5. Usage & creation
6. Defense
7. Play style
8. Athleticism
9. Shooting ability
10. Dominance

Within each category, individual metrics are compared with Kobe's corresponding career values.

Similarity is calculated using percentage deviation:

Similarity = 100 × (1 − |candidate − Kobe| / |Kobe|)

Similarity scores are capped at a minimum of 0.

When multiple metrics belong to the same category, their similarity scores are averaged to produce the category score.

The final player score is the equal-weighted average of the 10 category scores.

The player with the highest final score is considered the closest statistical and stylistic match under this model.

## Kobe Reference

Kobe Bryant's full regular-season NBA career is used as the reference profile.

Traditional statistics are calculated from career totals rather than averaging individual season averages.

## Important Limitation

This model measures similarity according to the selected metrics. It does not prove that two players actually play identically, and the final result can change if different metrics or category weights are used.