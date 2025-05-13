# Juego de preguntas y respuestas


questions = (
    "1. What is the longest river in the world?",
    "2. Who painted the Sistine Chapel?",
    "3. In which year did humans first land on the Moon?",
    "4. Which country has the most native Spanish speakers?",
    "5. What chemical element has the symbol 'Au'?"
)

options = (
    ("A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"),
    ("A. Leonardo da Vinci", "B. Raphael", "C. Michelangelo", "D. Donatello"),
    ("A. 1965", "B. 1969", "C. 1972", "D. 1959"),
    ("A. Spain", "B. Argentina", "C. Mexico", "D. Colombia"),
    ("A. Silver", "B. Gold", "C. Aluminum", "D. Uranium")
)

answers = ("B", "C", "B", "C", "B")
guesses = []
score = 0
question_number = 0


for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_number]:
        print(option, end=" ")
    guesses.append(input("\nChoose your answer (A, B, C or D): ").upper())
    if guesses[question_number] == answers[question_number]:
        print("Correct!!")
        score += 1
    else:
        print(f"Incorrect! the correct answer is {answers[question_number]}")
    question_number += 1

print("................")
print("     RESULT     ")
print("................")

print("Correct answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print("\nYour answers:    ", end=" ")
for guess in guesses:
    print(guess, end=" ")

score = int(score / len(questions) * 100)
print(f"\nYour total score is {score}%")



