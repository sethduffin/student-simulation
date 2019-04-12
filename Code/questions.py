from main import *
from random import randint,choice

page = None

def simulate():
	total = list(range(1,question_count+1))
	t = randint(0,question_count)
	f = question_count - t

	form = {}

	for i in range(t):
		num = choice(total)
		total.remove(num)
		form[num] = True
	for i in range(f):
		num = choice(total)
		total.remove(num)
		form[num] = False

	form = dict(sorted(form.items()))

	take(form)

def math_box(key,text,hold=False):
	math = page.find("mathquill-block-id",key)
	math.click()
	action.send_keys(text).do()
	if not hold:
		sleep(0.3)
		page.find('class','lrn_stimulus_content',True)[0].click()
	sleep(0.3)

def take(questions):
	for question,value in questions.items():
		if driver.find('class','current-item-pos').text != str(question):
			item_num = str(question-1)
			page_button = driver.find('class','slides-vertical-pagination').find('xpath','./li[@data-index="'+item_num+'"]').find('tag','button')
			action.move_to_element(page_button).do()
			page_button.click()
		sleep(0.2)
		global page
		page = driver.find("xpath","//*[@id=\"learnosity_assess\"]/div/div[3]/div[1]/div/div[2]/div["+str(question)+"]")
		eval('attempts.q'+str(question))(value)
		sleep(0.2)

	question = question_count
	if driver.find('class','current-item-pos').text != str(question):
		item_num = str(question-1)
		page_button = driver.find('class','slides-vertical-pagination').find('xpath','./li[@data-index="'+item_num+'"]').find('tag','button')
		action.move_to_element(page_button).do()
		page_button.click()
	driver.find('class','test-submit').click()
	driver.implicitly_wait(15)
	driver.find('text~','Date Completed').flag()	
	driver.implicitly_wait(implicit_wait)

