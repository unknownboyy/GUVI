def my_function_to_find_factorial(number_to_find_factorial):
    if number_to_find_factorial==0:
        return 1
    return number_to_find_factorial*my_function_to_find_factorial(number_to_find_factorial-1)
number_to_find_factorial_in_main_function=int(input())
print(my_function_to_find_factorial(number_to_find_factorial_in_main_function))