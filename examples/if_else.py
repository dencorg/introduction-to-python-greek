max = 10
x = 50

if x > max:
    print('μεγαλύτερο')
else:
    print('μικρότερο')

if x > max:
    max = x

y = 0
if x > y:
    y = y + 10
else:
    x = x - 10

# είσοδος από χρήστη και μετατροπή σε σωστό τύπο
answer = int(input('What is the product of 2*5'))

if answer == 10:
    print('Correct!')

print('Exiting program')

my_name = 'dennis'

your_name = input('Καλημέρα! Ποιό είναι το όνομά σου;')

if (συνθήκη εδώ):
    print('Και μένα!')
else:
    print('Χάρηκα για τη γνωριμία!')

x = int(input('Διάλεξε αριθμό: '))

if x < 0:
    print('Μετατροπή σε θετικό αριθμό...');
    x = -x
elif x == 0:
    print('Μηδεν')
elif x == 1:
    print('Ενα')
else:
    print('Μεγαλύτερος του 1')