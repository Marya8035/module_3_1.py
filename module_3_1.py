calls = 0

def count_calls():
    global calls
    calls += 1

def string_ifo(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, strings):
    count_calls()
    return string.lower() in map(str.lower, strings)

print(string_ifo('Capybara'))
print(string_ifo('Armageddon'))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN'])) #Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cycling'])) # No matches
print(calls)