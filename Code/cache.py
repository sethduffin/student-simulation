class saved:
	class TEMPLATE:
		course_count = None
		courses = {}
		class admin:
			username = None
			password = None
			email = None
		class students:
			username = None
			password = None
			ammount = None
			keys = None
	class sd_demo_stud_a:
		course_count = 1
		courses = {'https://atomicjolt.instructure.com/courses/4054': 'Student Simulation'}
		class admin:
			username = "sd_admin"
			password = "testing123"
			email = "seth.duffin@atomicjolt.com"
		class students:
			username = "sd_demo_stud_b"
			password = "testing123"
			ammount = 2
			keys = [2,3,4,5]
	class example_student_a:
		course_count = 1
		courses = {'https://atomicjolt.instructure.com/courses/3517': 'FINAL EXAM'}
		class admin:
			username = "sd_admin"
			password = "testing123"
			email = "seth.duffin@atomicjolt.com"
		class students:
			username = "example_student_a"
			password = "testing123"
			ammount = 20
			keys = [ 13, 15, 16, 17, 18, 19, 20, 21]