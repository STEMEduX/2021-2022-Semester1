##
## array.py

import array
  
def main():
    arr = array.array('i', [1, 4, 4, 6, 9])

    for i in range (0, 5):
        print (arr[i], end = " ")

    print ("\r")

    arr[2] = 50

    for i in range (0, 5):
        print (arr[i], end = " ")

    print ("\r")

main()