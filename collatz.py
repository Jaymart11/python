def collatz(number):
    if number == 1:
        return
    
    if(number % 2 == 0): 
        d_num = number // 2
    else:
        d_num = 3 * number + 1

    print(d_num)

    return collatz(d_num)


numberInput  =  collatz(int(input("Enter a integer: ")))
