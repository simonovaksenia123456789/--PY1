import random

def get_unique_list_numbers() -> list[int]:

    list_=[]
    while len(list_) < 15:
        n = random.randint(-10,10)
        if n not in list_:
            list_.append(n)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

