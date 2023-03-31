import random

rule = int(input("Podaj rule: "), 2)
n = int(input("Podaj n: "))
k = int(input("Podaj k: "))

# losowe generowanie ciagu
s = ""
chars = ['_', '*']
for i in range(n):
    s += random.choice(chars)

# ignorujemy uzytkownika...
# mniej-wiecej w srodku...
s = 39 * '_' + '*' + 40 * '_'
n = len(s)

# tworzenie slownika do zastosowania reguly
predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
prerule = ["_" * int(i=='0') + "*" * int(i=='1') for i in str(bin(rule))[2:].zfill(8)]
automat = { key: value for (key, value) in zip(predict, prerule) }

print(s)

for i in range(k):
    # tworzymy nowa generacje s bazujac na slowniku 'automat'
    new_s = ""

    # brzegowy lewy
    new_s += automat["".join([s[-1], s[0], s[1]])]

    # reszta, bierzemy po 3 znaki i zamieniamy je na 1 nowy
    for i in range(1, n - 1):
        new_s += automat[s[i - 1:i + 2]]

    # brzegowy prawy
    new_s += automat["".join([s[-2], s[-1], s[0]])]

    s = new_s
    print(s)
