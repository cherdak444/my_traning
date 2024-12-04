def calculate_structure_sum(data_structure):
    total_sum = 0
    
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item)
    
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            if isinstance(key, (int, float)):
                total_sum += key
            elif isinstance(key, str):
                total_sum += len(key)
            if isinstance(value, (int, float)):
                total_sum += value
            elif isinstance(value, str):
                total_sum += len(value)
            total_sum += calculate_structure_sum(value)
    
    elif isinstance(data_structure, (int, float)):
        total_sum += data_structure
    
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
