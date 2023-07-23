# importing the module
import tracemalloc
import time

def time_mem(func_mntr):

    def wrapper(*args, **kwargs):
        # starting the monitoring
        tracemalloc.start()
        start_time = time.time()

        result = func_mntr(*args, **kwargs)

        end_time = time.time()
        # displaying the memory
        mu = tracemalloc.get_traced_memory()
        # print("base_memory: ",(mu[0]),"bytes, ",(mu[0])/1024,"KiB")
        print("peek_memory: ",(mu[1])/1024,"KiB",end=" - ")
        # stopping the library
        tracemalloc.stop()
        print(f"Execution time: {end_time - start_time} seconds")

        return result
    
    return wrapper



def time_mem_data(func_mntr):

    def wrapper(*args, **kwargs):
        # starting the monitoring
        tracemalloc.start()
        start_time = time.time()

        result = func_mntr(*args, **kwargs)

        end_time = time.time()
        # displaying the memory
        mu = tracemalloc.get_traced_memory()
        # print("base_memory: ",(mu[0]),"bytes, ",(mu[0])/1024,"KiB")
        print("peek_memory: ",(mu[1])/1024,"KiB",end=" - ")
        # stopping the library
        tracemalloc.stop()
        print(f"Execution time: {end_time - start_time} seconds")

        return [result,(mu[1])/1024,(end_time - start_time)]
    
    return wrapper





 
 