import pytest
from src.n_queens import NQueensSolver

def test_n_queens_4():
    """测试 N=4 的情况，应该有 2 个解"""
    solver = NQueensSolver(4)
    solutions = solver.solve()
    assert len(solutions) == 2

def test_n_queens_8():
    """测试 N=8 (标准八皇后)，应该有 92 个解"""
    solver = NQueensSolver(8)
    solutions = solver.solve()
    assert len(solutions) == 92

def test_n_queens_1():
    """测试 N=1 边界情况，应该有 1 个解"""
    solver = NQueensSolver(1)
    solutions = solver.solve()
    assert len(solutions) == 1

def test_n_queens_2_3():
    """测试 N=2 和 N=3，应该无解"""
    assert len(NQueensSolver(2).solve()) == 0
    assert len(NQueensSolver(3).solve()) == 0
