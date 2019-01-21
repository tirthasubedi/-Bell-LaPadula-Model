# Moe= only can view 
#Larry= Top Secret 
#Curly=
#Shemp=

# import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'copy.txt')


# class Majestyeye:
# # only be able to view 

# 	def viewonly():



# class Topsecret: 
# 	# can view, create 
# 	def __init__(self, action):
# 		self.action = action

# 	def ask_user(self):
# 		self.action= input("What do you want to do with file: create, read, write: ")



# class Secret:
# 	# can creat own file, cannot write on topsecret 



# class Public:
# 	# they can creat own file but cannot veiw other files





def Majestyeye():
# only be able to view 
	action= input("What do you want to do with file: create, read, write:")
	filename=str(input("Please Enter File Name followed by .txt: "))
	if action == "create":
		f = open(filename, "w")
	elif action == "read":
		f= open(filename, "r")
		print(f.read())
	elif action == "write":
		f=open(filename, "w")
		text=input("Enter the Text that you want to add on textfile: ")
		f.write(text)
		# print(f.wri
	else:
		print("Please Type Correctly")

def Topsecret():
# can view, create 
	action= input("What do you want to do with file: create, read, write:")
	filename=str(input("Please Enter File Name followed by .txt: "))
	if action == "create":
		f = open(filename, "w")
		# print(f.write())
	elif action == "read":
		f= open(filename, "r")
		print(f.read())
	elif action == "write":
		f=open(filename, "w")
		text=input("Enter the Text that you want to add on textfile: ")
		f.write(text)
	
	else:
		print("Please Type Correctly")


def Secret():
	# can creat own file, cannot write on topsecret 
	action= input("What do you want to do with file: create, read, write:")
	filename=str(input("Please Enter File Name followed by .txt: "))
	if action == "create":
		f = open(filename, "w")
		# print(f.write())
	elif action == "read":
		f= open(filename, "r")
		print(f.read())
	elif action == "write":
		f=open(filename, "w")
		text=input("Enter the Text that you want to add on textfile: ")
		f.write(text)
		# print(f.wri
	else:
		print("Please Type Correctly")


def Public():
	# they can creat own file but cannot veiw other files
	action= input("What do you want to do with file: create, read, write:")
	filename=str(input("Please Enter File Name followed by .txt: "))
	if action == "create":
		f = open(filename, "w")
		# print(f.write())
	elif action == "read":
		f= open(filename, "r")
		print(f.read())
	elif action == "write":
		f=open(filename, "w")
		text=input("Enter the Text that you want to add on textfile: ")
		f.write(text)
		# print(f.wri
	else:
		print("Please Type Correctly")


def main():

	print("Welcome to My super-secure program!!")

	user= input("Enter Your name?: ")
	if user == "moe":
		#view only
		a= Majestyeye()
		print(a)

	elif user == "larry":
		b= Topsecret()
		print(b)

	elif user == "curly":
		c= Secret()
		print(c)

	elif user == "shemp":
		d= Public()
		print(d)
	else:
		print("You are New/Unknown User:")
		

main()