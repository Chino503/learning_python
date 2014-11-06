
#This is how you make a list
the_list = [1, 2.5, 'a'] 
print(the_list)

#This is how you get the length of a list
len(the_list)
print(the_list)

#You can get/change something on a list 
the_list[1] = 'z'
print(the_list)

#This is another way to create a list
another_list = list("Hello")
print(another_list)

# you can check if the list contains something by doing the following:
contains = 'e' in another_list
print(contains)

#this is another example
my_sentence = "This is some random sentence!"
the_split_sentence = my_sentence.split()
print(the_split_sentence)

# This is how you join string
the_joined_list = ' '.join(the_split_sentence) #YOU CANNOT JOIN A LIST OF NUMBERS.
print(the_joined_list)


