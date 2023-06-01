#declare 2 numbers
#read the values
#add the 2 numbers and assign to a new variable
#display the sum
#end program

def add_two_num():
    print("Please give me 2 numbers to add together")
    num1 = input("first number: ")
    num2 = input("second number: ")

    if num1.isalpha() or num2.isalpha():
        if num1.isalnum() or num2.isalnum():
            return "Please enter valid numbers!"
    else:
        return int(num1) + int(num2)

print(add_two_num())