#!/usr/bin/python3
print('Hello World')
#defining my own function without arguments
def song():
    print('Hello Hello, can you hear my name')
    print('They call me crazy')
song()
print('thank you')
#defining a function with arguments
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
#now we call the function with argumens
greet('es')
greet('fr')
greet('hi')
