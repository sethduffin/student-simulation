from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
from data import get_name
import extensions
import os,sys

# --- Settings ---
implicit_wait = 3
sleep_modifier = 1 # Keep this for acurate rates
question_count = 26

class rate: # Rate per student in minutes
	create = 0.3
	delete = 0.1
	simulate = 1

def sleep(num):
	time.sleep(num*sleep_modifier)

driver = None
action = None

class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    stop = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

info = {}

def error(message=None):
	print()
	print()
	print("%s%s: %s, %s:%s%s" % (color.red,sys.exc_info()[0].__name__, sys.exc_info()[1], os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename), sys.exc_info()[2].tb_lineno,color.stop))
	if message:
		print(color.red+message+color.stop)
	print()
	print()
	input(' -- Enter --')
	driver.quit()
	quit()

def state(message):
	print(message,flush=True,end='')

def bar(part,whole):
	status = str(part)+'/'+str(whole)
	width, height = os.get_terminal_size(0)
	width = int(int(width-10)/2)-len(status)
	prog = int(float(part/whole)*width)
	fin = '='*prog
	unf	= ' '*int(width-prog)
	state('\b'*int(width*2))
	state('[%s%s] %s' % (fin,unf,status))

def login(username,password):
	driver.find("name","pseudonym_session[unique_id]").clear()
	driver.find("name","pseudonym_session[password]").clear()
	driver.find("name","pseudonym_session[unique_id]").send_keys(username)
	driver.find("name","pseudonym_session[password]").send_keys(password)
	driver.find("class","Button--login")[0].click()
def logout():
	driver.find('id','global_nav_profile_link').click()
	sleep(0.5)
	driver.find('xpath','/html/body/div[3]/span/span/div/div/div/div/div/span/form/button').click()
	try:
		alert = driver.switch_to.alert
		alert.accept()
	except:
		pass
def get_info():
	from data import load_saved,save_info
	global info

	info = load_saved()
	used_save = info.admin.username != None

	print()
	os.system('clear')
	print(color.bold+'INFO'+color.stop)
	info_template = {
		1:[' '+color.underline+'Admin'+color.stop,'u'],
		2:['   > Username: ', 'info.admin.username'],
		3:['   > Password: ', 'info.admin.password'],
		4:['   > Email: ', 'info.admin.email'],
		5:[' '+color.underline+'Courses'+color.stop+' - Number of Courses: ', 'c'],
		6:[' '+color.underline+'Students'+color.stop, 'u'],
		7:['   > Username Template: ', 'info.students.username'],
		8:['   > Password: ', 'info.students.password'],
		9:['   > Ammount: ', 'info.students.ammount'],
	}

	for num,li in info_template.items():
		key = li[0] 
		ref = li[1] 

		if ref == 'u':
			print(key)
		elif ref == 'c':
			if info.courses == {}:
				info.course_count = int(input(key))
				for i in range(info.course_count):
					i += 1
					print('   > Course #%s ' % i)
					url = input('     > Url: ')
					name = input('     > Assignment Name: ')
					info.courses[url] = name
			else:
				print(key+str(info.course_count))
				i = 1
				for url,name in info.courses.items():
					print('   > Course #%s ' % i)
					print('     > Url: '+url)
					print('     > Assignment Name: '+name)
					i += 1

		else:
			value = eval(ref)
			if value != None:
				print(key+str(value))
			elif value == None and not key == '   > Ammount: ':
				exec(ref+'= "'+input(key)+'"')
			elif key == '   > Ammount: ' :
				if info.students.keys == None:
					if info.students.ammount == None:
						resp = input(key)
						if resp == 'e':
							key = input('   > Exact Key: ')
							info.students.keys = [key]
						else:
							exec(ref+'='+resp)
							info.students.keys = list(range(1,info.students.ammount+1))
				else:
					info.students.ammount = len(info.students.keys)
					print(key+str(info.students.ammount))

	#print('keys:',info.students.keys)
	print()
	if used_save:
		if not input(color.yellow+'Confirm [Y/N] '+color.stop) in ['Y','y','yes','Yes']:
			get_info()
	else:
		if input(color.yellow+'Do you want to save info? '+color.stop) in ['Y','y','yes','Yes']:
			save_info(info)
	print()

def create_student(name,username,password,email,courses):
	driver.get("https://atomicjolt.instructure.com/accounts/1")
	driver.find('text','People').click()
	driver.find('aria-label','Add people').click()
	driver.find('xpath','/html/body/span/span/form/div[2]/fieldset/span/span/span/span/span/span/span[1]/label/span/span[1]/span[2]/span/input').send(name)
	driver.find('xpath','/html/body/span[1]/span/form/div[2]/fieldset/span/span/span/span/span/span/span[4]/label/span/span/span[2]/span/input').send(email)
	driver.find('xpath','/html/body/span[1]/span/form/div[2]/fieldset/span/span/span/span/span/span/span[5]/label/span/span/span[2]/span/input').send(username)
	driver.find('text+','Email the user about this account creation').click()
	driver.find('text+','Add User').up().click()
	sleep(0.5)
	if len(driver.find('class','ic-flash-error',True)) > 0:
		error('The student prefix has already been used, try again')
	sleep(1)
	driver.find('placeholder','Search people...').send_keys(email)
	sleep(1)
	driver.find('data-automation','users list').find('tag','tr',True)[0].find('tag','a',True)[0].click()
	sleep(1)
	driver.find('text+','Add Login').click()
	driver.find('id','pseudonym_unique_id').send_keys(username)
	driver.find('id','pseudonym_password').send_keys(password)
	driver.find('id','pseudonym_password_confirmation').send_keys(password)
	driver.switch_to.active_element.send_keys(Keys.ENTER)
	sleep(2)
	driver.find('id','right-side-wrapper').delete()
	sleep(1)
	driver.find('id','login_information').find('class','delete_pseudonym_link',True)[0].click()
	Alert(driver).accept()
	for course,assignment in courses.items():
		driver.get(course)
		driver.find('text','People').click()
		sleep(1)
		driver.find('id','addUsers').click()
		sleep(1)
		driver.find('text+','Login ID',True)[1].click()
		sleep(1)
		driver.find('tag','textarea').send_keys(username)
		driver.find('id','addpeople_next').click()
		sleep(1)
		driver.find('id','addpeople_next').click()
		sleep(1)

