# matt's scripts

Dead = '{} {} {} {}'
print(Dead.format( "1", '2', '3', '4'))
print(Dead.format('one','two', 'three', 'four'))
print(Dead.format(
    "Walk me out in the morning dew my honey...",
    "Walk me out in the morning dew today",
    "I can't walk you out in the morning dew my honey...",
    "Beat it on down the line!"
))

object = '{} {}'
print(object.format('1' , '2'))
print("Will it work?")

x = 250.000
y = 50.00   
h = 0
print('I owe tcf', x)
print('Once a month i can pay', y)
print('It will take me', x / y, 'months to pay tcf off')
print('Just think about it x - y = ', x - y )
print('5 months later it will all be paid off i will owe', h)