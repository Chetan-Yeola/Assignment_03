def myreduce(num):
    num_list=list(range(1,number+1))
    sum_of_elements=0
    for i in num_list:
        sum_of_elements+=i
    return num_list,sum_of_elements
print("Input:")
number=int(input("Please insert the number :"))
output_value=myreduce(number)
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])