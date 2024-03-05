[1]list = [ 1, 2, 7, 5, 21, 34, 0, 0, 2, 7, 4, 1, 1, 1 ]

summa = sum ( list )

print ( f"Sum of all numbers in this one list equals to = {summa}")

[2]
simple_string = input ( "Введите строку: " )

uppercase_count = sum ( 1 for char in simple_string if char.isupper() )
lowercase_count = sum ( 1 for char in simple_string if char.islower() )

print ( "Количество строчных букв = ", lowercase_count )
print ( "Количество заглавных букв = ", uppercase_count )


[3]
def is_palindrom_or_not ( stroka ) :
    stroka = "".join ( char for char in stroka.lower() if stroka.isalnum() )
    return stroka == stroka[::-1]

our_input = input ( "Введите строку для проверки: ")

if is_palindrom_or_not ( our_input ) :
    print ( "Да, строка является палиндромом")
else :
    print ( "Не, не палиндром")

[4]
import time
import math

def geemesquare () :
    number = int ( input ( "Введите число: ") )
    msec = int ( input ( "Введите кол-во миллисекунд: " ) )
    
    time.sleep ( msec / 1000 )
    result = math.sqrt ( number )
    print ( f"Квадратный корень из {number} после {msec} миллисекунд, будет = {result}")
    
geemesquare ()



[5]
my_tuple = ( True, True, 5, True )

if all ( my_tuple ) :
    print ( "Все элементы tuple истинны." )
else:
    print( "Не все элементы tuple истинны." )
    