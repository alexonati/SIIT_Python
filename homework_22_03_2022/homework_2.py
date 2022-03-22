def my_undefinite_number_of_param_func(*args):
    numbers = 0
    items_from_tuple = args
    if len(args) == 0:
        return 0
    else:
        print(len(args))
        for item in items_from_tuple:
            try:
                number = int(item)
                numbers = numbers + number
            except ValueError:
                pass
        return numbers


args = input("Please enter the parameters: ")

print(my_undefinite_number_of_param_func(args))
print(my_undefinite_number_of_param_func(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_undefinite_number_of_param_func())


def number_sums(first_number):
    total_even = 0
    total_odd = 0
    total_sum = 0
    recursive_sum = 0

    def recursiveSum(first_number):
        if first_number <= 1:
            return first_number
        return first_number + recursiveSum(first_number - 1)

    if first_number <= 1:
        return first_number
    elif first_number > 1:
        total_sum = recursive_sum(first_number)
        for number in range(1, first_number + 1):
            if number % 2 == 0:
                total_even = total_even + number
            else:
                total_odd = total_odd + number
    return total_sum, total_even, total_odd


def is_the_number_whole(second_number):
    if second_number.isdigit():
        if int(second_number) - float(second_number) == 0:
            print(f"The number you have entered, number {second_number}, is a whole number.")
    else:
        print(0)


while True:
    first_number = input(" Please Enter the number you need the different sums for: ")
    try:
        first_number = int(first_number)
    except ValueError:
        continue
    else:
        break
print(
    f"The sums of all numbers between [0, n], of all even numbers and all odd numbers are: {number_sums(first_number)}")

while True:
    second_number = input(" Please Enter the number to check for wholeness: ")
    try:
        second_number = int(second_number)
    except ValueError:
        continue
    else:
        break

is_the_number_whole(second_number)
