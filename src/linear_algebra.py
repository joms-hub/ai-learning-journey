import math
Vector = list[float]
Matrix = list[Vector]

def add(v1: Vector, v2: Vector) -> Vector:
    return [x + y for x, y in zip(v1, v2)]

def sum_vectors(vectors: list[Vector]) -> Vector:
    return [sum(values) for values in zip(*vectors)]

def subtract(v1: Vector, v2: Vector) -> Vector:
    return [x - y for x, y in zip(v1, v2)]

def dot(v1: Vector, v2: Vector) -> float:
    return sum(x * y for x, y in zip(v1, v2))

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * x for x in v]

def vector_mean(vectors: list[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, sum_vectors(vectors))

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def distance(v1: Vector, v2: Vector) -> float:
    return magnitude(subtract(v1, v2))

def shape(matrix: Matrix) -> tuple[int, int]:
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    return (num_rows, num_cols)


