first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(el) for el in first_strings if len(el) >= 5]
print(first_result)

second_result = [(el1, el2) for el1 in first_strings for el2 in second_strings if len(el1) == len(el2)]
print(second_result)

third_result = {el: len(el) for el in first_strings + second_strings if not len(el) % 2}
print(third_result)
