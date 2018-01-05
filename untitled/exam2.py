n = input("Enter the number of rows in matrix")
m= input("Enter the number of column in matrix")
if n == m:
    #matrix=[[]]
    matrix = [[[] for i in range(3)] for i in range(3)]
    print("Enter the values of the matrix")
    for row in range(0,int(n)):
        for column in range(0,int(m)):
            num = int(input())
            matrix[row][column] = num

    #matrix = [[1, 0, 0], [4, 5, 0], [7, 8, 9]]

    upper=[]
    lower=[]
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            if j > i:
                lower.append(matrix[j][i])
            elif j < i:
                upper.append(matrix[j][i])

    for num in range(0,int(n)):
        if upper[num] ==0:
             print("it is a upper triangel")
        else:
            print("it is not upper triangle")




else:
    print("Enter the square matrix value")
