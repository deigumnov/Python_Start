from datetime import datetime
from multiprocessing import Process
N_MAX = 300
N_PROC = 12
l = [i ** 5 for i in range(2 * N_MAX)]


def proc(left, right, name: str):
    print(left, right, name)
    for a in range(left, right):
        for b in range(a, N_MAX + 1):
            for c in range(b, N_MAX + 1):
                for d in range(c, N_MAX + 1):
                    tmp = l[a] + l[b] + l[c] + l[d]
                    e = int(tmp ** 0.2 // 1)
                    if l[e] == tmp:
                        print(a, b, c, d, e, a + b + c + d + e)


if __name__ == '__main__':
    start_time = datetime.now()

    procs = [Process(target=proc,
                     args=(1,
                           int(1 * N_MAX // N_PROC),
                           'pr0',))]
    for i in range(1, N_PROC - 1):
        procs.append(Process(target=proc,
                             args=(int(i * N_MAX // N_PROC),
                                   int((i + 1) * N_MAX // N_PROC),
                                   'pr' + str(i),)))
    procs.append(Process(target=proc,
                         args=(int((N_PROC - 1) * N_MAX // N_PROC),
                               N_MAX + 1,
                               'pr' + str(N_PROC - 1),)))
    for process in procs:
        process.start()
    for process in procs:
        process.join()
    end_time = datetime.now()
    print(f'Количество процессов: {N_PROC}')
    print(f'Лимит: {N_MAX}')
    print(f'Время работы: {end_time - start_time}')
