def three_four_numbers_generator ( n ):
    for i in range ( n + 1 ) :
        if i % 3 == 0 and i % 4 == 0 :
            yield i

n = 16

three_four_numbers = three_four_numbers_generator ( n )

for number in three_four_numbers:
    print ( number )
    

