def get_count_char(str_):
    str_ = str_.lower().split(' ')
    while ('', '\n') in str_:
        str_.remove('', '\n')
    # str_ = sorted(str_)
    str_ = ''.join(str_)
    dict = {}
    for i in str_:
        if i.isalpha():
            c = str_.count(i)
            if i not in dict:
                dict[i] = c
    return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
