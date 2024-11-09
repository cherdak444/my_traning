def calculate_structure_sum(data):
    total = 0
    for element in data:
        if isinstance(element, (list, tuple, dict)):
            if any(isinstance(x, (int, float)) for x in element):
                if isinstance(element, list) or isinstance(element, tuple):
                    total += sum(calculate_structure_sum(x) for x in element)
                else: 
                    for value in element.values():
                        if isinstance(value, (int, float)):
                            total += value
            elif isinstance(element, str):
                total += len(element)
        elif isinstance(element, (int, float)):
            total += element
    return total

data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = calculate_structure_sum(data_structure)
print(result)