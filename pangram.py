import string, sys
	'''
	This program takes in a sentence and checks if it is a 
	pangram(Pangrams are sentences constructed 
	by using every letter of the alphabet at least once) or not

	'''
alphaset = raw_input()
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    if alphaset <= set(str1.lower()) :
        return "pangram"
    else:
        return "not pangram"
 
print  ispangram(alphaset)

