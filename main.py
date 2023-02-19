#!/usr/bin/env python3

import os
import socket
from collections import Counter

data_dir = "/home/data"
output_dir = "/home/output"
result_file = os.path.join(output_dir, "result.txt")

# List all text files in the data directory
files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]

# Print the list of text files
print("List of text files in directory:")
output = f"List of text files in directory:\n"
for f in files:
    print(f)
    output += f"{f}\n"

# Read the text files and count the total number of words
total_words = 0
word_counts = Counter()
for f in files:
	with open(os.path.join(data_dir, f)) as file:
        	content = file.read()
        	words = content.split()
        	word_counts.update(words) 
        	total_words += len(words)
	print(f"\nNumber of words in {f} are {len(words)}")
	output += f"Number of words in {f} are {len(words)}\n"
	print(f"The words are \n{words}")
	print(f"\nTop 3 words with maximum count in {f} are {word_counts.most_common(3)}")
	output += f"Top 3 words with maximum count in {f} are {word_counts.most_common(3)}\n"

# Print the total number of words
print(f"\nTotal number of words in both files combined: {total_words}")
output += f"Total number of words in both files combined: {total_words}\n"


# Find the IP address of the machine
#ip_address = os.popen("hostname -I | cut -d' ' -f1").read().strip()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"\nIP address of the machine: {ip_address}")
output += f"IP address of the machine: {ip_address}\n"
    

# Write the output to a file
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
with open(result_file, "w") as file:
    file.write(output)

#print(output.strip())  # print output to console
print(f"\nResults written to {result_file}")
