from src.main import main


def test_main_correct_working() -> None:
    assert main() is None
