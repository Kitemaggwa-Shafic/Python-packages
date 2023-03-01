'''
defining a dynamic function tests with two parameters test1 and test2

'''


def tests(test1, test2):
	# checking if test1 marks enetered are equal to test2 marks entered
	if test1 == test2:
		# using the above if condition, if test1 marks are equal to test2 marks entered, we shall return only test1 marks from this function
		return test1
	else:
		# using the above if condition, if test1 marks are not equal to test2 marks entered, we shall return only test2 marks from this function
		return test2
# declaring a variables test1 and test2 and assigning it input values from user keyboard, and since they are strings, we are typecasting them to integers
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
defining another dynamic function courseWrk with cswork as the parameter

'''
def courseWrk(cswork):
	# declaring a variable testsMark assigning it to return values from tests function
	testsMark = tests(test1,test2)
	# declaring a variable avgtestsCswork and assignning it to cswork marks and the value from testsMark above and diving the sum by 2
	avgtestsCswork = (cswork + testsMark)/2
	# declaring a variable fnltestsCswork and assigning it to the avgtestsCswork value and multiplying it by 40 over 100
	fnltestsCswork = avgtestsCswork * (40/100)
	# printing ......................... to a user to create some ka design 
	print('..............................')
	# printing "your final coursework mark is" to the user and also adding on the calculated final value from function courseWrk
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
# declaring  a variable cswork and assigning it to input value from user keyboard and typecasting it to an integer value
cswork = int(input('Please enter your course work Marks: '))
# invoking a function courseWrk and giving it cswork variable values
courseWrk(cswork)

