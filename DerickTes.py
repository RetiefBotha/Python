def factorial(number):
    product=1
    for i in range(number):
        product=product *(i+1)
    return product

User_input=input('Please enter a pos number')
print(factorial(eval(user_input)))
 
