from main import *
from random import randint,choice

page = None

def simulate():
	total = list(range(1,question_count+1))
	c = randint(0,question_count)
	i = question_count-c

	form = {}

	partials = [3,4,13,15,16,17,18,19,20,21,22,23,24,25]

	for letter in ['c','i']:
		for key in range(eval(letter)):
			num = choice(total)
			total.remove(num)
			if num in partials and choice([True, False]):
				form[num] = 'p'
			else:
				form[num] = letter

	form = dict(sorted(form.items()))

	# for key,value in form.items():
	# 	if value == 'c':
	# 		print(color.green+str(key)+': '+value+color.stop)
	# 	if value == 'p':
	# 		print(color.blue+str(key)+': '+value+color.stop)
	# 	if value == 'i':
	# 		print(color.red+str(key)+': '+value+color.stop)
	# input()
	# return

	take(form)

def math_box(key,text,hold=False):
	temp_action = ActionChains(driver)
	math = page.find("mathquill-block-id",key)
	math.click()
	temp_action.send_keys(text).perform()
	temp_action.reset_actions()
	if not hold:
		sleep(0.3)
		try:
			page.find('class','lrn_stimulus_content',True)[0].click()
		except:
			driver.find('tag','body').click()
	sleep(0.3)

def take(questions):
	for question,value in questions.items():
		temp_action = ActionChains(driver)
		if driver.find('class','current-item-pos').text != str(question):
			item_num = str(question-1)
			page_button = driver.find('class','slides-vertical-pagination').find('xpath','./li[@data-index="'+item_num+'"]').find('tag','a')
			temp_action.move_to_element(page_button).do()
			page_button.click()
		sleep(0.2)
		global page
		page = driver.find("xpath","//*[@class=\"slides-control\"]/div["+str(question)+"]")
		try:
			eval('attempts.q'+str(question))(value)
		except Exception as e:
			print()
			print('While answering question %s' % (question))
			error()
		sleep(0.2)

	question = question_count
	if driver.find('class','current-item-pos').text != str(question):
		temp_action = ActionChains(driver)
		item_num = str(question-1)
		page_button = driver.find('class','slides-vertical-pagination').find('xpath','./li[@data-index="'+item_num+'"]').find('tag','a')
		temp_action.move_to_element(page_button).do()
		page_button.click()
	driver.find('class','test-submit').click()
	driver.implicitly_wait(15)
	driver.find('text~','Date Completed').flag()	
	driver.implicitly_wait(implicit_wait)

