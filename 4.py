import random

correct = 0
wrong = 0

while wrong < 3:
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    correctotvet = num1 + num2

    user_answer = input(f"{num1} + {num2} = ")

    if int(user_answer) == correctotvet:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        wrong += 1

print(f"Игра окончена. Правильных ответов: {correct}")