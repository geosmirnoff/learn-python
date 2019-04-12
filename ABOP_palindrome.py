def reverse(text):
    return text[::-1]

def del_chars(text):
    forbidden = (',', '.', ':', ';', '!', '?', '\\', '|', '/', '(', ')', '-', ' ', '_', '*', '"', '+', '=', '[', ']', '{', '}', '<', '>', '`', '~', '%', '$', '@', '^', '&')
    text = text.lower()
    for char in forbidden:
        if char in text:
            text = text.replace(char, '')
    return text
            
def is_palindrome(text):
    text = del_chars(text)
    return text == reverse(text)

something = input('Введите текст: ')

if (is_palindrome(something)):
    print('Палиндром')
else:
    print('Не палиндром')
