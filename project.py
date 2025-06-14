import json
import random
import datetime
import os

QUESTIONS_FILE = "questions.json"
ANSWERS_LOG = "answers_log.txt"

def load_questions():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_answer(q, a):
    with open(ANSWERS_LOG, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}]\nQ: {q}\nA: {a}\n\n")

def practice_mode(qs):
    if len(qs) == 0:
        print("no questions to practice")
        return

    random.shuffle(qs)
    print("\n--- Practice ---")
    for q in qs:
        print("\nQ:", q)
        a = input("Your Answer: ")
        save_answer(q, a)
        print("saved!\n")

def review_samples(qdict):
    print("\n-- sample answers --")
    for q in qdict:
        samp = qdict[q].get("sample", "[no sample]")
        print(f"\nQ: {q}\nSample: {samp}")

def add_question():
    q = input("question: ")
    samp = input("sample answer (opt): ")
    qs = load_questions()
    qdict = {x["question"]: x for x in qs}
    qdict[q] = {"question": q, "sample": samp}
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(list(qdict.values()), f, indent=4)
    print("added.")

def main():
    while True:
        print("\n== Visa Interview Helper ==")
        print("1. Practice Questions")
        print("2. Sample Answers")
        print("3. Add Question")
        print("4. Exit")

        opt = input("Choose: ")
        qdata = load_questions()
        qdict = {x["question"]: x for x in qdata}

        if opt == "1":
            practice_mode(list(qdict.keys()))
        elif opt == "2":
            review_samples(qdict)
        elif opt == "3":
            add_question()
        elif opt == "4":
            print("Ok bye. Good luck. 🙂")
            break
        else:
            print("try again")

if __name__ == "__main__":
    main()