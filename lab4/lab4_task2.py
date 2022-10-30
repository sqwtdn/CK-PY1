def get_count_char(str_):
    dict_ = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for l in str_:
        if l.isalpha():
            if l in dict_:
                dict_[l] += 1
            else:
                dict_[l] = 1
    return dict_

def count_pr(str_):
    dict_ = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for l in str_:
        if l.isalpha():
            if l in dict_:
                dict_[l] += 1
            else:
                dict_[l] = 1
    len_ = sum(dict_.values())
    for name, val in dict_.items():
        dict_[name] = round((val / len_) * 100, 1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(count_pr(main_str))
