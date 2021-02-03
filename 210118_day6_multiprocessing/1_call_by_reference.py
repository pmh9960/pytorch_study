import numpy as np

# Every functions of python call by reference
def function(var):
    # global var  # 도 가능 (but don't use global variable)
    var += 1
    print("Variable in function:", var)


def function_set(set):
    set.add(1231)
    print("Variable in function:", set)


if __name__ == "__main__":
    var = np.ones((10,))  # global variable (declare in __main__)
    print("Variable in main    :", var)
    function(var)

    var1 = 1  # function call by reference but 1 is immutable
    print("Variable in main    :", var1)
    function(var1)

    # Immutable variables (Similar to call by value)
    var_str = "minho"
    var_int = 1
    var_float = 1.123
    var_tuple = ("min", "ho", 123)

    print("Variable in main    :", var_int)
    function(var_int)
    print("Variable in main    :", var_float)
    function(var_float)

    # Mutable variables (call by ref)
    var_list = []
    var_dict = {"1": 123}
    var_set = {123}
    var = np.ones((10,))
    print("Variable in main    :", var_set)
    function_set(var_set)
