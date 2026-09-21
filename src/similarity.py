def percentage_similarity(reference, candidate):
    difference = abs(candidate - reference)

    percentage_difference = difference / abs(reference)

    similarity = 100 * (1 - percentage_difference)

    return max(0, similarity)

if __name__ == "__main__":
    kobe_height = 78
    example_player_height = 77

    score = percentage_similarity(
        kobe_height,
        example_player_height
    )

    print(round(score, 2))
