def normalize(data: list[float]) -> list[float]:
    """Normalize a list of floats to the range [0, 1]."""
    (min_val, max_val) = (min(data), max(data))
    if max_val - min_val == 0:
        return [0.0 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]