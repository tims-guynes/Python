def main():

    numbers = [1, 2, 3, 4, 5]
    numbers = double_value(numbers)

    return numbers

def double_value(numbers):
    temp_lst = []
    for num in numbers:
        temp_lst.append(num*2)
    
    return temp_lst

print(main())