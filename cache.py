import random
import math

read = 0;
readmiss = 0; 
write = 0;
writemiss = 0;
writeback = 0; 
swaprequest = 0; 
swap = 0; 

n1 = 0;		
n2 = 0;		# maximum of 3 (value of 8)
n3 = 0;		# maximum of 7 (value of 128)

numtrace = 3;	# number of traces or test cases
i = 0;

# Replacement policies
replacement_policy = 0; # True LRU = 0 | 1-bit LRU = 1

# Parameters
num_sets = 2^n1;	
num_ways = 2^n2;
line_size = 2^n3;

#read input trace from txt file
trace = open("word.txt", "r");

while i < numtrace:

	read_trace = trace.readline()

	data = read_trace.split();
	print(data[0]);
	print(data[1]);

	if data[0] == "0":
		print("read request");

	if data[0] == "1": 
		print("write request");

	if data[0] == "2":
		print("invalidation request");
	
	i = i + 1;
