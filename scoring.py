import numpy as np
from models import Student

WEIGHTS = {
    "sleep": 0.25,
    "wake": 0.10,
    "tidy": 0.20,
    "study": 0.10,
    "noise": 0.15,
    "smoke": 0.10,
    "guests": 0.05,
    "hobbies": 0.05
}

def criterion_sims(x: Student, y: Student) -> dict[str, float]:
    clip = lambda v: max(0.0, min(1.0, float(v)))
    union = x.hobbies | y.hobbies

    return {
        "sleep": clip(1.0 - abs(x.sleep - y.sleep) / 5.0),
        "wake": clip(1.0 - abs(x.wake - y.wake) / 5.0),
        "tidy": clip(1.0 - abs(x.tidy - y.tidy) / 4.0),
        "study": 1.0 if x.study == y.study else 0.0,
        "noise": clip(1.0 - abs(x.noise - y.noise) / 4.0),
        "smoke": 1.0 if x.smoke == y.smoke else 0.0,
        "guests": clip(1.0 - abs(x.guests - y.guests) / 4.0),
        "hobbies": float(len(x.hobbies & y.hobbies) / len(union)) if union else 0.0,
    }

def pair_score(x: Student, y: Student, weights: dict = WEIGHTS) -> float:
    w = dict(weights)
    if x.top in w:
        w[x.top] *= 1.5
    total_weight = sum(w.values())
    sims = criterion_sims(x, y)
    score = 100.0 * sum(w[k] * sims[k] for k in w) / total_weight
    return round(score, 2)

def compute_score_matrix(students: list[Student], weights: dict = WEIGHTS) -> np.ndarray:
    n = len(students)
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i][j] = pair_score(students[i], students[j], weights)
    return M

def build_pref_lists(M: np.ndarray, students: list[Student]) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    ids_a = [s.id for s in students if s.group == "A"]
    ids_b = [s.id for s in students if s.group == "B"]

    pref_a = {a: sorted(ids_b, key=lambda b: -M[a][b]) for a in ids_a}
    pref_b = {b: sorted(ids_a, key=lambda a: -M[b][a]) for b in ids_b}

    return pref_a, pref_b
