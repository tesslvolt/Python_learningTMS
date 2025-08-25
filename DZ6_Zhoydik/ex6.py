#  См. предыдущую задачу, но вместо шифра Цезаря
# использовать шифр Виженера.
message = input("Введите ваше сообщение: ").strip().lower()
action = input("шифровать/расшифровать: ").strip().lower() # стрип и ловер подсказал гпт, потому что при корректном вводе
                                                           # ничего не выводмло
alphabet = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя")

def encryption1(message):
    keyword = input("ключевое слово: ").strip().lower()
    message = message.lower()
    message_encrypted = ''
    i = 0
    for letter in message:
        position_m = alphabet.find(letter)
        position_k = alphabet.find(keyword[i % len(keyword)])
        sum = position_m + position_k
        if sum > 34:
            sum = abs(position_k - position_m)
        if letter in alphabet:
            message_encrypted += alphabet[sum]
        else:
            message_encrypted += letter
        i += 1
    print(f"зашифрованное сообщение {message_encrypted}")


def decryption2(message):
    keyword = input("ключевое слово: ").strip().lower()
    message = message.lower()
    message_decrypted = ''
    i = 0
    for letter in message:
        position_m = alphabet.find(letter)
        position_k = alphabet.find(keyword[i % len(keyword)]) # подсказал гпт
        sum = position_m - position_k
        if sum > 34:
            sum = abs(position_k + position_m)
        if letter in alphabet:
            message_decrypted += alphabet[sum]
        else:
            message_decrypted += letter
        i += 1
    print(f"расшифрованное сообщение {message_decrypted}")


if action == "шифровать":
    encryption1(message)
elif action == "расшифровать":
    decryption2(message)
