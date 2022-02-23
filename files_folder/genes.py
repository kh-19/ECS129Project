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

rna_seq = 'AUG CUG'
aa_seq = ''

rna_seq = rna_seq.split()

aa_list = {
	'UUU': 'F',
	'UUC': 'F',
	'UUA': 'L',
	'UUG': 'L',
	'UCU': 'S',
	'UCC': 'S',
	'UCA': 'S',
	'UCG': 'S',
	'UAU': 'Y',
	'UAC': 'Y',
	'UAA': '',
	'UAG': '',
	'UGU': 'C',
	'UGC': 'C',
	'UGA': '',
	'UGG': 'W',
	'CUU': 'L',
	'CUC': 'L',
	'CUA': 'L',
	'CUG': 'L',
	'CCU': 'P',
	'CCC': 'P',
	'CCA': 'P',
	'CCG': 'P',
	'CAU': 'H',
	'CAC': 'H',
	'CAA': 'Q',
	'CAG': 'Q',
	'CGU': 'R',
	'CGC': 'R',
	'CGA': 'R',
	'CGG': 'R',
	'AUU': 'I',
	'AUC': 'I',
	'AUA': 'I',
	'AUG': 'M',	
	'ACU': 'T',
	'ACC': 'T',
	'ACA': 'T',
	'ACG': 'T',
	'AAU': 'N',
	'AAC': 'N',
	'AAA': 'K',
	'AAG': 'K',
	'AGU': 'S',
	'AGC': 'S',
	'AGA': 'R',
	'AGG': 'R',
	'GUU': 'V',
	'GUC': 'V',
	'GUA': 'V',
	'GUG': 'V',
	'GCU': 'A',
	'GCC': 'A',
	'GCA': 'A',
	'GCG': 'A',
	'GAU': 'D',
	'GAC': 'D',
	'GAA': 'E',
	'GAG': 'E',
	'GGU': 'G',
	'GGC': 'G',
	'GGA': 'G',
	'GGG': 'G'
}

for i in rna_seq:
	aa = aa_list[i]
	aa_seq = aa_seq + aa

print(aa_seq)

#close file
dna_file.close()
