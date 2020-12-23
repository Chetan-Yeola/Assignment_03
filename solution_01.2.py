print("Input:")
number=int(input("Please insert the number: "))
num_list=list(range(1,number+1))
def myfilter(num_list):
   
    num_even_list=[]
    num_odd_list=[]
    
    for i in num_list:
        if(i%5==0):
            if(i%2==0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)
                
    return num_even_list,num_odd_list

output_value=myfilter(num_list)

#Output

print("Output:")
print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])