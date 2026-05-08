import numpy as np

def cosine_similarity(a, b):

    A = np.array(a, dtype=float)
    B = np.array(b, dtype=float)

    dot_result = np.dot(A, B)

    norm_result = np.linalg.norm(A) * np.linalg.norm(B)

    if norm_result == 0:
        return 0.0

    return dot_result / norm_result