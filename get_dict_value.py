ages = {
    'Maria': 33,
    'Iva': 19
}

# bad way
if 'Iva' in ages:
    age = ages['Iva']
else:
    age = 'Unknown'
print('Iva is %s years old!' % age)

# good way
age = ages.get('Iva', 'Unknown')
print('Iva is %s years old!' % age)
