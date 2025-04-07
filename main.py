import random
ball = 0
bosqich = 1
natija = []
while True:
    if bosqich == 1:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
    elif bosqich == 2:
        a = random.randint(9, 19)
        b = random.randint(9, 19)
    amal = ['+', '-', '*', '/']
    tanlangan_amal = random.choice(amal)
    match tanlangan_amal:
        case '+':
            correct = a + b
        case '-':
            correct = a - b
        case '*':
            correct = a * b
        case '/':
            if b == 0 or a % b != 0:
                continue
            correct = a // b
    options = [correct]
    while len(options) < 4:
        x = correct + random.randint(-5, 5)
        if x not in options:
            options.append(x)
    random.shuffle(options)
    letters = ['A', 'B', 'C', 'D']
    variantlar = dict(zip(letters, options))
    print(f"\n{a} {tanlangan_amal} {b} = ?")
    for harf, qiymat in variantlar.items():
        print(f"{harf}) {qiymat}")
    javob = input("Javobingiz (A/B/C/D): ").strip().upper()
    if javob == 'natija':
        print(natija)
    if javob in variantlar and variantlar[javob] == correct:
        ball += 1
        print(f"✅ To'g'ri! Ball: {ball}")
        natija.append(variantlar[javob]) 
        print(natija)
    else:
        ball -= 1
        print(f"Noto'g'ri. To'g'ri javob: {correct}. Ball: {ball}")
        natija.append(variantlar[javob])
        print(natija)
    if ball < 0:
        print("O'yin tugadi!")
        break
    elif ball == 10:
        print('Barakalla! Keyingi bosqichga o\'tdingiz')
        bosqich = 2
