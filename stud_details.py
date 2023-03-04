student_data=[]
teacher_data=[]
print("top")
def create_student():
	rollno=input("Enter your Roll no:")
	name=input("Enter your name:")
	age=input("Enter your age:")
	dept=input("Enter your department")
	student_creation=create_student_data(rollno,name,age,dept)
	print({"status":1,"message":"created successfully"})
	status=int(input("Enter 1 for student detail\nEnter 2 for Teacher detail\nEnter 3 to get student detail\nEnter 4 to get Teacher detail"))
	check_status(status)
def create_student_data(rollno,name,age,dept):
	data={
	"rollno":rollno,"name":name,"age":age,"dept":dept
	}
	student_data.append(data)

def create_teacher():
	staffid=input("Enter your staff id:")
	name=input("Enter your name:")
	age=input("Enter your age:")
	dept=input("Enter your department")
	staff_creation=create_staff_data(staffid,name,age,dept)
	print({"status":1,"message":"created successfully"})
	status=int(input("Enter 1 for student detail\nEnter 2 for Teacher detail\nEnter 3 to get student detail\nEnter 4 to get Teacher detail"))
	check_status(status)
def create_staff_data(staffid,name,age,dept):
	data={
	"staffid":staffid,"name":name,"age":age,"dept":dept
	}
	teacher_data.append(data)

def get_student():
	print(student_data)
	status=int(input("Enter 1 for student detail\nEnter 2 for Teacher detail\nEnter 3 to get student detail\nEnter 4 to get Teacher detail"))
	check_status(status)
def get_teacher():
	print(teacher_data)
	status=int(input("Enter 1 for student detail\nEnter 2 for Teacher detail\nEnter 3 to get student detail\nEnter 4 to get Teacher detail"))
	check_status(status)

def check_status(status):
	if status==1:
		create=create_student()
	elif status==2: 
		create=create_teacher()
	elif status==3:
		get=get_student()
	elif status==4:
		get=get_teacher()
	else:
		print("Enter Valid status!")
		
status=int(input("Enter 1 for student detail\nEnter 2 for Teacher detail\nEnter 3 to get student detail\nEnter 4 to get Teacher detail"))
check_status(status)


print("test dummy")