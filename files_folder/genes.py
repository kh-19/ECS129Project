#import file
dna_file = open("dna.txt", "r")
dna = ""

#localize file contents to variables
for i in dna_file:
	dna = i




def compl_strand(dna_seq):
	#slice off 5' end
	dna_seq = dna_seq[3:]
	#slice off 3' end
	dna_seq = dna_seq[:-2]
	
	#PART1: Create Complementary DNA Sequence
	compl_dna_seq = ''
	for nucleotide in compl_dna_seq:
		if nucleotide == 'A':
			compl_dna_seq = sis_dna + "T"
		elif nucleotide == 'T':
			compl_dna_seq = sis_dna + "A"
		elif nucleotide == 'C':
			compl_dna_seq = sis_dna + "G"
		elif nucleotide == 'G':
			compl_dna_seq = sis_dna + "C"
	
	return compl_dna_seq

print(compl_strand(dna))

#close file
dna_file.close()
