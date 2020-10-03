#FIZZ BUZZ

for n in range(1,101):
    print_out = ""
    if n % 3 == 0:
        print_out = print_out + "Fizz"
    if n % 5 == 0:
        print_out = print_out + "Buzz"
    if n % 5 != 0 and n % 3 != 0:
        print_out = print_out + str(n)
    print(print_out)
