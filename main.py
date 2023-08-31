import argparse
import multiprocessing
import numpy as np
import time

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="number of processes", type=int, choices=range(1, multiprocessing.cpu_count()))
parser.add_argument("--quiet", help="suppress index output", action="store_true")
args = parser.parse_args()

NUMBER_OF_TASKS = args.n or 1


def my_function(pool_index):
    if not args.quiet:
        print(f"I am {pool_index}")
    dim_size = 1000
    my_nums = np.zeros((dim_size, dim_size))

    for i in range(dim_size):
        for j in range(dim_size):
            my_nums[i, j] += np.random.rand()
    return np.sum(my_nums)


def main():
    pool_index = range(16)
    t = time.time()
    p = multiprocessing.Pool(NUMBER_OF_TASKS)
    p.map(my_function, pool_index)
    print(f"{NUMBER_OF_TASKS}: {time.time() - t}")


if __name__ == "__main__":
    main()
