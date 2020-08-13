
#list = range(10,15)

#print list
#print list[2]

#	print "I love you Anshuma!"


def fibonacci(N):
	fib_list = [1,1]
	i = 2
	while i <= N:
		x = fib_list[i-1] + fib_list[i-2]
		fib_list.append(x)
		i = i + 1
	print fib_list	


def factorial(N):
	i = N
	result = 1
	while i > 0:
		result = result*i
		#print result 
		i-=1
	return result
	
	
def print_even(N):
	for i in range(1,N+1):
		if i % 2 == 0:
			print i,

user_input = raw_input("Hey dude, give me a numnber to calculate ;) = ")
print_even(int(user_input))




	


