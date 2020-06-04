# program to determine narcissistic numbers - an exploration of Python
# written september 2013
# updated for python 3 June 2020
# setup
overall_number = 0
found_string = "Candidate Found! -> "
final_string = "Narcissistic Numbers through"

def single_eval(eval_one):
#compare and print
	if eval_one ** 1 == eval_one : print(found_string, overall_number)

def square_eval(eval_one,eval_ten) :
#add squares
	squares = eval_one ** 2 + eval_ten ** 2
#eval to overall number and print
	if squares == overall_number : print(found_string, overall_number)


def cube_eval(eval_one,eval_ten,eval_hundred):
#add cubes
	cubes = eval_one ** 3 + eval_ten ** 3 + eval_hundred ** 3
#eval to overall number and print
	if cubes == overall_number : print(found_string, overall_number)
	
def quad_eval(eval_one,eval_ten,eval_hundred,eval_thousand):
#add quads
	quads = eval_one ** 4 + eval_ten ** 4 + eval_hundred ** 4 + eval_thousand ** 4
#eval to overall number and print
	if quads == overall_number : print(found_string, overall_number)
	
def pent_eval(eval_one,eval_ten,eval_hundred,eval_thousand,eval_tenthousand):
#add pents
	pents = eval_one ** 5 + eval_ten ** 5 + eval_hundred ** 5 + eval_thousand ** 5 + eval_tenthousand ** 5
#eval to overall number and print
	if pents == overall_number : print(found_string, overall_number)

for tenthousands in range(0,10):
	for thousands in range(0,10):
		for hundreds in range(0,10):
			for tens in range(0,10):
				for ones in range(0,10):
					# print overall_number
					if overall_number < 10 : single_eval(ones)
					if overall_number > 9 and overall_number < 100 : square_eval(ones,tens)
					if overall_number > 99 and overall_number < 1000 : cube_eval(ones,tens,hundreds)
					if overall_number > 999 and overall_number < 10000 : quad_eval(ones,tens,hundreds,thousands)
					if overall_number > 9999 and overall_number < 100000 : pent_eval(ones,tens,hundreds,thousands,tenthousands)
					overall_number = overall_number + 1
print(final_string, overall_number)

input ("prompt : ")
