word = 'Python'

# ο πρώτος χαρακτήρας
print(word[0])

# ο δεύτερος χαρακτήρας
print(word[1])

print(word[2])
print(word[3])
print(word[5])

len(word)   # 6 μήκος, πλήθος χαρακτήρων
print(word[len(word) - 1])

word = 'Python'
print(word[0])   # P
print(word[-1])  #n

print(word[1:4])
# 'yth'
print(word[1:])
# 'ython'
print(word[:4])

word = "Python"

for letter in word:
    print(2 * letter, end="")

# PPyytthhoonn
# 'Pyth'
print(word[::2])
# 'Pto'
print(word[::-1])
# 'nohtyP'

# ένωση
greeting = 'Hello ' + 'there'
print(greeting)
# 'Hello there'

print('a' * 10)
# 'aaaaaaaaaa'

print('y' in 'Python')
# True
print('f' in 'Monty')
# False

print("Γειά σου {}! Με λένε {}".format('Γιώργο', 'Διονύση'))
# 'Γειά σου Γιώργο! Με λένε Διονύση'

print("Γειά σου {1}! Με λένε {0}".format('Γιώργο', 'Διονύση'))
# 'Γειά σου Διονύση! Με λένε Γιώργο'

'Monty-Python'.split('-')  # ['Monty', 'Python']

'hello world'.replace('hello', 'goodbye')  # 'goodbye world'

'hello world'.count('l')   # 3

'Python'.startswith('P')   # True

'python'.upper()           # 'PYTHON'
'PYTHON'.lower()           # 'python'