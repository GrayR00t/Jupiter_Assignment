from cpu import t_cpu
from gpu import t_gpu 
from check import is_valid
from profit import t_profit


profit_of_prod = input("Enter the profit associated with individual product(order p1 p2 p3 p4):")
profit_of_prod = profit_of_prod.split()
for i in range(0, len(profit_of_prod)):
    profit_of_prod[i]= int(profit_of_prod[i])


print(profit_of_prod)

cpu_usage = input("Enter the cpu usage of individual products(p1 p2 p3 p4):")
cpu_usage = cpu_usage.split()
for i in range(0, len(cpu_usage)):
    cpu_usage[i]= int(cpu_usage[i])

print(cpu_usage)

gpu_usage = input("Enter the gpu usage of individual products(p1 p2 p3 p4):")
gpu_usage = gpu_usage.split()
for i in range(0, len(gpu_usage)):
    gpu_usage[i]= int(gpu_usage[i])

print(gpu_usage)
allowed_cpu = int(input("Enter total number cpu available in data center:"))
allowed_gpu = int(input("Enter total number gpu available in data center:"))

print(allowed_cpu)
print(allowed_gpu)

t_customer = int(input("Enter the available customer:"))

print(t_customer)

total_max_profit = 0
cust_p1 = 0
cust_p2 = 0
cust_p3 = 0
cust_p4 = 0
for i in range(0, t_customer+1):
    for j in range(0, t_customer + 1):
        for k in range(0,t_customer+1):
            total_sum = i+j+k
            n_p4 = t_customer - total_sum
            if(n_p4 < 0):
                continue
            total_gpu = t_gpu(gpu_usage[0],gpu_usage[1],gpu_usage[2],gpu_usage[3] , i , j , k, n_p4)
            total_cpu = t_cpu(cpu_usage[0], cpu_usage[1], cpu_usage[2], cpu_usage[3], i ,j ,k ,n_p4)
            if(is_valid(total_cpu,total_gpu,allowed_cpu,allowed_gpu)):
                total_profit = t_profit(profit_of_prod[0], profit_of_prod[1], profit_of_prod[2], profit_of_prod[3], i ,j ,k ,n_p4)
                if(total_max_profit < total_profit):
                    total_max_profit = total_profit
                    cust_p1 = i
                    cust_p2 = j
                    cust_p3 = k
                    cust_p4 = n_p4



print(total_max_profit)
print(cust_p1)
print(cust_p2)
print(cust_p3)
print(cust_p4)