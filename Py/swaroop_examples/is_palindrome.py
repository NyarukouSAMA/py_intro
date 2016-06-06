def reverse(text):
    return text[::-1]
def is_palindrome(text):
    forbidden = ('!', ' ', ',', '.', '?')
    text = text.lower()
    textFormated = ''
    for sign in text:
        if sign not in forbidden:
            textFormated += sign
    text = textFormated
    del(textFormated)
    return text == reverse(text)

something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")