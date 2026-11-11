score = 0
print(f"Current user score: {score}")

print("Питання 1: які кольори прапору України?")
print("1. жовтий і блакитний")
print("2. червоний і зелений")
print("3. чорний і жовтий")
print("4. зелений і фіолетовий")

ans = int(input("користувач вводить: "))
if ans == 1:
    print("Correct answer!")
    score = score + 100
    print(f"Current user score: {score}")


print("Питання 2: в якому місті знаходиться ДТЕУ?")
print("1. Вінниця")
print("2. Київ")
print("3. Львів")
print("4. Одеса")

ans = int(input("користувач вводить: "))
if ans == 2:
    print("Correct answer!")
    score = score + 100
    print(f"Current user score: {score}")
if ans == 1:
    print("Wrong answer!")
    print("You lost")