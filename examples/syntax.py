# integers
one = 1
two = 2
some_number = 10000

# booleans
true_boolean = True
false_boolean = False

# string
my_name = "Dennis"
greek_name = "Διονύσης"

# float
book_price = 15.80

# int
type(some_number)
# bool
type(true_boolean)
# str
type(my_name)
# float
type(book_price)

# πολλαπλή εκχώρηση
name, age = "Γιώργος", 13

# εκτύπωση μεταβλητών
print(name)
print(age)

print('γειά σου', name)

# αυτό είναι ένα σχόλιο

# είσοδος από τη γραμμή εντολών
name = input("Όνομα; ")

# εκτύπωση στη γραμμή εντολών
print("Καλημέρα", name)

# μετατροπή τύπου
x = '2'
x = int(2)
type(x)  # int

num = input("Χ: ")
num ** 2   # throws error
num = int(num)
num ** 2   # correct