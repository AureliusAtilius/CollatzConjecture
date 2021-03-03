
def collatz(number):
    Bruce= True
    while Bruce:
        if number%2==0:
            number=number//2
            print(number)

        else:
            number = (number*3)+1
            print(number)

        if number==1:
            Bruce = False

        else:
            continue



collatz(int(input("Please input a number\n")))