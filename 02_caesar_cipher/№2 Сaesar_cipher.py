def caesar(text, shift):
    result = ''
    for i in text:
        if i.isalpha():
            if i.isupper():     
                a = chr( (ord(i) - ord('A') + shift) % 26 + ord('A') )
            else:
                a = chr( (ord(i) - ord('a') + shift) % 26 + ord('a') )
            result += a
        else:
            result += i
    return result
user_input = input("Введи слова: ")
shift = int(input("веди сколько сдвигов: "))
print(caesar(user_input, shift))

