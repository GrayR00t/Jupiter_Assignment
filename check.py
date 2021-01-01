

def is_valid(t_cpu, t_gpu, all_cpu, all_gpu):
    if(t_cpu <= all_cpu and t_gpu <= all_gpu):
        return True
    else:
        return False    