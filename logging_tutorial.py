# there are 4 levels of logging
# DEBUG: detailed description when diagnosing problems
# INFO: information that things are working as expected
# WARNING: indication that something unexpected happened
# or indication that some problem may arise in future
# ERROR: critical problems causing software to stop

import logging
import class_tutorial

logging.basicConfig(
    level=logging.DEBUG,
    filename="./my_log.log",
    format="%(asctime)s:%(levelname)s:%(processName)s:%(funcName)s:%(message)s",
)


def add_func(*args):
    logging.info("running add_func")
    total = 0
    for e in args:
        total += e
    return total


if __name__ == "__main__":
    res = add_func(2, 3, 4)
    logging.info("adding 2,3,4 gives {}".format(res))
