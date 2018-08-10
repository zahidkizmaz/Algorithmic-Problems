import multiprocessing as mp 

def spawn(num):
    print('Spawned {}'.format(num))


if __name__ == '__main__':
    for i in range(55):
        p = mp.Process(target=spawn, args=(i,))
        p.start()
        p.join()
        