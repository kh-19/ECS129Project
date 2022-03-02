ORF_str = "ACTGGGGGGGGGGGGGGGGGGGGGGGG"

def modify_ORF(ORF_str):
	#check if ORF_str is an empty string
	if len(ORF_str) == 0:
		print('Invalid Input! Empty String')
	
	#make ORF a list
	ORF = list(ORF_str)
	
	while True:
		#view the ORF:
		print('Your ORF Length is', len(ORF))		
		left = input("Starting position to view ORF (Press 'q' or 'Q' to quit and continue to ORF translation): ")
		if left == 'Q' or left == 'q':
			break
		
		try:
			left = int(left)
			if left > len(ORF):
				print()
				print("Invalid input - Starting position greater than length of ORF. Please enter a valid integer.")
				print()
				continue
			elif left <= 0:
				print()
				print('Invalid input - Staring position less than or equal to zero. Please enter a valid integer.')
				print()
				continue
		except:
			print()
			print("Invalid input (should be an integer). Try again.")
			print()
			continue
		
		right = left + 9
		
		nav_bar = ''
		view_orf = ''
		
		for i in range(left, right+1):
			if i < 10:
				i = str(i) + "     "
			elif i < 100:
				i = str(i) + "    "
			elif i < 1000:
				i = str(i) + "   "
			elif i < 10000:
				i = str(i) + "  "
			else:
				i = str(i) + " "
			
			nav_bar = nav_bar + i
			
		
		sliced_ORF = ORF[left - 1: right]
		for i in sliced_ORF:
			i = str(i) + "     "
			view_orf = view_orf + i
		
		print()
		print(nav_bar)
		print(view_orf)
		print()

		
		#ask where mutation should be
		pos = input("What position should the mutation be made at? (Type \'q\' or \'Q\' to quit and continue to ORF translation). To select a new window, type \'w\' or \'W\': ")
		pos = pos.upper()
		
		#check if the input signals to quit
		if pos == 'Q':
			break
		elif pos == 'W':
			print()
			continue
		
		#check if the input is an integer
		try:
			pos = int(pos)
		except:
			print("Your input is not an integer! Try again")
			continue
		
		#check if the input is invalid (lesser than left value of window)
		if pos < left:
			print('Invalid input. Your position value needs to be in the window!')
			continue
			
		#check if the input is invalid (greater than length of ORF)
		elif pos > (len(ORF)):
			print('Invalid Input. Your position value is greater than the length of the ORF!')
			continue
		
		#adjust position input so it is zero-indexed
		indx = pos - 1
		
		
	#ask what type of mutation do you want?
		ans = input("What kind of mutation should be made at this position? Type 'S' for substitution, 'I' for insertion or 'D' for deletion. Type 'Q' to quit and continue to ORF translation: ")
		ans = ans.upper()
		
		if ans == 'S':
			ORF = subst_nuc(ORF, indx)
		elif ans == 'I':
			ORF = ins_nuc(ORF, indx)
		elif ans == 'D':
			ORF = del_nuc(ORF, indx)
		elif ans == 'Q':
			print("Quitting mutations!")
			break
		else:
			print("Incorrect input. Try again.")
			continue

		sliced_ORF = ORF[left - 1: right]
		for i in sliced_ORF:
			i = str(i) + "     "
			view_orf = view_orf + i
		
		print()
		print(nav_bar)
		print(view_orf)
		print()

#subsitution
def subst_nuc(ORF, indx):
	subst = input("Substitude Nucleotide in ORF with: ")
	ORF[indx] = subst
	return ORF

#insertion
def ins_nuc(ORF, indx):
	ins = input("Nucleotide to insert into ORF: ")
	ORF.insert(indx, ins)
	return ORF

#deletion
def del_nuc(ORF, indx):
	try:
		ORF.pop(indx)
		return ORF
	except:
		print("Error! Do you have an empty string?")

def main():
	modify_ORF(ORF_str)

main()
