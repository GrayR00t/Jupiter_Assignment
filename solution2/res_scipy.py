'''
Using scipy libraby available in python we can solve this problem.

The mathematical model for given problem can be defined like this:
    Given profit for each product:
        1. p1 = 20
        2. p2 = 12
        3. p3 = 40
        4. p4 = 25
    Total number of customer can be served = 50
    Constraints given on cpu and gpu for each product:
        1. p1 = 3cpu + 0gpu
        2. p2 = 2cpu + 1gpu
        3. p3 = 1cpu + 2gpu
        4. p4 = 0cpu + 3gpu

    Total number of cpu available = 100
    Total number of gpu available = 90

    Mathematical equation:
        profit = 20*p1 + 12*p2 + 40*p3 + 25*p4 ( we have to maximize profit under above given contraint) 
        p1 + p2 + p3 + p4 <= 50
        3*p1 + 2*p2 + p3 <= 100
        p2 + 2*p3 + 3*p4 <= 90
        p1, p2, p3, p4 >=0


    As in scipy we can't maximize the profit so we transform our equation by multiply -1 both side:
        -1*(profit) = -1*(20*p1 + 12*p2 + 40*p3 + 25*p4)
        -profit = -20*p1 - 12*p2 - 40*p3 - 25*p4


'''

#importing linprogramming from scipy library
from scipy.optimize import linprog

#make  obj list with value of profit associated with each product

obj = [-20, -12, -40, -25]

#make lsh list of list with cofficient of fallowing equation
#        p1 + p2 + p3 + p4 <= 50
#        3*p1 + 2*p2 + p3 <= 100
#        p2 + 2*p3 + 3*p4 <= 90

lhs = [[1,1,1,1],
       [3,2,1,0],
       [0,1,2,3]]


#make rhs list of values havin right hand side values in fallowing equation    
#        p1 + p2 + p3 + p4 <= 50
#        3*p1 + 2*p2 + p3 <= 100
#        p2 + 2*p3 + 3*p4 <= 90

rhs = [50, 100, 90]

#as product can't be negative so we have to put bound on product value should be grater than zero

bnd =[(0,float("inf")),(0,float("inf")),(0,float("inf")),(0,float("inf"))]

#calling linprog function

opt = linprog(c=obj,A_ub = lhs , b_ub = rhs, bounds=bnd,method="revised simplex")

print(opt)

'''
Output of print(opt) will be:
    con: array([], dtype=float64)
    fun: -1900.0
    message: 'Optimization terminated successfully.'
    nit: 2
    slack: array([ 0., 40.,  0.])
    status: 0
    success: True
    x: array([ 5.,  0., 45.,  0.]) -> this array is value of product for maximum profit
    [p1 = 5 , p2 = 0, p3 = 45, p4 = 0]

'''    


