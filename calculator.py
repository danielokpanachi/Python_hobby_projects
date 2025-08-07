import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide

}


# numberz = add
# print(numberz(3,5))

should_continue = True

while should_continue:
    temp_store = 0
    first_number = input("Enter a number ")
    f_number = int(first_number)

    pick_operator = input("Choose an operator ")

    second_number = input("Enter a number ")
    s_number = int(second_number)

    if pick_operator == "+":
        addition_operator = operations["+"]
        print(addition_operator(f_number, s_number))
        temp_store = addition_operator(f_number, s_number)
        print(f" This is temp store {temp_store}")
    elif pick_operator == "-":
        addition_operator = operations["-"]
        print(addition_operator(f_number, s_number))
        temp_store = addition_operator(f_number, s_number)
        print(f" This is temp store {temp_store}")
    elif pick_operator == "*":
        addition_operator = operations["*"]
        print(addition_operator(f_number, s_number))
        temp_store = addition_operator(f_number, s_number)
        print(f" This is temp store {temp_store}")
    elif pick_operator == "/":
        addition_operator = operations["/"]
        print(addition_operator(f_number, s_number))
        temp_store = addition_operator(f_number, s_number)
        print(f" This is temp store {temp_store}")



#    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
# if restart == "no":
#     should_continue = False
#     print("Thank you for playing!")

    continue_with_previous = input(f"Type 'yes' to continue calculating with {temp_store} , type 'no' to start new calculation:\n ").lower()
    if continue_with_previous == "yes":
        next_number = input("Enter the next number ")
        n_number = int(next_number)

        pick_operator = input("Choose an operator ")

        # final_result = addition_operator(f_number, s_number) + temp_store

        if pick_operator == "+":
            addition_operator = operations["+"]
            print(addition_operator(temp_store, n_number))
            temp_store = addition_operator(temp_store, n_number)
            print(f" This is temp store {temp_store}")
        elif pick_operator == "-":
            addition_operator = operations["-"]
            print(addition_operator(temp_store, n_number))
            temp_store = addition_operator(temp_store, n_number)
            print(f" This is temp store {temp_store}")
        elif pick_operator == "*":
            addition_operator = operations["*"]
            print(addition_operator(temp_store, n_number))
            temp_store = addition_operator(temp_store, n_number)
            print(f" This is temp store {temp_store}")
        elif pick_operator == "/":
            addition_operator = operations["/"]
            print(addition_operator(temp_store, n_number))
            temp_store = addition_operator(temp_store, n_number)
            print(f" This is temp store {temp_store}")
        continue_with_previous = input(f"Type 'yes' to continue calculating with {temp_store} , type 'no' to start new calculation:\n ").lower()

        # print(f"The final result is {final_result}")
    elif continue_with_previous == "no":
        should_continue = True
