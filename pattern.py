def pattern(n=2):
    # num = input("Please enter a number greater than or equal to 2\n")
    num = n
    # if num.isnumeric() and int(num)>=2:
    if num >= 2:
        for i in range(1,int(num)+1):
            for j in range(1,i+1):
                # print(f"j is {j}")
                print(j,end=",")
            print("")
        for k in range(1,n):
            # print(f'n is {n}')
            print(k, end=',')
            for l in range(n-k, 1,-1):
                print(l,end=',')
                # n = n - 1
                # print(f'num is {num}')
                # k = k-1
            print("")

print(pattern(8))
