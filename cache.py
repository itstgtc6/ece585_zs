import random
import math

read = 0;
readmiss = 0; 
write = 0;
writemiss = 0;
writeback = 0; 
swaprequest = 0; 
swap = 0; 
i = 0

n_sets = 0;		
n_ways = 0;		# maximum of 3 (value of 8)
n_linesize = 0;		# min: 5 max: 7 (value of 128)

numtrace = 3;	# number of traces or test cases

# Replacement policies
replacement_policy = 0; # True LRU = 0 | 1-bit LRU = 1

# Parameters inputed by the user 
num_sets = 2**n_sets;	
num_ways = 2**n_ways;
line_size = 2**n_linesize; 

num_sets = input("Enter number of sets: ")
n_sets = math.log(num_sets, 2)
print(n_sets)

num_ways = input("Enter ways association: ")
n_ways = math.log(num_ways,2)
print(n_ways)

if num_ways > 8:
	print("ERROR: associativity cannot be greater than 8")
	exit()

line_size = input("Enter line size: ")
n_linesize = math.log(line_size,2)
print(n_linesize)

if line_size > 128 or line_size < 32:
	print("ERROR: line size must be between 32 and 128")
	exit() 

replacement_policy = input("input a 0 for True LRU and a 1 for 1-bit LRU: ")
if(replacement_policy != 0 and replacement_policy != 1):
	print("ERROR: inputs are outside of specified bounds")
	exit()


# functions: getting how many bits belong in each field 
# Currently only showing 8 bits and should show 32 bits 
def get_taglength(address):
	global taglength
	taglength = 32 - n_sets - n_linesize

def get_index(address):
	# of cache blocks per set: line_size
	global indexlength
	indexlength = n_sets - n_ways
#	print(indexlength)

def convert_to_binary(addy):
	global address
	address = "{:032b}".format(int(addy,16))
	
# function: reading cache
def read_cache(address):
	


#read input trace from txt file
trace = open("word.txt", "r")

while i < numtrace:

	read_trace = trace.readline()

	data = read_trace.split();
	# Converting addresses to binary 
	convert_to_binary(data[1])
	get_taglength(address)
	print(data[1])
	print(address)
	print(taglength)	

	if data[0] == "0":
		print("read request");

	if data[0] == "1": 
		print("write request");

	if data[0] == "2":
		print("invalidation request");
		
	i = i + 1;



