def generate_question():
    import random
    operation = random.choice(['+', '-'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    
    question = f"What is {num1} {operation} {num2}?"
    return question, answer

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def play_game():
    correct_count = 0
    for _ in range(3):
        question, correct_answer = generate_question()
        user_answer = int(input(question + " "))
        if check_answer(user_answer, correct_answer):
            correct_count += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    print(f"You got {correct_count} out of 3 questions correct.")