#This are a few examples of how to use the range()
for i in range(5):
	print(i) #0,1,2,3,4

ex_1 = range(5, 10)
print(ex_1) # [5, 6, 7, 8, 9]

ex_2 = range(0, 10, 3)
print(ex_2) # [0, 3, 6, 9]

ex_3 = range(-10, -100, -30)
print(ex_3) #[-10, -40, -70]

# Iterating over indeces
sentence = "Mary had a little lamb".split()
for i in range(len(sentence)):
	print(i, sentence[i])

# This is something strange
print(range(0,10))