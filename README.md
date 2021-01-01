# Jupiter_Assignment
For above assigment I am providing two solution written in python, one without use of any inbuilt library and another with scipy library.


## General Instructions to run the solution
- Clone the repository in your local machine
- Install the scipy library required for solution2 open terminal and type fallowing command
```bash
pip install scipy
```


### Instructions to run solution1
- Navigate to solution1 directory
```bash
cd ./Jupiter_Assignment/solution1
```
- To run the solution1 type fallowing command in terminal
```bash
python main.py
```
#### Output of solution1 
```
PS C:\Users\Pattinson\python_projects\res_allocation> python main.py
Enter the profit associated with individual product(order p1 p2 p3 p4):20 12 40 25
Enter the cpu usage of individual products(p1 p2 p3 p4):3 2 1 0
Enter the gpu usage of individual products(p1 p2 p3 p4):0 1 2 3
Enter total number cpu available in data center:100
Maximum profit would be 1900 for p1 = 5, p2 = 0, p3 = 45, p4 = 0

```
### Instructions to run solution2
-Navigate to solution2 directory
```bash
cd ./Jupiter_Assignment/solution2
```
- To run the solution1 type fallowing command in terminal
```bash
python res_scipy.py
```
#### Output of solution2
```
Output of print(opt) will be:
    con: array([], dtype=float64)
    fun: -1900.0 -> this max profit value for [p1 =5 , p2 = 0 , p3 = 45, p4 = 0]
    message: 'Optimization terminated successfully.'
    nit: 2
    slack: array([ 0., 40.,  0.])
    status: 0
    success: True
    x: array([ 5.,  0., 45.,  0.]) -> this array is value of product for maximum profit
    [p1 = 5 , p2 = 0, p3 = 45, p4 = 0]

```

## Project Status
- We can solve the given problem more efficiently by using mathematical approach but due short time I am unable to implemented the solution.
