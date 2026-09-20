# Day 1 — Defining the Project

Date: September 20, 2026
Time spent: 56 minutes

## Goal

Turn an NBA comparison question I've thought about into a structured data-analysis project.

## Work completed

- Created the GitHub repository.
- Set up a Python virtual environment.
- Defined the main research question.
- Brainstormed possible dimensions of player similarity.
- Wrote my first simple similarity function.

## Main idea

I realized that comparing players only through box-score statistics would miss a major part of the question. I want the eventual model to consider not only what players produce but how they produce it.
A player can pass the eye test, but what shows up in the box score can validate that impression—or completely challenge it. At the same time, one explosive game or even a ten-game 20-point stretch doesn’t define a player; sustained performance across an entire season tells a much stronger story.
Even season averages only tell part of that story: two players can produce similar numbers while getting there through completely different shot selection, roles, and styles of play.

## Coding

I experimented with percentage difference as a simple way of measuring similarity between two numerical values.

## What I still don't know

- Whether percentage difference is the best similarity method
- Which advanced statistics are available historically for Kobe
- Whether career Kobe or prime Kobe is the better reference
- How different categories should be weighted

## Next session

Investigate available NBA data sources and determine which statistics are realistically obtainable.