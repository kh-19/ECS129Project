def modify_gene(gene):

    s = ""
    #creating 2 copies of frame_list: one where deletion operation is done, another where duplication operation
    # is done
    frame_list = []
    location_of_input = []

    #convert gene to list of triplets 
    for i in range(0, int(len(gene) / 3)):
        j = i * 3
        s = gene[j:j+3]
        frame_list.append(s)
        s = ""

    responses = ['Yes', 'yes'] 
    inp = input("Would you like to mutate the longest open reading frame (i.e. duplicate or delete bases)? Respond Yes or No: ")
    
    if inp in responses:
        
        #if they want to modify the gene
        inp = input("Enter 3 bases that you would like to mutate in the sequence: ")
        #convert their input to upper case in order to match with format of sequence
        inp = inp.upper() 
        
        #checking that they sequence they chose is present in the longest ORF we gave them 
        if inp in gene:

            #MUTATION #1: DELETION
            inp_index = -1
            
            for i in range(0, len(frame_list)):
                
                # if you already detected the input triplet, do not reset
                if frame_list[i] == inp and inp_index == -1:
                    inp_index = i
                    location_of_input.append(inp_index)
                    
                #reset inp_index, to see if the program can detect another input triplet 
                    inp_index = -1

            print("Your triplet is located at the following indexes: ", location_of_input)
            inp = input("Choose the index from which you would like to mutate your triplet (i.e: 0, 2, etc.): ")
            
            #answer comes as string --> need to convert to integer
            inp = int(inp)
            if inp in location_of_input:
                #removes user triplet from list at the index they chose 
                frame_list.pop(inp)
                #converting list to sequence of letters
                frame_list = ''.join(frame_list)
                return frame_list
            else:
                while inp not in location_of_input:
                    inp = input("Enter a valid index: ")
                
        #if user didn't enter a triplet that's in the gene                  
        else:
            while inp not in gene:
                inp = input("That triplet is not present! Please enter another set of 3 bases: ")
    
    else:
        print("Ok! The protein from the current gene will be printed below.")

    

    


        
    
