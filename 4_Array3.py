####
##
##
## Array3.py

def main():
    sides = 6


    a = [0] * (sides + 1)
    
    print("The numbers are ")
    for i in range(0, sides + 1):
        a[i] = i
        print(a[i], end = " ")

    print("\r")


main()