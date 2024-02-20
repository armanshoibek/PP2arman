def even_numbers_generator ( n ):
    for i in range ( 0, n + 1 ) :
        if i % 2 == 0:
            yield i

n = 16

even_numbers = even_numbers_generator ( n )

for number in even_numbers:
    print( number, end = ", " )


