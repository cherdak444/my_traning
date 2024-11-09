calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    length = len(string)
    uppercase_string = string.upper()
    lowercase_string = string.lower()
    return (length, uppercase_string, lowercase_string)

def is_contains(string, list_to_search):
    global calls
    if string.lower() in [s.lower() for s in list_to_search]:
        count_calls()
        return True
    else:
        count_calls()
        return False

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)