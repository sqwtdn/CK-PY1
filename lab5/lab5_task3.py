from random import shuffle


def get_unique_list_numbers() -> list[int]:
    spisok = [i for i in range(-10, 11)]
    shuffle(spisok)
    spisok = spisok[:15]
    return spisok


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
