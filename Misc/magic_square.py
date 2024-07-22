# The Magic Square is a grid with 3 rows and 3 columns with the following properties:
# • The grid contains every number from 1 to 9.
# • The sum of each row, each column, and each diagonal all add up to the same number.

# This is an example of a Magic Square:
# 4 9 2
# 3 5 7
# 8 1 6

# You can simulate a 3x3 grid using a two-dimensional list. For example, the list
# corresponding to the grid above would be: [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

# Write a function that accepts a two-dimensional list as an argument and
# returns whether the list represents a Magic Square (either True or False).

# Create a program that tests the function on the following two-dimensional lists and prints out the results each on a separate line:

# [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[4, 9, 2], [3, 5, 5], [8, 1, 6]] 

def ms(a):
    b=len(a)
    c=[] 
    d1=0 
    d2=0 
    
    for i in range(0,b-1): 
        
        if(sum(a[i])!=sum(a[i+1]) and sum(a[i])<=27 and sum(a[i+1])<27):
            return False 
    for i in range(0,b): 
        for j in range(0,b):
            if(i==0):
                c.append(0)
            c[j]+=a[j][i]
            if(i==j): 
                d1+=a[i][j]
    
    for i in range(0,b-1): 
        if(c[i]!=c[i+1]):
            return False
    for i in range(b-1,-1,-1): 
        for j in range(b-1,-1,-1):
            if(i==j):
                d2+=a[i][j]
                
    if(d1!=d2): 
        return False
    if(sum(a[0])==c[0]==d1==d2): 
        return True
    
print(ms([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print(ms([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(ms([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(ms([[4, 9, 2], [3, 5, 5], [8, 1, 6]]))