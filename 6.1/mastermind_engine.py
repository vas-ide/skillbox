from random import random, randint

from termcolor import colored


def generate_number():
    generate_number_list = []
    generate_number_set = set()
    generate_number_str = ''
    while len(generate_number_list) < 4:
        num = randint(0, 9)
        if num < 10:
            generate_number_list.append(num)
            generate_number_set.add(num)
            generate_number_str += str(num)
        if int(generate_number_list[0]) == 0:
            generate_number_list = []
            generate_number_set = set()
            generate_number_str = ''
        if len(generate_number_list) > len(generate_number_set):
            generate_number_list = []
            generate_number_set = set()
            generate_number_str = ''
    return generate_number_str


def check_a_generated_number(input_number=1234, generate_number=1234):
    input_number = str(input_number)
    generate_number = str(generate_number)
    generate_number_dict = {}
    input_number_dict = {}
    cows_num = 0
    bulls_num = 0
    livestock = {'bulls': 0, 'cows': 0}
    for num, value in enumerate(generate_number):
        generate_number_dict[num] = value
    for num, value in enumerate(input_number):
        input_number_dict[num] = value
    for key in range(len(generate_number)):
        if generate_number_dict[key] == input_number_dict[key]:
            bulls_num += 1
    livestock['bulls'] = bulls_num
    for i in generate_number:
        for j in input_number:
            if i == j:
                cows_num += 1
    livestock['cows'] = cows_num - bulls_num
    return print(colored(f'Быки - {livestock["bulls"]}  Коровы - {livestock["cows"]}', color='cyan'))