class attempts:
	def q1(correct):
		try:
			if correct:
				page.find('text+','Violet').click()
			if not correct:
				page.find('text+','Blue').click()
		except:
			error()

	def q2(correct):
		if correct:
			page.find('text~','Red').click()
		if not correct:
			page.find('text+','Green').click()

	def q3(correct):
		if correct:
			page.find('text+','Baton Rouge, LA').click()
			page.find('text+','Olympia, WA').click()
		if not correct:
			page.find('text+','Houston, TX').click()

	def q4(correct):
		if correct:
			tof = [1,0,1]
		if not correct:
			tof = [0,1,0]
		for i,box in enumerate(page.find('class','lrn_choicematrix_type_table').find('tag','tbody',True)):
			box.find('data-colno',str(tof[i])).click()

	def q5(correct):
		if correct:
			math_box('1','3+3+4x')
		if not correct:
			math_box('1','8+2+18x')

	def q6(correct):
		if correct:
			math_box('77','m')
			math_box('83','2')
		if not correct:
			math_box('77','t')
			math_box('83','4')

	def q7(correct):
		if correct:
			math_box("95","y",True)
			action.key_down(Keys.SHIFT).send_keys("6").key_up(Keys.SHIFT).do()
			sleep(0.5)
			action.send_keys("2").do()
			math_box("95","")
			math_box("100","3x")
		if not correct:
			math_box("95","7t")
			math_box("100","4w")

	def q8(correct):
		if correct:
			math_box("113",'40')
		if not correct:
			math_box("113",'20')

	def q9(correct):
		if correct:
			math_box("121","87.7° F")
		if not correct:
			math_box("121","90° F")

	def q10(correct):
		if correct:
			math_box("127","3")
			math_box("132","2")
		if not correct:
			math_box("127","4")
			math_box("132","2")

	def q11(correct):
		if correct:
			math_box("134","0.005km")
		if not correct:
			math_box("134","1.3km")

	def q12(correct):
		ids = [187,191,195,199]
		if correct:
			values = [9,7,4,6]
		if not correct:
			values = [3,3,3,3]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q13(correct):
		ids = [280,283,277]
		driver.find("class","lrn_float_element_container").delete()
		if correct:
			values = ["40","7.81±0.01","50"]
		if not correct:
			values = ["12","15","36"]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q14(correct):
		ids = [296,308]
		if correct:
			values = ["a","20"]
		if not correct:
			values = ["18","13"]
		for i,val in enumerate(values):
			math_box(str(ids[i]),str(val))

	def q15(correct):
		if correct:
			order = [3,0,2,1]
		if not correct:
			order = [2,1,0,3]
		for i,val in enumerate(order):
			page.find('class','lrn_possibilityList').find('data-index',str(val)).click()
			page.find('class','lrn_response_input').find('data-inputid',str(i)).click()

	def q16(correct):
		if correct:
			order = [
			"North America",
			"South America",
			"Asia",
			"Africa",
			"Australia",
			"Europe",
			"Antartica",
			]
		if not correct:
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
			page.find('text~',str(val)).click()
			page.find('class','lrn_response_input').find('data-inputid',str(i)).click()

	def q17(correct):
		try:
			if correct:
				order = [1,4,9]
			if not correct:
				order = [9,1,4]
			for i,val in enumerate(order):
				page.find('class','lrn_possibilityList').find('text~',str(val)).click()
				page.find('class','lrn_response_input').find('data-inputid',str(i)).click()
		except Exception as e:
			error(e)

	def q18(correct):
		if correct:
			values = [
			"backwaters",
			"Western",
			"ninety-eight",
			"primitive",
			"digital watches"
			]
		if not correct:
			values = [
			"seth",
			"is",
			"really",
			"super",
			"cool"
			]
		for i,val in enumerate(values):
			page.find('data-inputid',str(i)).send_keys(val)

	def q19(correct):
		if correct:
			values = [
			"Nevada",
			"South Dakota",
			"Alabama",
			]
		if not correct:
			values = [
			"Utah",
			"North Dakota",
			"Georgia",
			]
		for i,val in enumerate(values):
			page.find('data-inputid',str(i)).find("text~",val).click()

	def q20(correct):
		if correct:
			order = [
			"F. Scott Fitzgerald",
			"Mark Twain",
			"C.S. Lewis",
			"Herman Melville",
			"Jane Austen",
			"C.S. Lewis",
			]
		if not correct:
			order = [
			"C.S. Lewis",
			"F. Scott Fitzgerald",
			"Mark Twain",
			"C.S. Lewis",
			"Herman Melville",
			"Jane Austen",
			]
		for i,val in enumerate(order):
			page.find('class','lrn_possibilityList').find('text~',str(val)).click()
			page.find('class','lrn_response_input').find('data-inputid',str(i)).click()

	def q21(correct):
		if correct:
			order = [2,0,1,3]
		if not correct:
			order = [3,1,2,0]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val)).click()
			page.find('class','lrn_sort_block',True)[i].click()

	def q22(correct):
		if correct:
			order = [4,2,1,0,3]
		if not correct:
			order = [0,1,2,3,4]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val)).click()
			page.find('class','lrn_sort_block',True)[i].click()

	def q23(correct):
		if correct:
			order = [3,0,1,7,6,4,2,5]
		if not correct:
			order = [0,1,2,3,4,5,6,7]
		for i,val in enumerate(order):
			page.find('class','lrn-dragdrop-container').find('data-response-index',str(val)).click()
			page.find('class','lrn_sortable',True)[i].click()

	# def q24(correct):
	# 	if correct:
	# 		page.find('class','lrn_start_recording').click()
	# 	if not correct:
	# 		pass

	# def q25(correct):
	# 	if correct:
	# 		page.find('class','lrn_paintable').click()
	# 	if not correct:
	# 		pass

	def q24(correct):
		if correct:
			for elem in page.find("data-row","1",True):
				elem.click()
		if not correct:
			page.find("data-row","1",True)[0].click()

	def q25(correct):
		if correct:
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
		if not correct:
			words = ['age','of','Heaven']
		for word in words:
			driver.find('class','lrn_tokenhighlight_text').find('text~',word,True)[0].click()

	# def q28(correct):
	# 	return
	# 	try:
	# 		if correct:
	# 			values = [8,9,10]
	# 		if not correct:
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

	# def q29(correct):
	# 	return
	# 	if correct:
	# 		pass
	# 	if not correct:
	# 		pass

	def q26(correct):
		if correct:
			page.find('tag','input').send_keys('7')
		if not correct:
			page.find('tag','input').send_keys('50')



	

	
	