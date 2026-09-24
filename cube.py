# define function to calculate cube
def cube(number):
    return number*number*number

#define a function which will execute a cube function if the user enter number is divisible by three
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
#desplay result
print(by_three(9))
print(by_three(4))

