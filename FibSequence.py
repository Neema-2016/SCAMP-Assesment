terms = int(input("Input number of terms\n"))
def fibb_seq(n):
    if n <= 1:
        return n

    else:
        return(fibb_seq(n-1) + fibb_seq(n-2)

#Checking validity of terms
if terms <= 0:
    print("Enter positive integer to continue!")

else:
    print("The Fibonaccci Sequence is: ")
    for i in range(terms):
        print(fibb_seq(i))
