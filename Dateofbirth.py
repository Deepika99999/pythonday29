birthdays = {'Albert': 'July 17 1706', 'Roger': 'Jan 27 1803', 'Adana': 'July 10 1998'}

while True:
    print("welcome we have birthdates of:",
          'Albert',
          'Roger',
          'Adan')
    print("Who's birthday is it that you are looking for? To cancel, press enter!")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
          print(birthdays)
       
