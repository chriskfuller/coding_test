# CSV file parser
# Expected time: 1.5-2 hr
# Expected result: parser, unit tests, brief documentation

#You’re given a list of csv files that each contain some genetic code, as well as some metadata
#The metadata includes a Timestamp, ID for an Output File, and a group that the sequence belongs to.
#Unfortunately, this data is mixed up and you have to write a parser to sort everything into the correct output files and groups.

# Assume there is no space, and each information is comma-seperated
# Each line is formatted as such:
# Timestamp, OutputFileID, Sequence, GroupLetters…

# Requirements
# 1. Your program must validate the output to follow the rules prescribed below. If a line does not follow these rules, ignore it.
# 2. Your program must output one file for each unique OutputFileID, each named ‘output_<OutputFileID>.csv’
# 3. Each output file must only contain lines formatted as such:
#	‘<GroupLetter>, <GroupConcatenatedSequence>’
#	GroupConcatenatedSequence is the result of concatenating every Sequence belonging to a certain GroupLetter,
#	after every Sequence has been sorted by ascending Timestamp.
#
#	GroupConcatenatedSequence may include sequences from any input file.
# 4. Bonus point:
#       Before you start implement this, think about future scale up. Bonus point for if you can implement it in such a way that 
#       it can handle input files that are too large to fit into memory.

# Rules for lines:
# 1. RecievedTime is a timestamp, e.g., 123456789
# 2. OutputFileID can only be positive integer, e.g., 3
# 3. Sequence can only contain the letters ‘atcgATCG.’ For example, ‘aaaTTT’ is a valid sequence, whereas ‘QWERTY’ is not.
# 4. Each individual GroupLetter can only come from the capital letters A-Z, and each always includes a single # as its prefix. E.g. #J is valid but #j and @j are not.

# Example
# input_1.csv
"1626727507,1,ATCGATCG,#B,#C,#D"
"1626728507,4,GGG,#D"
"1626728507,1,aaaa,#A,#B,#C"
"1626729508,4,aaaa,#A,#B"
"1626737507,4,aaaa,#?A,#B" # Invalid due to wrong format of GroupLetter

# input_2.csv
"1626747507,2,TTTTT,#A,#B"
"1626757507,3,CCC,#C"
"1626767507,CCC,#C" # Invalid due to lacking OutputFileId
"1626779507,1,AATT,#B,#C"
"1626787507,4,atcg,#C,#D"

# output_1.csv
"B,ATCGATCGaaaaAATT"
"C,ATCGATCGaaaaAATT"
"D,ATCGATCG"
"A,aaaa"
# Explaination:
# From input file 1 and 2, there are 3 lines belong to OutputFileId 1,
# The order of lines are
# "1626727507,1,ATCGATCG,#B,#C,#D"
# "1626728507,1,aaaa,#A,#B,#C"
# "1626779507,1,AATT,#B,#C"
# Thus, the output order will be
# B, C, D and A, since BCD are from line1, and A from line2.
# The GroupConcatenatedSequence for B will be ATCGATCG (from line1) + aaaa (from line2) + AATT (from line3)

# output_2.csv
"A,TTTTT"
"B,TTTTT"
# output_3.csv
"C,CCC"
# output_4.csv
"D,GGGatcg"
"A,aaaa"
"B,aaaa"
"C,atcg"

