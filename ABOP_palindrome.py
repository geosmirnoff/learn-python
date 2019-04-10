def reverse(text):
    return text[::-1]

def is_palindrome(text):
    forbidden = (',', '.', ':', ';', '!', '?', '\\', '|', '/', '(', ')', '-', ' ', '_')
    return text == reverse(text)

something = input('Введите текст: ')
if (is_palindrome(something)):
    print('Палиндром')
else:
    print('Не палиндром')
