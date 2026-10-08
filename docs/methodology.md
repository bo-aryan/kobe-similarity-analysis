# Methodology

## Research Question

Which current NBA player is most statistically and stylistically similar to Kobe Bryant?

## Overall approach

The project uses a category-based similarity model.

The current comparison pool contains 70 NBA players. Each player will be compared with Kobe across 10 categories:

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

The categories are meant to cover both production and playing style instead of relying only on points, rebounds and assists.

## Similarity calculation

For an individual numerical metric, similarity is calculated using percentage deviation:

Similarity = 100 × (1 − |candidate − Kobe| / |Kobe|)

Scores are capped at a minimum of 0.

When a category contains multiple metrics, the metric similarity scores are averaged to produce the category score.

The final player score is the equal-weighted average of the 10 category scores.

The highest-scoring player is therefore the closest match under this particular model.

## Kobe reference

Kobe Bryant's full regular-season NBA career is used as the reference profile.

For traditional statistics, career values are calculated from career totals rather than averaging individual season averages.

For season-level advanced metrics, the Kobe reference uses a minute-weighted career value.

For shooting tendencies, season-level shot-location attempts are weighted by games played before being combined into a career shot profile.

## Data limitations

Not every metric from the reference framework can be reproduced directly from the NBA API.

I will not replace unavailable specialized metrics with made-up values. If a metric cannot be collected consistently, that limitation will be stated and the final implementation will use only data that can actually be supported.

The model measures similarity according to the selected metrics. It does not prove that two players actually play identically, and the result could change if different metrics or category weights were used.
