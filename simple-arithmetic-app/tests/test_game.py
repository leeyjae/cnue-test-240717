import pytest
from src.game import generate_question, check_answer

def test_generate_question():
    question, answer = generate_question()
    assert isinstance(question, str)
    assert isinstance(answer, int)

def test_check_answer_correct():
    assert check_answer(5, 5) == True

def test_check_answer_incorrect():
    assert check_answer(5, 3) == False

def test_generate_question_range():
    question, answer = generate_question()
    # Assuming the question is in the form "x + y" or "x - y"
    assert '+' in question or '-' in question
    assert 0 <= answer <= 20  # Assuming the answer is within a reasonable range for the game