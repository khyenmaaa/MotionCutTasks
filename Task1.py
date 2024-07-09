def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["a. New Delhi", "b. West Bengal", "c. Maharashtra", "d. Assam"],
            "answer": "a"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["a. Earth", "b. Mars", "c. Jupiter", "d. Saturn"],
            "answer": "c"
        },
        {
            "question": "Which network protocol is called connection-oriented protocol?",
            "options": ["a. TCP", "b. UDP", "c. FTP", "d. HTTP"],
            "answer": "a"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["a. 6", "b. 7", "c. 8", "d. 9"],
            "answer": "c"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["a. O2", "b. H2O", "c. CO2", "d. NaCl"],
            "answer": "b"
        }
    ]
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (a, b, c, d): ").lower()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

        print()

    print(f"Your final score is {score}/{len(questions)}")

quiz_game()
