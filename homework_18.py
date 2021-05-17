import os
import os. path

print("we are creating folders in {}".format(os.getcwd()))

if not "new_dir" in os.listdir() or not os.listdir('new_dir') :
	
	os.makedirs("new_dir/Dir1/Dir2")
	os.makedirs("new_dir/Dir1/Dir3")
	f = os.path.join("new_dir","File"+"txt")
	
else:

	list_new_dir1 = os.listdir("new_dir")
	
	if not "Dir1" in list_new_dir1:
		os.makedirs("new_dir/Dir1/Dir2")	
		os.makedirs("new_dir/Dir1/Dir3")
		
	else:
		list_new_dir2 = os.listdir('new_dir/Dir1')
		if not "Dir2" in list_new_dir2:
			os.mkdir('new_dir/Dir1/Dir2')
		elif not 'Dir3' in list_new_dir2:
			os.mkdir('new_dir/Dir1/Dir3')
def deleting():
	
	deleting_path = int(input("pleas tell me wiche path do you want to delete"))
	if deleting_path == 1 and not os.listdir("new_dir/Dir1/Dir3"):
		os.chdir("new_dir/Dir1")
		os.rmdir("Dir3")
		os.rmdir("Dir2")
	elif deleting_path == 2 and not os.listdir("new_dir/Dir1"):
		print(kkkkk)
		os.chdir("new_dir")
		os.rmdir("Dir1")
	elif deleting_path ==3 and not os.listdir("new_dir"):
		os.chdir(os.getcwd())
		os.rmdir("new_dir")	


	
#print(os.listdir('new_dir/Dir1'))

