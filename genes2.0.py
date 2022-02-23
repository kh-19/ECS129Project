
def main():
        
        #import file
        dna_file = open("dna.txt", "r")
        print('in file: ',dna_file);

        dna_strand = ""

        #localize file contents to variables
        for i in dna_file:
                
                #get a DNA strand
                dna_strand = i
                print("Original DNA Strand:", dna_strand)
                
                #slice off 5' end
                dna_strand = dna_strand[3:]
                #slice off 3' end
                dna_strand = dna_strand[:-4]
                print("Cleaned DNA Strand:", dna_strand)

                #get complementary DNA strand (normal and reversed) 
                compl_dna_strand = compl_strand(dna_strand)
                print("Cleaned Complementary DNA Strand: ", compl_dna_strand)
                
                reversed_compl_dna_strand = compl_dna_strand[::-1]
                print("Reversed Complementary DNA Strand: ", reversed_compl_dna_strand)

                #process both DNA strands

# PK: Careful, you need to process dna_strand and reversed_compl_dna_strand!

                gene = process_all_seq(dna_strand, reversed_compl_dna_strand)
                
                #neither sequence has start + stop codon present
                if gene == "":
                        print("ERROR: No valid open reading frame detected")
                else:
                        print("Longest open reading frame: " + gene)

                #transcribe longest gene into mRNA
                RNA_strand = dna2rna(gene)
                print("RNA strand: " + RNA_strand) 

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


def process_all_seq(dna_seq, compl_dna_seq):

    #trying to find valid open reading frame from DNA sequence 
    print("Processing DNA Strand: ")

    # find longest gene on input strand
    gene =  process_seq(dna_seq)


    #trying to find valid open reading frame from complimentary DNA sequence
    
# PK: even if you found a gene on the input strand, the complementary strand could still contain
#     a gene that is longer!

    gene1 = process_seq(compl_dna_seq)
    if len(gene1) > len(gene):
          gene = gene1

    return gene


def process_seq(dna_seq):
    num_of_triplets = int(len(dna_seq) / 3)
    
# PK: find longest gene based on first reading frame
    gene = find_ORF(dna_seq)
# PK: even if you found a gene based on the first reading frame, the second reading frame may contain a longer one
    gene1 = find_ORF(dna_seq[1: ])
    if len(gene1) > len(gene):
          gene = gene1
# PK: even if you found a gene based on the first and second reading frames, the third reading frame may contain a longer one
    gene1 = find_ORF(dna_seq[2: ])
    if len(gene1) > len(gene):
          gene = gene1
    return gene
    
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

# PK: Initialize start_index to -1: it means not yet detected
        start_index = -1
        stop_index = 0

        print(frame_list)

        for i in range(0, len(frame_list)):

# PK: if you already detected an ATG, do not resest as this would be a Methionine inside this gene
                if frame_list[i] == "ATG" and start_index == -1:
                    start_index = i
# PK: only consider stop codon if a start codon has been detected
                if (frame_list[i] == "TAG" or frame_list[i] == "TAA" or frame_list[i] == "TGA") and start_index != -1:
                    stop_index = i
                    gene = frame_list[start_index:stop_index+1]
                    gene = ''.join(gene)
                    length = len(gene)
                    if length > lmax:
                            lmax = length;
                            longest_gene = gene;
# PK: reset start_index, to see if the program can detect another longer gene after!
                    start_index = -1

        return longest_gene

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

if __name__ == "__main__":
        main()
