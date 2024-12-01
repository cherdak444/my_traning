# Функция для генерации пар и проверки кратности
def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i+1, 21): 
            if n % (i + j) == 0:
                result += str(i) + str(j)
  
    return result

n = int(input("Введите число от 3 до 20: "))

password = generate_password(n)
print(f"Пароль: {password}")
