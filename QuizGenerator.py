import random

def quiz_game():
    print("Welcome to the Quiz Game!\n")

    # List of questions and answers
    questions = [
        ("What is the capital of France?", "paris"),
        ("Which planet is known as the Red Planet?", "mars"),
        ("What is the square root of 64?", "8"),
        ("Who wrote 'To Kill a Mockingbird'?", "harper lee"),
        ("What is the chemical symbol for water?", "h2o"),
        ("What is the largest mammal in the world?", "blue whale"),
        ("How many continents are there on Earth?", "7"),
        ("What is the speed of light in vacuum? (in km/s)", "299792"),
        ("Who developed the theory of relativity?", "einstein"),
        ("What is the powerhouse of the cell?", "mitochondria"),
        ("Which is the longest river in the world?", "nile"),
        ("What is the capital of Japan?", "tokyo"),
        ("Who painted the Mona Lisa?", "leonardo da vinci"),
        ("How many players are there in a soccer team?", "11"),
        ("What gas do plants absorb from the atmosphere?", "carbon dioxide"),
        ("What is the smallest prime number?", "2"),
        ("Which metal is liquid at room temperature?", "mercury"),
        ("What is the chemical formula for table salt?", "nacl"),
        ("Which country is famous for pizza and pasta?", "italy"),
        ("What is the name of the closest star to Earth?", "sun"),
    ]

    # Shuffle questions to randomize order
    random.shuffle(questions)

    score = 0  # Track user score

    for question, correct_answer in questions:
        user_answer = input(question + " ").strip().lower()
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}.\n")

    print(f"🎉 Game Over! Your final score is {score}/{len(questions)}.")

# Run the quiz
quiz_game()
