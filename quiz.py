import random
import time

questions = {
    "General Knowledge": [
        {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"}
    ],
    "Science": [
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"}
    ]
}

lifelines = {
    "50-50": "Eliminates two incorrect answers.",
    "Ask the Audience": "Allows you to see the percentage of audience votes for each option."
}

def choose_question(category):
    return random.choice(questions[category])

def use_lifeline(lifeline, question):
    if lifeline == "50-50":
        answers = [question["answer"]]
        while len(answers) < 3:
            random_question = choose_question(category)
            answer = random_question["answer"]
            if answer not in answers:
                answers.append(answer)
        random.shuffle(answers)
        return answers
    elif lifeline == "Ask the Audience":
        audience_response = {"A": random.randint(0, 100), "B": random.randint(0, 100), "C": random.randint(0, 100)}
        audience_response[question["answer"]] += random.randint(10, 30)
        total = sum(audience_response.values())
        audience_response = {key: round((value / total) * 100) for key, value in audience_response.items()}
        return audience_response

print("Welcome to the Quiz Game!")
while True:
    category = input("\nChoose a category (General Knowledge, Science): ").capitalize()
    if category not in questions:
        print("Invalid category. Please choose again.")
        continue
    
    question = choose_question(category)
    print("\nCategory:", category)
    print("Question:", question["question"])

    timer = 10
    while timer > 0:
        print(f"Time left: {timer} seconds", end="\r")
        time.sleep(1)
        timer -= 1

    lifeline = input("Choose a lifeline (50-50, Ask the Audience) or type 'Skip' to skip the question: ")
    if lifeline in lifelines:
        if lifeline == "Skip":
            continue
        elif lifeline == "50-50":
            answers = use_lifeline(lifeline, question)
            print(f"\n50-50: {answers}")
            answer = input("Enter your answer: ")
        elif lifeline == "Ask the Audience":
            audience_response = use_lifeline(lifeline, question)
            print("\nAudience Response:")
            for key, value in audience_response.items():
                print(f"{key}: {value}%")
            answer = input("Enter your answer: ")
    else:
        answer = input("Enter your answer: ")

    if answer.lower() == question["answer"].lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
