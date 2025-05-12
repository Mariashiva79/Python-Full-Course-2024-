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
    print("-----------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Choose your answer (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was {answers[question_number]}")
    question_number += 1

print("--------------------")
print("        RESULT      ")
print("--------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"The score is {score}%")




