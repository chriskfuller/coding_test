# Sequence file parser:
# Expected time: 90 min
# Expected results: Complete parser class, unit tests, and brief documentation

# Description:
# The input files will be a list of csv files that each contain some genetic code, as well as some metadata
# The metadata includes a Timestamp, ID for an Output File, and a group that the sequence belongs to.
# Unfortunately, this data is mixed up and you have to write a parser to sort everything into the correct output files and groups.

# Format of input file:
# You can safely assume there is no space within entries, and each information is comma-seperated.
# Each line is formatted as such: RecievedTime is a timestamp in seconds, OutputFileID, Sequence, GroupLetters…, e.g, 1626727507,1,ATCGATCG,#B,#C,#D
# Detail of each entry:
# 1. RecievedTime is an integer of timestamp in seconds, e.g., 123456789
# 2. OutputFileID can only be positive integer, e.g., 3
# 3. Sequence can only contain the letters ‘atcgATCG.’ For example, ‘aaaTTT’ is a valid sequence, whereas ‘QWERTY’ is not.
# 4. Each individual GroupLetter can only come from the capital letters A-Z, and each always includes a single # as its prefix. E.g. #J is valid but #j and @j are not.

# What will your parser do
# 1. Your program must validate the input to follow the rules prescribed below. If a line does not follow these rules, ignore it.
# 2. Your program must output one file for each unique OutputFileID, each file needs to be named as ‘output_<OutputFileID>.csv’, e.g., output_1.csv
# 3. Each output file must only contain lines formatted as such: ‘<GroupLetter>, <GroupConcatenatedSequence>’, e.g., "B,ATCGATCGaaaaAATT"
#	4. GroupConcatenatedSequence is the result of concatenating every Sequence belonging to a certain GroupLetter, after every Sequence has been sorted by ascending Timestamp. 
#    To note, GroupConcatenatedSequence may include sequences from any input file.
# 4. Bonus point:
#       Before you start implement this, think about future needs of scaling up. Bonus point for if you can implement it in such a way that 
#       it can handle input files that are too large to fit into memory.

# Objectives:
# Complete a parser that can inject the input files, process it, and output as desired format files.
# Complete unit tests to ensure the codes work properly.
# Complete a brief documentation, describing the purpose of this parser, and how we can use it.
# The code will be run with our own test suites, thus clear documentation is crucial for us to run it properly.

# Example
# input_1.csv
"1626727507,1,ATCGATCG,#B,#C,#D"
"1626728507,1,aaaa,#A,#B,#C"
"1626737507,2,aaaa,#?A,#B" # Invalid due to wrong format of GroupLetter

# input_2.csv
"1626747507,2,TTTTT,#A,#B"
"1626767507,CCC,#C" # Invalid due to lacking OutputFileId
"1626779507,1,AATT,#B,#C"

# output_1.csv
"B,ATCGATCGaaaaAATT"
"C,ATCGATCGaaaaAATT"
"D,ATCGATCG"
"A,aaaa"
# Explaination:
# From input file 1 and 2, there are 3 lines belong to OutputFileId 1,
# The order of lines based on ascending timestamp are
# "1626727507,1,ATCGATCG,#B,#C,#D"
# "1626728507,1,aaaa,#A,#B,#C"
# "1626779507,1,AATT,#B,#C"
# Thus, the output order will be
# B, C, D and A, since BCD are from line1 and line3, and A from line2.
# The GroupConcatenatedSequence for B will be ATCGATCG (from line1) + aaaa (from line2) + AATT (from line3)

# output_2.csv
"A,TTTTT"
"B,TTTTT"
