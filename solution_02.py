lst=list('xyx')
Output=[a*n for a in lst for n in range(1,5)]
print(Output)

lst1=list('xyz')
Output1=[a*n for n in range(1,5) for a in lst1 ]
print(Output1)

number=[2,3,4]
number1=[[x+n] for x in number for n in range(0,3)]
print(number1)

number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)