'''
def spirits (color):
    color = color.lower()
    match color:
        case 'red':
            return 'Fire'
        case 'blue':
            return 'Water'
        case 'green':
            return 'Wind'
        case 'Yellow':
            return 'Earth'
        case _:
            return 'Wrong Color'

color = input("What's your house color? ")
print (color, 'is', spirits(color))
'''
'''
colors = ['red', 'yellow', 'blue', 'green']
spirits = ['fire', 'earth', 'water', 'wind']

print("Spirits")
print("----------------------------------------")
for count, color in enumerate(colors):
    print(color, 'is', spirits[count])
'''

bruh= int(input("num"))
while bruh != 4:
    bruh= int(input("num"))
    if bruh == 4:
        break