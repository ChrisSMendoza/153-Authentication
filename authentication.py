from collections import deque

# GLOBALS
past_passwords = deque(["pass1", "jatelmuffin"]) 

def set_new_password(new_password):

	#password has been used within last 5
	if(used_n_before(new_password)):
		return False

	return True

def used_n_before(new_password):
	
	# not used before
	if(past_passwords.count(new_password) == 0):
		past_passwords.append(new_password)

	print past_passwords
# 	//don't allow password

# //else 
# 	//pop queue, push queue
	return True

# //enforce password history
# 	//don't allow last 5

# //in set new password
# //keep passwords in queue


# TIME TO BRING OUT MY ** MAIN **
new_password = "gameandwatch"	
set_new_password(new_password)









