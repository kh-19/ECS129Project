import re
#importing modify_gene function to allow users to create mutations given longest ORF 
from genemodifyV5 import *

def main():
        #import file
        while True:
	        fname = input("Name of DNA File: ")
	        try:
	        	dna_file = open(fname, "r")
	        	break
	        except:
	        	print("Incorrect file name. Make sure you are entering the name of a .txt file (e.g. \'dna.txt\'): ")
	        	continue
        print('in file: ',dna_file);

        dna_strand = ""

        #localize file contents to variables
        for i in dna_file:
                
                #get a DNA strand
                dna_strand = i
                dna_strand = dna_strand.upper()
                
                #check DNA strand for miscellaneous characters
                if dna_strand.isalpha() == False:
                	print('Faulty input. Special Characters or Numbers detected in DNA input. Check your DNA sequence and start again.')
                	break
                
                #define what characters are not allowed (only A, T, G, C allowed)
                bad_chars_list = ['B','D','E','F','H','I','J','K','L','M','O','P','Q','R','S','U','V','W','X','Y','Z','/s']
                for i in bad_chars_list:
                    bad_chars = re.compile(i)
                    if(bad_chars.search(dna_strand) == None):
                        continue
                    else:
                        print("Warning: erroneous input detected! Please check DNA sequence and try again.")
                        
                        if i == '\s':
                            print("Unauthorized Space detected in Sequence")
                            return
                            
                        print("Problematic Character Detected:", i)
                        return
                print("No erroneous DNA input!")
                
                #print DNA strand recieved
                print("Cleaned DNA Strand:", dna_strand)

                #get complementary DNA strand (normal and reversed) 
                compl_dna_strand = compl_strand(dna_strand)
                print("Cleaned Complementary DNA Strand: ", compl_dna_strand)
                
                reversed_compl_dna_strand = compl_dna_strand[::-1]
                print("Reversed Complementary DNA Strand: ", reversed_compl_dna_strand)

                #you need to process dna_strand and reversed_compl_dna_strand!
                gene = process_all_seq(dna_strand, reversed_compl_dna_strand)
                
                #neither sequence has start + stop codon present
                if gene == "":
                        print("ERROR: No valid open reading frame detected")
                        break
                else:
                        print("Longest open reading frame: " + gene)

                #beyond the prompt: introducing user interaction with program
                user_strand = modify_ORF(gene)
                if user_strand:
                        user_RNA_strand = dna2rna(user_strand)
                        user_protein = RNAtoAA(user_RNA_strand)
                        print("Your protein sequence: " + user_protein)

                #transcribe longest gene into mRNA
                RNA_strand = dna2rna(gene)
                print("Original sequence RNA strand: " + RNA_strand)

                #translate mRNA into protein
                amino_acid_seq = RNAtoAA(RNA_strand)
                print("Original sequence Protein sequence: " + amino_acid_seq)

        #close file
        dna_file.close()
                
#find complementary strand
def compl_strand(dna_seq):

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

#generating ORF's from complementary strand (through calling below functions); afterwards, comparing ORF's found 
# on complementary strand with original strand to find longest ORF 
def process_all_seq(dna_seq, compl_dna_seq):

        #trying to find valid open reading frame from DNA sequence 
        ##    print("Processing DNA Strand: ")

        # find longest gene on input strand
        gene =  process_seq(dna_seq)


        #trying to find valid open reading frame from complimentary DNA sequence
        #even if you found a gene on the input strand, the complementary strand could still contain
        #a gene that is longer!

        gene1 = process_seq(compl_dna_seq)
        if len(gene1) > len(gene):
          gene = gene1

        return gene

#calling find_ORF to generate 3 ORFs for original DNA strand (by shifting the index for each call); using longest gene found from each ORF 
#and comparing their length to one another 
def process_seq(dna_seq):
        num_of_triplets = int(len(dna_seq) / 3)

        # find longest gene based on first reading frame
        gene = find_ORF(dna_seq)
        #even if you found a gene based on the first reading frame, the second reading frame may contain a longer one
        gene1 = find_ORF(dna_seq[1: ])
        if len(gene1) > len(gene):
          gene = gene1
        #even if you found a gene based on the first and second reading frames, the third reading frame may contain a longer one
        gene1 = find_ORF(dna_seq[2: ])
        if len(gene1) > len(gene):
          gene = gene1
        return gene

#generates open reading frame given dna sequence 
def find_ORF(dna_seq):

        s = ""
        frame_list = []

        longest_gene = ""
        lmax = 0

        #looping through sequence in triplets, adding triplets to initialized list 
        for i in range(0, int(len(dna_seq) / 3)):
                j = i * 3
                s = dna_seq[j:j+3]
                frame_list.append(s)
                s = ""

        #checking list containing triplets to see how many ATG (start codon) + stop codon are found 

        #Initialize start_index to -1: it means not yet detected
        start_index = -1
        stop_index = 0

        ##        print(frame_list)

        for i in range(0, len(frame_list)):

                # if you already detected an ATG, do not resest as this would be a Methionine inside this gene
                if frame_list[i] == "ATG" and start_index == -1:
                    start_index = i
                #only consider stop codon if a start codon has been detected
                if (frame_list[i] == "TAG" or frame_list[i] == "TAA" or frame_list[i] == "TGA") and start_index != -1:
                    stop_index = i
                    gene = frame_list[start_index:stop_index+1]
                    gene = ''.join(gene)
                    length = len(gene)
                    if length > lmax:
                            lmax = length;
                            longest_gene = gene;
                #reset start_index, to see if the program can detect another longer gene after!
                    start_index = -1

        return longest_gene

#transcribe mRNA given DNA sequence; since ORF is in 5'-3', you need to just replace T's with U's
def dna2rna(dna_seq):
        mRNA_seq = ''
        for nucleotide in dna_seq:
                if nucleotide == 'T':
                        mRNA_seq = mRNA_seq + "U"
                else:
                        mRNA_seq = mRNA_seq + nucleotide
        return mRNA_seq

#translate mRNA into amino acid sequence
def RNAtoAA(rna_seq):

        triplet = ''
        rna_seq_list = []
        for i in range(0, int(len(rna_seq) / 3)):
                j = i * 3
                triplet = rna_seq[j:j+3]
                rna_seq_list.append(triplet)
                triplet = ""

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

        aa_seq = ""

        for triplet in rna_seq_list:
                aa = aa_list[triplet]
                aa_seq = aa_seq + aa

        return aa_seq


if __name__ == "__main__":
        main()
