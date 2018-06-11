from collections import deque

# GLOBALS
num_past_pass_allowed = 5
past_passwords = deque(["pass1", "jatelmuffin"], num_past_pass_allowed) 

def set_new_password(new_password):

	#password has been used within last 5
	if(used_before(new_password)):
		#PROMPT FOR OTHER PASSWORD
		return False #dont allow 

	else: #track new password

		#max number of passwords being tracked
		if(len(past_passwords) == num_past_pass_allowed):
			past_passwords.popleft() #stop tracking oldest one

		past_passwords.append(new_password)
		return True
	

def used_before(new_password):
	
	# not used before
	if(past_passwords.count(new_password) == 0):                     
		return False
	
	return True


# TIME TO BRING OUT MY ** MAIN **
new_passes = ["dude", "hey", "phone", "snookie", "other", "other"]

for new_pass in new_passes:
	
	# failed to set new password
	if(set_new_password(new_pass) == False):
		print "the pass *", new_pass, "* has been used in the last ",num_past_pass_allowed


print past_passwords









