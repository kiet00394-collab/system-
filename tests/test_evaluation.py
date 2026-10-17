import numpy as np
import pytest
from evaluation import avg_satisfaction, run_experiment

def test_avg_satisfaction():
    # 2 sinh viên ghép cặp: a=0, b=1
    match = {0: 1}
    M = np.zeros((2, 2))
    M[0][1] = 80.0
    M[1][0] = 90.0
    sat = avg_satisfaction(match, M)
    assert sat == 85.0

def test_avg_satisfaction_empty_match():
    assert avg_satisfaction({}, np.zeros((2, 2))) == 0.0

def test_run_experiment_structure_and_validity():
    res = run_experiment(n=20, seed=42, n_random=10)
    assert res["n"] == 20
    assert "gs" in res
    assert "random" in res
    assert "blocking_pairs" in res
    # Gale-Shapley phải luôn đảm bảo 0 cặp chặn
    assert res["blocking_pairs"] == 0
    # Thang điểm hài lòng trong đoạn [0, 100]
    assert 0.0 <= res["gs"] <= 100.0
    assert 0.0 <= res["random"] <= 100.0
