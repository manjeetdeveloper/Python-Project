questions = {
    "Question 1: What is Python?": "a",
    "Question 2: List is?": "c",
    "Question 3: Tuple is?": "d",
    "Question 4: Which of the following is the correct extension of the Python file?": "a",
    "Question 5: Which keyword is used for function in Python language?": "b",
}

options = {
    "Question 1: What is Python?": ["(a) Programming Language", "(b) Snake", "(c) Movie", "(d) Car"],
    "Question 2: List is?": ["(a) Immutable", "(b) Error", "(c) Mutable", "(d) Function"],
    "Question 3: Tuple is?": ["(a) Imutable", "(b) Error", "(c) Mutable", "(d) Immutable"],
    "Question 4: Which of the following is the correct extension of the Python file?": ["(a) .py", "(b) Error", "(c) .html", "(d) .js"],
    "Question 5: Which keyword is used for function in Python language?": ["(a) fun", "(b) def", "(c) len", "(d) html"],
}

# Tracks the number of correct answers
score = 0

# Quiz Game Function
def quiz_game():
    global score
    print("Welcome to the Python Quiz!\n")

    for question, correct_answer in questions.items():
        print(question)
        for option in options[question]:
            print(option)
        
        # Take user's answer
        answer = input("Your answer (a, b, c, d): ").lower()

        # Check if the answer is correct
        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.\n")

    # Display final score
    print(f"Quiz Complete! Your final score is: {score} out of {len(questions)}")
    print(f"You answered {score} questions correctly out of {len(questions)}.")

# Start the quiz
quiz_game()
