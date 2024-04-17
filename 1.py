N = int(input("Введите кол-во слов: " ))
massive=[]

for i in range(N):
    word = input("Введите слово: ")
    massive.append(word)
probel = " ".join(massive)
print("Слова в одной длинной строке: ", probel)