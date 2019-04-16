from main import *

get_info()

while True:
	choice = get_action()
	if choice > 3:
		break
	else:
		run(choice)
		print()