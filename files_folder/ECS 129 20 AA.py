### ECS 129 ###

infile = open('AA_seq.csv', 'r')
AA_table = []

for line in infile:
    line = line.strip()
    (code, name) = line.split(",")
    AA_table.append((code,name))
# AA table is a tuple list of AA's with their three letter codon followed by their 3 letter AA name
print(AA_table)

# print(AA_table[0])