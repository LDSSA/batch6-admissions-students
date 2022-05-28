import numpy as np


def test_exercise_4(answers):
    expected = {
        "question_1": 3,
        "question_2": 3,
        "question_3": 2,
        "question_4": 4,
        "question_5": 1,
        "question_6": 1,
        "question_7": 4,
        "question_8": 2,
        "question_9": 2,
        "question_10": 1,
        "question_11": 2,
        "question_12": 3,
        "question_13": 4,
        "question_14": 1,
    }

    assert isinstance(answers, dict)
    try:
        for k in answers.keys():
            q, n = k.split('_')
            assert q == 'question'
            assert 1 <= int(n) <= 14
    except AssertionError:
        raise AssertionError("Answers dict has unexpected keys")

    score = 0
    for k in expected.keys():
        if k not in answers:
            continue
        if expected[k] == answers[k]:
            score += 1

    final_score = int(round(score * 5 / 14))
    if final_score == 0:
        raise AssertionError("Not enough correct answers to score points :(")

    print(f"{score} correct answers. Your score is {final_score}.")
    
    return final_score
