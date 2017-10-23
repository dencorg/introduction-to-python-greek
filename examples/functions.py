def add(a, b):
    c = a + b

    return c

print(add(2, 3))

def find_min(a,b):
    if a < b:
        return a
    else:
        return b

print(find_min(3,4))

# προεπιλεγμένα ορίσματα

def hello(message='Hello world!'):
    print(message)

hello()
hello('Hello there!')

def greetings(greet="hello", name="there"):
    print(greet + ' ' + name)

greetings()
greetings(name='dennis', greet='bye')