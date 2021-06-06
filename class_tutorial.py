import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.name = f_name + " " + l_name
        logger.info(f"Employee object created with name as {self.name}")


if __name__ == "__main__":
    e1 = Employee("Raja", "Biswas")

