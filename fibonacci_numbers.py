# program to determine Fibonacci numbers - an exploration of Python
# using the Liber Abaci sequence that starts with a 1
#setup
overall_number = 0
start_string = "Calculation of Liber Abaci Fibonacci Series"
inquiry_string = "How many numbers would you like in the series? "
sequence_string = "Fibonacci Series Number"
fibonacci_one = 0
fibonacci_two = 1

#main
print "%s" % (start_string)
series_number = input(inquiry_string)
for series in range(1,series_number+1):
  #Calculate Fibonacci Number
  fibonacci = fibonacci_one + fibonacci_two
  print "%s %d : %d" % (sequence_string, series, fibonacci)
  fibonacci_two = fibonacci_one
  fibonacci_one = fibonacci
	
input ("Press any key to exit : ")