  
import os
import os. path
def creating_folders():
		
	print("we are creating folders in {}".format(os.getcwd()))

	if not "new_dir" in os.listdir():
		os.makedirs("new_dir/Dir1/Dir2")
		os.makedirs("new_dir/Dir1/Dir3/Dir4")
		os.chdir("new_dir")
		
		with open('File.txt', 'w') as f:
			pass
	else:
		os.chdir("new_dir")
		list_new_dir1 = os.listdir()
		if not "Dir1" in list_new_dir1:
			os.makedirs("Dir1/Dir2")	
			os.makedirs("Dir1/Dir3/Dir4")	
		else:
			os.chdir('Dir1')
			list_new_dir2 = os.listdir()
			if not "Dir2" in list_new_dir2:
				os.mkdir('Dir2')
				os.makedirs('Dir3/Dir4')
			else:
				os.chdir('Dir3')
				list_new_dir3 = os.listdir()
				if not "Dir4" in list_new_dir3:
					os.mkdir('Dir4')
	return "folders creating this is path "
def deleting():
	os.chdir(os.getcwd())
	deleting_path = int(input("pleas tell me wiche path do you want to delete"))
	if deleting_path == 1 and not os.listdir("new_dir/Dir1/Dir3/Dir4"):
		
		os.chdir("new_dir/Dir1/Dir3")
		os.rmdir("Dir4")
	elif deleting_path == 2 and not os.listdir("new_dir/Dir1/Dir2"):
		os.chdir(os.getcwd())
		if os.listdir('new_dir/Dir1/Dir3'):
			os.rmdir('new_dir/Dir1/Dir3/Dir4')	
			os.rmdir('new_dir/Dir1/Dir2')
			os.rmdir("new_dir/Dir1/Dir3")
		else:
			os.rmdir('new_dir/Dir1/Dir2')
			os.rmdir("new_dir/Dir1/Dir3")
	# elif deleting_path == 2 and not os.listdir("new_dir/Dir1/Dir3"):
	# 	os.chdir("new_dir/Dir1")
	# 	os.rmdir("Dir3")
	elif deleting_path ==3 and not os.listdir("new_dir/Dir1"):
		os.chdir(os.getcwd())
		if os.listdir('new_dir/Dir1') :
			if os.listdir('new_dir/Dir1/Dir3'):
				os.rmdir('new_dir/Dir1/Dir3/Dir4')	
			os.rmdir('new_dir/Dir1/Dir2')
			os.rmdir("new_dir/Dir1/Dir3")
			os.rmdir("new_dir/Dir1")
			os.remove('new_dir/File.txt')
		else:
			os.rmdir("new_dir/Dir1")
			os.remove('new_dir/File.txt')
		
	elif deleting_path == 4 and not os.listdir("new_dir") :
			if os.listdir('new_dir/Dir1') :
				if os.listdir('new_dir/Dir1/Dir3') and os.listdir('new_dir/Dir1/Dir2'):
					os.rmdir('new_dir/Dir1/Dir3/Dir4')
				else:
					os.rmdir('new_dir/Dir1/Dir2')
					os.rmdir('new_dir/Dir1/Dir3')
			else:
				os.rmdir('new_dir/Dir1')
	else:
		os.rmdir('new_dir')
	
s = input("Do you want to creat folders path")
if s == "yes" :
	creating_folders()
else:
	delete = input("Do you want to delete folders")
	if delete == 'yes':
		deleting()
	else:
		print("by")

