print("Welcome to the Python Quiz Challenge!")
quiz = {
    "Q1: Which function is used to display output in Python?": {
        "choices": ["A. echo()", "B. print()", "C. output()", "D. show()"],
        "answer": "b"
    },
    "Q2: What is the output of 2 ** 3?": {
        "choices": ["A. 6", "B. 8", "C. 5", "D. 9"],
        "answer": "b"
    },
    "Q3: Which function returns the number of characters in a string?": {
        "choices": ["A. length()", "B. count()", "C. len()", "D. size()"],
        "answer": "c"
    },
    "Q4: Which symbol is used to start a comment in Python?": {
        "choices": ["A. //", "B. /*", "C. #", "D. <!--"],
        "answer": "c"
    },
    "Q5: What is the correct file extension for Python files?": {
        "choices": ["A. .py", "B. .python", "C. .pt", "D. .pyt"],
        "answer": "a"
    },
    "Q6: What is the output of print(5 // 2)?": {
        "choices": ["A. 2.5", "B. 3", "C. 2", "D. 4"],
        "answer": "c"
    },
    "Q7: Which data type is used for decimal numbers in Python?": {
        "choices": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "b"
    },
    "Q8: Which of the following is a valid variable name?": {
        "choices": ["A. 2value", "B. my-var", "C. my_var", "D. first name"],
        "answer": "c"
    },
    "Q9: Which loop is used when you know the number of iterations?": {
        "choices": ["A. for", "B. while", "C. loop", "D. repeat"],
        "answer": "a"
    },
    "Q10: What will print('Python'[0]) display?": {
        "choices": ["A. Python", "B. P", "C. 0", "D. n"],
        "answer": "b"
    }
}


score = 0

for question, info in quiz.items():
    print("\n" + question)
    for choice in info["choices"]:
        print(choice)
    user_answer = input("Your answer (A/B/C/D): ").lower()
    
    if user_answer == info["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {info['answer'].upper()}")

print(f"\n Your final score: {score}/{len(quiz)}")
if score == 13:
    print("You are a genius")
elif score >= 10:
    print("Good Work!")
elif score >= 7:
    print("you are amazing!")
elif score >= 4:
    print("do practice daily")
else:
    print("don't give up")