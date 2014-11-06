#This is how Python Collections work

a_list = [1,2,3]
print(a_list)
a_list.append([4,5])
print(a_list)

# range is for getting lists whatever size you want it will add 0 to a number less then the one you input.
b_list = list(range(10)) 
print(b_list)
b_list = b_list+[10,11,12]
print(b_list)