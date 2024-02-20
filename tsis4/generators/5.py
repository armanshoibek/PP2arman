def all_numbers ( n ) :
    for i in range ( n, -1, -1 ) :
        yield i
        
n = 10 

all_num = all_numbers ( n )

for numbers in all_num :
    print ( numbers )
    