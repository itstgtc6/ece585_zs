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

n_sets = 15;		
n_ways = 3;		# maximum of 3 (value of 8)
n_linesize = 6;		# min: 5 max: 7 (value of 128)

numtrace = 3;	# number of traces or test cases

# Replacement policies
replacement_policy = 0; # True LRU = 0 | 1-bit LRU = 1

# Parameters
num_sets = 2**n_sets;	
num_ways = 2**n_ways;
line_size = 2**n_linesize; 

# Checking if parameters are within certain bounds 
if num_ways > 8:
	print("ERROR: associativity cannot be greater than 8")
	exit()

elif line_size > 128 or line_size < 32:
	print("ERROR: line size must be between 32 and 128")
	exit() 

# functions: getting how many bits belong in each field 
def get_taglength(address):
	taglength = len(address) - n_sets - n_linesize
	print(len(address))
	print(taglength)

def get_index(address):
	# of cache blocks per set: line_size
	indexlength = n_sets - n_ways
	print(indexlength)

# function: reading cache
#def read_cache(address):
#	index = get_index(

#read input trace from txt file
trace = open("word.txt", "r")

while i < numtrace:

	read_trace = trace.readline()

	data = read_trace.split();
	# Converting addresses to binary 
	address =  "{0:08b}".format(int(data[1],16))
	tag = get_taglength(address)
	print(tag)
	# get_index()	

	if data[0] == "0":
		print("read request");

	if data[0] == "1": 
		print("write request");

	if data[0] == "2":
		print("invalidation request");
		
	i = i + 1;
	

