print('=' * 30)
print('WEIGHT CONVERTER'.center(30))
print('=' * 30)
def lbs_kg():
    libs = float(input('Insert the weight in pounds: '))
    kilos = libs * 0.453592
    print(f'{libs} lbs weights {kilos} Kg.')
def kg_lbs():
    kilos = float(input('Insert the weight in kilos: '))
    libs = kilos * 2.20462
    print(f'{kilos} Kg weights {libs} lbs')
def leave():
    cont = str(input('Do you want to convert anything else? [Y/N] ')).strip().upper()[0]
    while cont not in 'yYnN':
        cont = str(input('Invalid choice. Do you want to convert anything else? [Y/N] ')).strip().upper()[0]
    if cont in 'nN':
        quit()
while True:
    choice = str(input('Do you want to convert Pounds(lbs) or Kilos(kg)? ')).strip().upper()[0]
    while choice not in 'pPlLkK':
        choice = str(input('Invalid choice. Do you want to convert Pounds(lbs) or Kilos(kg)? ')).strip().upper()[0]
    if choice in 'pPlL':
        lbs_kg()
    elif choice in 'kK':
        kg_lbs()
    leave()
    