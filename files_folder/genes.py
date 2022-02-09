#import file
dna_file = open("dna.txt", "r")
dna = ""

#localize file contents to variables
for i in dna_file:
	dna = i



#find complmentary strand
def compl_strand(dna_seq):
	#slice off 5' end
	dna_seq = dna_seq[3:]
	#slice off 3' end
	dna_seq = dna_seq[:-2]
	
	#PART1: Create Complementary DNA Sequence
	compl_dna_seq = ''
	for nucleotide in dna_seq:
		if nucleotide == 'A':
			compl_dna_seq = compl_dna_seq + "T"
		elif nucleotide == 'T':
			compl_dna_seq = compl_dna_seq + "A"
		elif nucleotide == 'C':
			compl_dna_seq = compl_dna_seq + "G"
		elif nucleotide == 'G':
			compl_dna_seq = compl_dna_seq + "C"
	
	return compl_dna_seq

#transcribe mRNA given DNA sequence
def dna2rna(dna_seq):
	mRNA_seq = ''
	for nucleotide in dna_seq:
		if nucleotide == 'A':
			mRNA_seq = mRNA_seq + "U"
		elif nucleotide == 'T':
			mRNA_seq = mRNA_seq + "A"
		elif nucleotide == 'C':
			mRNA_seq = mRNA_seq + "G"
		elif nucleotide == 'G':
			mRNA_seq = mRNA_seq + "C"
	return mRNA_seq

print(compl_strand(dna))
print(dna2rna(dna))

#close file
dna_file.close()
