def print_multiples_of_7(num):
    
    for i in range(1, num+1):
        if i%2 == 0:
            print(f"\t{7*i}")
        else:
            print(7*i)
            
print_multiples_of_7(5)            