# Программа получает на вход строку – сообщение и
# указание, что нужно сделать: шифровать или дешифровать.
# Реализовать две функции: первая шифрует заданное
# сообщение шифром Цезаря, вторая расшифровывает. В
# зависимости от выбора пользователя (шифровать или
# дешифровать) вызывается соответствующая функция,
# результат выводится в консоль.
message = input("Введите ваше сообщение: ")
action = input("шифровать/расшифровать: ")
alphabet = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя")

def encryption(message):
    key = int(input("шаг: "))
    message.lower()
    message_encrypted = ''
    for letter in message:
        position = alphabet.find(letter)
        new_position = position + key
        if letter in alphabet:
            message_encrypted += alphabet[new_position]
        else:
            message_encrypted += letter

    print(f"зашифрованное сообщение {message_encrypted}")

def decryption(message):
    key = int(input("шаг: "))
    message.lower()
    message_encrypted = ''
    for letter in message:
        position = alphabet.find(letter)
        new_position = position - key
        if letter in alphabet:
            message_encrypted += alphabet[new_position]
        else:
            message_encrypted += letter

    print(f"расшифрованное сообщение {message_encrypted}")

if action == "шифровть":
    encryption(message)
elif action == "расшифровать":
    decryption(message)