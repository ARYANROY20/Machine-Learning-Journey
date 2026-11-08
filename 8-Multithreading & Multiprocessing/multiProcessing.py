import multiprocessing
import time

def square_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube:{i}")

if __name__=="__main__":
    #Create two processes
    p1=multiprocessing.Process(target=square_num)
    p2=multiprocessing.Process(target=cube_number)

    t=time.time()

    #Start two proceses
    p1.start()
    p2.start()

    #Wait for the process
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)