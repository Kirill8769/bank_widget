import pytest

from src.utils import get_transactions, filepath

def test_get_transactions_correct_path():
    assert get_transactions(filepath) == ""