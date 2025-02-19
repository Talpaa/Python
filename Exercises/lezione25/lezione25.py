from multiprocessing import Process
import time

def bubble_sort_v2():
    
    from random import randint

    x = [randint(0, 10000) for i in range(50000)]

    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break

def sleep():

    print(f'Sono nella funzione')

    time.sleep(60)

    print(f'Sto uscendo dalla funzione')


if __name__ == "__main__":

    tic: float = time.time()

    t1 = Process(target=bubble_sort_v2)
    t2 = Process(target=bubble_sort_v2)
    t3 = Process(target=bubble_sort_v2)
    t4 = Process(target=bubble_sort_v2)
    t5 = Process(target=bubble_sort_v2)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    #time.sleep(45)
    toc: float = time.time()
    time_elapsed: float = toc - tic

    print(f'{time_elapsed=}')