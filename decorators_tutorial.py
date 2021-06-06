# decorators: decorator is a design pattern in python that
# allows you to extend or modify the behavior of a callable
# e.g. function, method, class without permanently changing
# the callable itself

# the decorator gives us lots of flexibility
# and decouples the functionality methods and main methods

from time import time, sleep
import numpy as np
import pandas as pd
import random
import sys
import pdb


def get_dataframe_memory_footprint(df):
    """
    Compute memory footprint of a dataframe

    :param df: input dataframe
    :type df: pd.DataFrame
    :return: dataframe size in MB
    :rtype: float
    """
    # pdb.set_trace()
    m = df.memory_usage(deep=True).sum()
    factor = 1.0 / (2 ** 20)
    m = m * factor
    return m


# basics
def profile_runtime_without_args(f):
    # execute the function
    def inner_func():
        # record the start time
        start_time = time()
        f()
        # get the end time
        end_time = time()
        print("time elapsed: {:.2f} seconds".format(end_time - start_time))

    return inner_func


def profile_runtime_with_args(f):
    # execute the function
    def inner_func(*args, **kwargs):
        # record the start time
        print("calling {} with {}".format(f.__name__, args))
        start_time = time()
        ans = f(*args, **kwargs)
        # get the end time
        end_time = time()
        print("time elapsed: {:.2f} seconds".format(end_time - start_time))
        return ans

    return inner_func


def dataframe_memory_flag(threshold):
    def decorator_body(func):
        def wrapper(*args, **kwargs):
            for df in args:
                m = get_dataframe_memory_footprint(df)
                if m > threshold:
                    print("Memory Error! Exiting!")
                    sys.exit()
            res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator_body


if __name__ == "__main__":

    @profile_runtime_without_args
    def fun():
        print("sleeping for 5 seconds")
        sleep(5)

    # print(fun)
    # print(type(fun))
    # fun()

    @profile_runtime_with_args
    def compute_sum(a, b):
        return a + b

    @profile_runtime_with_args
    def compute_factorial(n):
        sleep(0.5)
        if n == 0:
            return 1
        else:
            return n * compute_factorial(n - 1)

    # r = compute_factorial(7)
    # print(r)
    n = 1000
    df = pd.DataFrame(
        {
            "name": ["h_{}".format(i) for i in range(n)],
            "age": [random.randint(0, 100) for i in range(n)],
        }
    )
    # print(
    # "Dataframe memory consumption: {:.2f} MB".format(
    # get_dataframe_memory_footprint(df)
    # )
    # )

    @dataframe_memory_flag(threshold=0.1)
    def compute_mean_age(df):
        m_age = df["age"].mean()
        return m_age

    res = compute_mean_age(df)
    print("mean age {:.2f} years".format(res))
