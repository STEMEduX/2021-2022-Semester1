##
## array.py
  
import array

def main():
    
    myList = [1, 5, 6, 3, 7, 98]

    arr = array.array('i', myList)

    for i in range(0, 6):
        print(arr[i], end = " ")


    print("\r")

    arr.append(100)

    for i in range(0, 7):
        print(arr[i], end = " ")


    print("\r")    

    for j in range (50, 101):
        arr.append(j * j)

    for i in range(0, 58):
        print(arr[i], end = " ")

    print("\r")
    
    sum = 0

    for i in range(0, 58):
        sum = sum + arr[i]

    print(sum, end = " ")


    print("\r")




main()