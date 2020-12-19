

def len_name(name):
    return len(name)

def greting(name):
    print(f'Hi, good morning {name}')

def age(age):
    if age>0 and age<18:
        print('you are a younger')
    elif age>=18 and age<65:
        print('you are a adult')
    else:
        print('you are a oldman/oldwoman')

input_name = input('enter your name \n >')
input_age = int(input('Enter your age \n >'))

print(len_name(input_name))
greting(input_name)
age(input_age)



