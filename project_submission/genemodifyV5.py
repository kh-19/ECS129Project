def modify_ORF(ORF_str):
	#check if ORF_str is an empty string
	if len(ORF_str) == 0:
		print('Invalid Input! Empty String')
	
	#make ORF a list
	ORF = list(ORF_str)
	
	while True:
		#tell user how long their ORF is
		print('Your ORF Length is', len(ORF))
		
		#direct user to choose a ten-nucleotide window to 'zoom in' to a portion of the ORF
		#choose the starting position. For example, a 1 would mean to display positions 1 through 9 (10 positions total)	
		#the variable 'left' represents the leftmost position in the window (if the window shows positions 1-9, left = 1)	
		left = input("Choose a starting position to view ORF (Press 'q' or 'Q' to quit and continue to ORF translation): ")
		#if user wants to quit, they can input 'q' and leave the program
		if left == 'Q' or left == 'q':
			break
		
		try:
			#turn left from a str to an integer, if there is an error with that, head to except block
			left = int(left)
			
			#make sure that value for left is INSIDE the ORF (i.e. prevent input of '54' as left when ORF has only 42 characters)
			if left > len(ORF):
				print()
				print("Invalid input - Starting position greater than length of ORF. Please enter a valid integer.")
				print()
				continue
			#make sure that value for left is neither zero or a negative number - cause that doesn't make sense :)  
			elif left <= 0:
				print()
				print('Invalid input - Staring position less than or equal to zero. Please enter a valid integer.')
				print()
				continue
		#if there's an error in the try block, that means the user entered faulty input. Prod them to input a correct value
		except:
			print()
			print("Invalid input (should be an integer). Try again.")
			print()
			continue
		
		#calculate rightmost position of the window
		right = left + 9
		
		#create a navigation bar that shows the position of nucleotides
		nav_bar = ''
		#create a bar that aligns nucleotides of the ORF sequence with the positions in the nav bar (i.e. if A is 1st, A should be under a '1' to indicate it's at pos 1)
		view_orf = ''
		
		#format the nav bar
		for i in range(left, right+1):
			#if we are dealing with single digit position values, space them out like '1     2     3     4'
			if i < 10:
				i = str(i) + "     "
			#if we are dealing with double digit position values, space them out like '10    11   12   13'
			elif i < 100:
				i = str(i) + "    "
			#if we are dealing with triple digit position values, space them out like '100   101   102   103'
			elif i < 1000:
				i = str(i) + "   "
			#you get the idea, don't you? ;)
			elif i < 10000:
				i = str(i) + "  "
			#for some gargantuan number, one space between position values is good
			else:
				i = str(i) + " "
			#add these strings to the nav bar! since we are using a for loop, the value '1     ' gets added then '2     ' and so on until we have our nav bar!
			nav_bar = nav_bar + i
			
		#slice the orf so that we are viewing the window of the ORF the user wants
		sliced_ORF = ORF[left - 1: right]
		for i in sliced_ORF:
			i = str(i) + "     "
			view_orf = view_orf + i
		
		#print our lovely nav bar and orf so that we see the orf with position values above
		print()
		print(nav_bar)
		print(view_orf)
		print()

		
		#ask where mutation should be
		pos = input("What position should the mutation be made at? (Type \'q\' or \'Q\' to quit and continue to ORF translation). To select a new window, type \'w\' or \'W\'): ")
		pos = pos.upper()
		
		#check if the input signals to quit
		if pos == 'Q':
			break
		#check if input signals to select new window
		elif pos == 'W':
			print()
			continue
		
		#check if the input is an integer
		try:
			pos = int(pos)
		except:
			print("Your input is not an integer! Try again")
			continue
		
		#check if the input is invalid (left of window)
		if pos < left:
			print('Invalid input. Your position value needs to be in the window!')
			continue
		#check if the input is invalid (right of window)
		elif pos > right:
			print('Invalid input. Your position value needs to be in the window!')
			continue
			
		#check if the input is invalid (greater than length of ORF)
		elif pos > (len(ORF)):
			print('Invalid Input. Your position value is greater than the length of the ORF!')
			continue
		
		#adjust position input so it is zero-indexed
		indx = pos - 1
		
		
	#ask what type of mutation do you want?
		ans = input("What kind of mutation should be made at this position? Type \'S\' for substitution, \'I\' for insertion or \'D\' for deletion. Type \'Q\' to quit and continue to ORF translation: ")
		ans = ans.upper()
		
		#check what type of mutation our lovely user wants
		if ans == 'S':
			ORF = subst_nuc(ORF, indx)
		elif ans == 'I':
			ORF = ins_nuc(ORF, indx)
		elif ans == 'D':
			ORF = del_nuc(ORF, indx)
		#help user quit, if they want to
		elif ans == 'Q':
			print("Quitting mutations!")
			break
		#kindly ask user to input something valid
		else:
			print("Incorrect input. Try again.")
			continue
		
		#since we made a muation, slice the updated ORF to show the user the effect of the mutation on the ORF window
		sliced_ORF = ORF[left - 1: right]
		view_orf = ""
		for i in sliced_ORF:
			i = str(i) + "     "
			view_orf = view_orf + i
		
		print()
		print(nav_bar)
		print(view_orf)
		print()
	
	#after edits are done and break out of while loop, return modified ORF
	return ORF

#subsitution - sub in a value from the ORF list with another value the user specifies
def subst_nuc(ORF, indx):
	while True:
		subst = input("Substitude Nucleotide in ORF with: ")
		subst = subst.upper()
		#check to make sure that input is a valid DNA nucleotide (looking at you, Uracil!)
		if subst not in ['A','C','T','G']:
			print('Incorrect Input. Your input should either be \'A\', \'C\', \'T\', or \'G\'. Try again')
			continue
		else:
			break
		
	ORF[indx] = subst
	return ORF

#insertion - insert value in ORF list at user specified position
def ins_nuc(ORF, indx):
	while True:
		#check to make sure that input is a valid DNA nucleotide (looking at you, Uracil!)
		ins = input("Insert what Nucleotide?: ")
		ins = ins.upper()
		if ins not in ['A','C','T','G']:
			print('Incorrect Input. Your input should either be \'A\', \'C\', \'T\', or \'G\'. Try again')
			continue
		else:
			break
	ORF.insert(indx, ins)
	return ORF

#deletion - delete value in ORF list at user specified position
def del_nuc(ORF, indx):
	try:
		ORF.pop(indx)
		return ORF
	except:
		print("Error! Do you have an empty string?")
