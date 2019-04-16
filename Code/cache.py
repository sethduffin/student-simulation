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
	class demo_1:
		course_count = 2
		courses = {'https://atomicjolt.instructure.com/courses/2334': 'Quiz A', 'https://atomicjolt.instructure.com/courses/2342': 'Quiz B'}
		class admin:
			username = "sd_admin"
			password = "testing123"
			email = "seth.duffin@atomicjolt.com"
		class students:
			username = "sd_demo_student_a"
			password = "testing123"
			ammount = 3
			keys = [1, 2, 3]