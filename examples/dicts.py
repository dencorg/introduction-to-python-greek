prices = { 'milk': 3.67, 'bread': 1.67, 'cheese': 4.67 }
print(prices)

print(prices['milk'])

# προσθήκη ζεύγους κλειδιού τιμής
prices['butter'] = 1.95

# διαγραφή στοιχείου                        
del prices['butter']

for food in prices:
    print('{} costs {}'.format(food, prices[food]))

# bread costs 1.67
# cheese costs 4.67
# milk costs 3.67

for k, v in prices.items():
    print(k, v)

# bread 1.67
# cheese 4.67
# milk 3.67

len(prices)    # 3

prices.keys()
list(prices.keys())    # ['bread', 'cheese', 'milk']

prices.values()
list(prices.values())    # [1.67, 4.67, 3.67]

'milk' in prices      # True
'beer' in prices      # False

if 'milk' in prices:
    print('milk costs', prices['milk'])
    
# sets
basket = {'apple', 'orange', 'apple', 'orange', 'banana'}
print(basket)
# {'banana', 'orange', 'apple'}

'orange' in basket    # True
'pear' in basket      # False

for fruit in basket:
    print(fruit, end=' ')