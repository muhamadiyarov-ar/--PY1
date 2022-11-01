def get_count_char(str_):
    abc_dict = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()

    for sign in str_:
        if sign.isalpha():
            if sign in abc_dict:
                abc_dict[sign] += 1
            else:
                abc_dict[sign] = 1

    return abc_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

abc_dict = get_count_char(main_str)

def get_symbols(abc_dict):
    total_count = sum(abc_dict.values())
    new_dict = {}
    for count in abc_dict:
        new_dict[count] = abc_dict[count]/total_count * 100
    return new_dict

result = get_symbols(abc_dict)
print(result)