def delete_students(username):
	driver.get("https://atomicjolt.instructure.com/accounts/1")
	driver.find('text','People').click()
	while True:
		driver.find('placeholder','Search people...').send_keys(username)
		time.sleep(2)
		try:
			driver.find('data-automation','users list').find('tag','tr',True)[0].find('tag','a',True)[0].click()
		except:
			break
		sleep(1)
		driver.find('text','Delete from Atomic Jolt').click()
		sleep(1)
		driver.find('class','btn-primary').click()
		sleep(1)

def simulate_student(username,password,courses):
	import questions
	driver.get('https://atomicjolt.instructure.com/')
	login(username,password)
	try:
		driver.implicitly_wait(1)
		sleep(1)
		driver.find('name','user[terms_of_use]').click()
		driver.implicitly_wait(implicit_wait)
		driver.find('class','Button--primary').click()
		sleep(1)
		for button in driver.find('name','accept',True):
			driver.find('name','accept',True)[0].click()
			driver.get('https://atomicjolt.instructure.com/')
	except Exception as e:
		driver.implicitly_wait(implicit_wait)
	for course,assignment in courses.items():
		driver.get(course)
		driver.find('text','Assignments').click()
		driver.find('text*',assignment,True)[0].click()
		# sleep(10)
		driver.switch_to.frame(1)
		driver.implicitly_wait(10)
		try:
			driver.find('class','start-test-btn').click()
		except:
			pass
		driver.implicitly_wait(implicit_wait)
		sleep(1)
		questions.simulate()
		driver.switch_to.default_content()
	logout()

def get_action():
	print()
	os.system('clear')
	print(color.bold+'ACTION'+color.stop)
	print(' 1) '+color.underline+'Batch Create Students'+color.stop)
	print('     > Creates students with names like %s[1]' % (info.students.username))
	print(' 2) '+color.underline+'Batch Delete Students'+color.stop)
	print('     > Deletes all students starting with %s' % (info.students.username))
	print(' 3) '+color.underline+'Simulate Student Activity'+color.stop)
	print('     > Generate student attempts')
	print(' 4) '+color.underline+'Quit'+color.stop)

	print()

	try:
		choice = int(input(color.yellow+'Action #: '+color.stop))
	except:
		quit()	

	if choice == 2:
		print(color.red+'Are you sure? This will delete every user starting with:%s \n%s%s' % (color.yellow,info.students.username,color.stop))
		if not input('[Y/N]: ') in ['Y','Yes','y','yes']:
			quit()
	print()
	return choice

def run(choice):
	global driver,action

	opt = Options()

	opt.add_experimental_option("prefs", { \
		"profile.default_content_setting_values.media_stream_mic": 1, 
		# "profile.default_content_setting_values.media_stream_camera": 1,
		# "profile.default_content_setting_values.geolocation": 1, 
		# "profile.default_content_setting_values.notifications": 1 
	})

	driver = webdriver.Chrome(chrome_options=opt)
	action = ActionChains(driver)
	driver.implicitly_wait(implicit_wait)

	extensions.set_driver(driver,action)

	try:
		do(choice)
	except Exception as e:
		error()

	driver.quit()

def do(choice):
	print()
	os.system('clear')
	if choice == 1:
		print('Creating Students (%s min)' % (rate.create*info.students.ammount*info.course_count))
		bar(0,info.students.ammount)
		driver.get("https://atomicjolt.instructure.com/login/canvas")
		login(info.admin.username,info.admin.password)
		for i,num in enumerate(info.students.keys):
			na = get_name()
			un = info.students.username+'['+str(num)+']'
			pw = info.students.password
			e = info.admin.email.split('@')
			em = e[0]+'+'+un+'@'+e[1]
			co = info.courses
			create_student(na,un,pw,em,co)
			bar(i+1,info.students.ammount)
		logout()
		print()
		print()

	if choice == 2:
		print('Deleting Students (%s min)' % (rate.delete*info.students.ammount))
		driver.get("https://atomicjolt.instructure.com/login/canvas")
		login(info.admin.username,info.admin.password)
		delete_students(info.students.username)
		logout()

	if choice == 3:
		print('Simulating Student Activity (%s min)' % (rate.simulate*info.students.ammount*info.course_count))
		bar(0,info.students.ammount)
		for i,num in enumerate(info.students.keys):
			un = info.students.username+'['+str(num)+']'
			pw = info.students.password
			co = info.courses
			simulate_student(un,pw,co)
			bar(i+1,info.students.ammount)
		print()
		print()
	