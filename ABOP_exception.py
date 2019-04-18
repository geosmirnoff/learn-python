try:
    text = input('Введите текст')
except EOFError:
    print('ВНЕЗАПНЫЙ КОНЕЦ ФАЙЛА')
except KeyboardInterrupt:
    print('Вы отменили операцию')
else:
    print('Вы ввели {0}'.format(text))