class attempts:
	def q1(state):
		try:
			if state == 'c':
				page.find('text+','Violet')[0].click()
			elif state == 'i':
				page.find('text+','Blue')[0].click()
		except:
			error()

	def q2(state):
		if state == 'c':
			page.find('text~','Red')[0].click()
		elif state == 'i':
			page.find('text+','Green')[0].click()

	def q3(state):
		if state == 'c':
			page.find('text+','Baton Rouge, LA')[0].click()
			page.find('text+','Olympia, WA')[0].click()
		elif state == 'p':
			page.find('text+','Houston, TX')[0].click()
			page.find('text+','Olympia, WA')[0].click()
		elif state == 'i':
			page.find('text+','Houston, TX')[0].click()

	def q4(state):
		if state == 'c':
			tof = [1,0,1]
		elif state == 'p':
			tof = [1,1,1]
		elif state == 'i':
			tof = [0,1,0]
		for i,box in enumerate(page.find('class','lrn_choicematrix_type_table').find('tag','tbody').find('tag','tr')):
			box.find('data-colno',str(tof[i])).click()

	def q5(state):
		if state == 'c':
			math_box('1','3+2+4x')
		elif state == 'i':
			math_box('1','8+2+18x')

	def q6(state):
		if state == 'c':
			math_box('77','m')
			math_box('83','2')
		elif state == 'i':
			math_box('77','t')
			math_box('83','4')

	def q7(state):
		if state == 'c':
			math_box("95","y",True)
			action.key_down(Keys.SHIFT).send_keys("6").key_up(Keys.SHIFT).do()
			sleep(0.5)
			action.send_keys("2").do()
			math_box("95","")
			math_box("100","3x")
		elif state == 'i':
			math_box("95","7t")
			math_box("100","4w")

	def q8(state):
		if state == 'c':
			math_box("113",'40')
		elif state == 'i':
			math_box("113",'20')

	def q9(state):
		if state == 'c':
			math_box("121","87.7")
		elif state == 'i':
			math_box("121","90")

	def q10(state):
		if state == 'c':
			math_box("127","3")
			math_box("132","2")
		elif state == 'i':
			math_box("127","4")
			math_box("132","2")

	def q11(state):
		if state == 'c':
			math_box("134","0.005km")
		elif state == 'i':
			math_box("134","1.3km")

	def q12(state):
		ids = [187,191,195,199]
		if state == 'c':
			values = [9,7,4,6]
		elif state == 'i':
			values = [3,3,3,3]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q13(state):
		ids = [274,277,271]
		driver.find("class","lrn_float_element_container").delete()
		if state == 'c':
			values = ["40","7.81±0.01","50"]
		elif state == 'p':
			values = ["12","7.81±0.01","50"]
		elif state == 'i':
			values = ["12","15","36"]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q14(state):
		ids = [290,302]
		if state == 'c':
			values = ["a","20"]
		elif state == 'i':
			values = ["18","13"]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q15(state):
		if state == 'c':
			order = [3,0,2,1]
		elif state == 'p':
			order = [3,0,1,2]
		elif state == 'i':
			order = [2,1,0,3]
		for i,val in enumerate(order):
			page.find('class','lrn_possibilityList').find('data-index',str(val),True)[0].click()
			page.find('class','lrn_response_input').find('data-inputid',str(i),True)[0].click()

	def q16(state):
		if state == 'c':
			order = [
			"North America",
			"South America",
			"Asia",
			"Africa",
			"Australia",
			"Europe",
			"Antartica",
			]
		elif state == 'p':
			order = [
			"North America",
			"South America",
			"Asia",
			"Africa",
			"Europe",
			"Antartica",
			"Australia",
			]
		elif state == 'i':
			order = [
			"Antartica",
			"North America",
			"Europe",
			"South America",
			"Asia",
			"Australia",
			"Africa",
			]
		for i,val in enumerate(order):
			page.find('text~',str(val),True)[0].click()
			page.find('class','lrn_response_input').find('data-inputid',str(i),True)[0].click()

	def q17(state):
		try:
			if state == 'c':
				order = [1,4,9]
			elif state == 'p':
				order = [1,9,4]
			elif state == 'i':
				order = [9,1,4]
			for i,val in enumerate(order):
				page.find('class','lrn_possibilityList').find('text~',str(val),True)[0].click()
				page.find('class','lrn_response_input').find('data-inputid',str(i),True)[0].click()
		except Exception as e:
			error(e)

	def q18(state):
		if state == 'c':
			values = [
			"backwaters",
			"Western",
			"ninety-eight",
			"primitive",
			"digital watches"
			]
		elif state == 'p':
			values = [
			"backwaters",
			"Western",
			"primitive",
			"ninety-eight",
			"digital watches"
			]
		elif state == 'i':
			values = [
			"orange",
			"blue",
			"pink",
			"black",
			"green"
			]
		for i,val in enumerate(values):
			page.find('data-inputid',str(i)).send_keys(val)

	def q19(state):
		if state == 'c':
			values = [
			"Nevada",
			"South Dakota",
			"Alabama",
			]
		elif state == 'p':
			values = [
			"Nevada",
			"North Dakota",
			"Alabama",
			]
		elif state == 'i':
			values = [
			"Utah",
			"North Dakota",
			"Georgia",
			]
		for i,val in enumerate(values):
			page.find('data-inputid',str(i)).find("text~",val,True)[0].click()

	def q20(state):
		if state == 'c':
			order = [
			"F. Scott Fitzgerald",
			"Mark Twain",
			"C.S. Lewis",
			"Herman Melville",
			"Jane Austen",
			"C.S. Lewis",
			]
		elif state == 'p':
			order = [
			"F. Scott Fitzgerald",
			"Mark Twain",
			"C.S. Lewis",
			"Herman Melville",
			"C.S. Lewis",
			"Jane Austen",
			]
		elif state == 'i':
			order = [
			"C.S. Lewis",
			"F. Scott Fitzgerald",
			"Mark Twain",
			"C.S. Lewis",
			"Herman Melville",
			"Jane Austen",
			]
		for i,val in enumerate(order):
			page.find('class','lrn_possibilityList').find('text~',str(val),True)[0].click()
			page.find('class','lrn_response_input').find('data-inputid',str(i),True)[0].click()

	def q21(state):
		if state == 'c':
			order = [2,0,1,3]
		elif state == 'p':
			order = [3,0,1,2]
		elif state == 'i':
			order = [3,1,2,0]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val),True)[0].click()
			page.find('class','lrn_sort_block',True)[i].click()

	def q22(state):
		if state == 'c':
			order = [4,2,1,0,3]
		elif state == 'p':
			order = [2,4,1,0,3]
		elif state == 'i':
			order = [0,1,2,3,4]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val)).click()
			page.find('class','lrn_sort_block',True)[i].click()

	def q23(state):
		if state == 'c':
			order = [3,0,1,7,6,4,2,5]
		elif state == 'p':
			order = [7,0,1,3,6,4,2,5]
		elif state == 'i':
			order = [0,1,2,3,4,5,6,7]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val)).click()
			page.find('class','lrn_sortable',True)[i].click()

	# def q24(state):
	# 	if state == 'c':
	# 		page.find('class','lrn_start_recording').click()
	# 	elif state == 'i':
	# 		pass

	# def q25(state):
	# 	if state == 'c':
	# 		page.find('class','lrn_paintable').click()
	# 	elif state == 'i':
	# 		pass

	def q24(state):
		if state == 'c':
			for elem in page.find("data-row","1",True):
				elem.click()
		elif state == 'p':
			page.find("data-row","1",True)[0].click()
			page.find("data-row","1",True)[1].click()
		elif state == 'i':
			page.find("data-row","2",True)[0].click()

	def q25(state):
		if state == 'c':
			words = [
				'best', 
				'worst',
				'wisdom',
				'foolishness',
				'incredulity',
				'Light',
				'Darkness',
				'hope',
				'despair',
				'far',
				'noisiest',
				'good',
				'evil',
			]
		elif state == 'p':
			words = [
				'best', 
				'worst',
				'wisdom',
				'Light',
				'Darkness',
				'hope',
				'far',
				'evil',
			]
		elif state == 'i':
			words = ['age','of','Heaven']
		for word in words:
			driver.find('class','lrn_tokenhighlight_text').find('text~',word,True)[0].click()

	# def q28(state):
	# 	return
	# 	try:
	# 		if state == 'c':
	# 			values = [8,9,10]
	# 		elif state == 'i':
	# 			values = [4,3,2]
	# 		for i,val in enumerate(values):
	# 			circle = page.find('class','line-hover-circle',True)[i]
	# 			line = page.find('class','nv-y').find('text~',str(val))
	# 			print(line)
	# 			line.flag()
	# 			action.drag_and_drop(circle,line).do()
	# 		input('alrighty')
	# 	except:
	# 		error()

	# def q29(state):
	# 	return
	# 	if state == 'c':
	# 		pass
	# 	elif state == 'i':
	# 		pass

	def q26(state):
		if state == 'c':
			page.find('tag','input').send_keys('7')
		elif state == 'i':
			page.find('tag','input').send_keys('50')



	

	
	