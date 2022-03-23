print("Enter parameters: ")

print('''Examples of input:
1, 5, -3, 'abc', [12, 56, 'cad']
or 
2, 4, ‘abc’, param_1=2
or leave it blank
''')

args = input()


def my_undefinite_number_of_param_func(*args):
    items_sum = 0
    items_from_tuple = args
    if len(items_from_tuple) == 0:
        return 0
    else:
        for item in items_from_tuple:
            if isinstance(item, int):
                items_sum = items_sum + item
        return items_sum


print(my_undefinite_number_of_param_func(args))


def number_sums(first_number):
    total_even = 0
    total_odd = 0
    total_sum = 0
    recursive_sum = 0

    def recursive_sum(first_number):
        if first_number <= 1:
            return first_number
        return first_number + recursive_sum(first_number - 1)

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
