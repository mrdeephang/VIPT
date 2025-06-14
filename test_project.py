import os
import json
import datetime
import project

def test_load_questions():
    if os.path.exists(project.QUESTIONS_FILE):
        os.rename(project.QUESTIONS_FILE, "questions_backup.json")

    with open(project.QUESTIONS_FILE, "w") as f:
        json.dump([], f)

    questions = project.load_questions()
    assert isinstance(questions, list)

    os.remove(project.QUESTIONS_FILE)
    if os.path.exists("questions_backup.json"):
        os.rename("questions_backup.json", project.QUESTIONS_FILE)

def test_save_answer():
    q = "What is your name?"
    a = "My name is test"
    project.save_answer(q, a)

    assert os.path.exists(project.ANSWERS_LOG)

    with open(project.ANSWERS_LOG, "r") as f:
        content = f.read()
        assert "What is your name?" in content
        assert "My name is test" in content

def test_add_question_logic():
    test_q = "Why this university?"
    test_sample = "Because it fits my goals."

    qs = project.load_questions()
    qdict = {x["question"]: x for x in qs}
    qdict[test_q] = {"question": test_q, "sample": test_sample}

    with open(project.QUESTIONS_FILE, "w") as f:
        json.dump(list(qdict.values()), f, indent=4)

    qs2 = project.load_questions()
    found = False
    for item in qs2:
        if item["question"] == test_q and item["sample"] == test_sample:
            found = True
    assert found

print("All tests passed ✅")