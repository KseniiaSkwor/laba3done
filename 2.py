massive = []

while True:
    word = input("Введите слово (если хотите закончить введите 'stop') : ")
    if word == "stop":
        break
    massive.append(word)

probel = " ".join(massive)
print("Слова в одной длинной строке: ", probel)