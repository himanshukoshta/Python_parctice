## Define a function that takes a variable number of integer arguments and returns their product. 
# Test the function with different inputs.
def product(*args):
    pro=1
    for i in args:
        pro*=i
    return pro
    
print(product(1,2,3,4))