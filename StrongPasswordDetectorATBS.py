import re

passwordChanged = False
while passwordChanged == False:
 	
	print('Please type a strong pasword')
	uInput = input()

	#check length
	if len(uInput) < 8:
		print ('A strong password has at least 8 chracters')
	else: 
		pass
	#check for a capital
	capitalRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
	mo = capitalRegex.findall(uInput)

	if mo == []:
		print('A strong password includes both capital and lowercase letters')
		
	else:
		pass
		

	#check for a digit
	digitRegex = re.compile(r'[0123456789]')
	mo = digitRegex.findall(uInput)
	
	if mo == []:
		print('A strong password includes at least one number')
		
	else: 
		passwordChanged = True

password = uInput


print('Please type your new password to unlock the secret message.')
passInput = input()
unlocked = False
while unlocked == False:

	if passInput == password:
		print ('SECRET MESSAGE: I love you!')
		unlocked = True
	else:
		print('That is not the correct password.')
		unlocked = False

x = input()
	