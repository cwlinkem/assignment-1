#!
import sys

program_name = sys.argv[0]

if len(sys.argv) == 3:
	filename = sys.argv[1]
	col_index = int(sys.argv[2])
	input_stream = open(filename, 'rU')
else:
	sys.exit(program_name + ": Expecting two arguments: <filename> <column index>")

product = 1L
for line in input_stream:
	word_list = line.split()
	word_of_interest = word_list[col_index]
	int_of_interest = long(word_of_interest)
	product = product * int_of_interest
print product