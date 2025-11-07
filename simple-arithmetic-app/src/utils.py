def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def format_question(num1, num2, operation):
    return f"What is {num1} {operation} {num2}?"

def format_result(correct_count, total_questions):
    return f"You got {correct_count} out of {total_questions} questions correct!"