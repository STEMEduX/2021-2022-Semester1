##
## cal1.py
# sum = 1 + 2 + 3 + ....... + 98 + 99 + 100
def main():
    sum = 0
    count = 1 # initialize variable count with value 1
    roll = True

    while roll:
        sum = sum + count
        count = count + 1

        if count > 100:
            roll = False;


    print("Sum: ", sum)

main()