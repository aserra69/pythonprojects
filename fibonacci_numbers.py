# program to determine Fibonacci numbers - an exploration of Python
# using the Liber Abaci sequence that starts with a 1
# written september 2013
# updated for python 3 June 2020
# setup
overall_number = 0
start_string = "Calculation of Liber Abaci Fibonacci Series"
inquiry_string = "How many numbers would you like in the series? "
sequence_string = "Fibonacci Series Number"
fibonacci_one = 0
fibonacci_two = 1

#main program
#prompt the user
print(start_string)
#Take size of series and assign to veriable as an integer
series_number = int(input(inquiry_string))
#Loop through the series size requested
for series in range(1,series_number+1):
  #Calculate Fibonacci Number
  fibonacci = fibonacci_one + fibonacci_two
  print(sequence_string, series, fibonacci)
  #Move number to prepare for next cycle
  fibonacci_two = fibonacci_one
  fibonacci_one = fibonacci
	
input ("Press any key to exit : ")
