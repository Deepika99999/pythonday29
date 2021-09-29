name = input('Enter your name: ')
age = input('Enter your age: ')

year = 2018 - int(age) + 100
message = name + ' will be 100 years old in ' + str(year) + '\n'
print(message)

num = input('Enter a number: ')
message = message * int(num)

print(message)