#1 function that accepts a list of numbers as an argument 

def sum_of_odd_numbers(list_of_numbers): 
    total = 0
    for num in list_of_numbers:
        if num % 2 != 0: 
            total += num 
    return total 

numbers= [1,2,3,4,5,6,7]
print(sum_of_odd_numbers(numbers))  

#2 

name_list = ['abigail', 'duncan', 'monty']
name = input("Name please!").lower()

if name not in name_list:
    print("Who goes there?")
else:
    print(f"Welcome home {name}!")
