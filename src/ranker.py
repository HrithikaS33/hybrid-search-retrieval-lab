def reciprocal_rank_fusion(result_sets: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for results in result_sets:
        for rank, doc_id in enumerate(results, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1 / (k + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


def apply_freshness_boost(score: float, is_current_policy: bool) -> float:
    return score * 1.12 if is_current_policy else score
