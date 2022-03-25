"""
Carlos Barona
my_module
"""

def greeting(name):
    return(f'Hello, {name}')

def letter_text(**kwargs):
    if 'name' and 'amount' and 'denomination' in kwargs:
        return(f"Hello {kwargs['name']}, this letter is to inform you that you have won {kwargs['amount']} {kwargs['denomination']}.")
    else:
        return("incorrect parameters supplied")


print(letter_text(name = "Carlos", amount = "7", denomination = "Yen"))