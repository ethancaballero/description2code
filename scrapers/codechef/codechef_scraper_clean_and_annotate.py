# -*- coding: utf-8 -*-
import shutil
import os
import re
import requests
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import html2text
import time
import argparse
import concurrent.futures

def escape_lt(html):
    html_list = list(html)
    for index in xrange(0, len(html) - 1):
        if html_list[index] == '<' and html_list[index + 1] == ' ':
            html_list[index] = '&lt;'
    return ''.join(html_list)

'''not sure if this one makes sense'''
def escape_gt(html):
    html_list = list(html)
    for index in xrange(0, len(html) - 1):
        if html_list[index] == ' ' and html_list[index + 1] == '>':
            html_list[index + 1] = '&gt;'
    return ''.join(html_list)

def get_problem_list(url):
	page = requests.get(url)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	soup = BeautifulSoup(html_content, "html.parser")

	messages = []

	text = soup.select("body a")

	for row in text:
		message = ""
		raw = str(row)
		body = re.search('/submit/(.*)" t', raw)

		if body != None:
			w = body.group(1)
			message = str(w)
			if message != 'easy' and message != 'medium' and message != 'hard' and message != 'challenge' and message != 'extcontest' and message != 'school':
				messages.append(message)

	return messages

def get_solution_ids(name, language):

	if language == 'python':
		url = 'https://www.codechef.com/status/%s?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)
		url2 = 'https://www.codechef.com/status/%s?page=1&sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)
	elif language == 'c++':
		url = 'https://www.codechef.com/status/%s?sort_by=All&sorting_order=asc&language=41&status=15&handle=&Submit=GO' % (name)
		url2 = 'https://www.codechef.com/status/%s?page=1&sort_by=All&sorting_order=asc&language=41&status=15&handle=&Submit=GO' % (name)
	else:
		pass

	page1 = requests.get(url)
	if str(page1) == "<Response [503]>":
		while str(page1) == "<Response [503]>":
			time.sleep(1)
			page1 = requests.get(url)

	page2 = requests.get(url2)
	if str(page2) == "<Response [503]>":
		while str(page2) == "<Response [503]>":
			time.sleep(1)
			page2 = requests.get(url2)

	if re.search("<div align='center' class='pageinfo'>", page1.text) == None:
		html_content = page1.text
	else:
		html_content = page1.text + page2.text

	messages = []

	print url
 
	solution_id = re.findall("href='/viewsolution/(.+?)' target='_blank'>View", html_content)
	pts = re.findall("/>\\[(.+?)pts\\]<", html_content)

	#'''
	print solution_id
	print pts
	print len(pts)
	print len(solution_id)
	#'''

	if len(pts) != 0 and len(solution_id) != 0:

		for i in range(len(pts)):
			if str(pts[i]) == '100':
				messages.append(str(solution_id[i]))

	elif len(pts) == 0 and len(solution_id) != 0:
		for i in range(len(solution_id)):
			messages.append(str(solution_id[i]))
	else:
		pass

	print len(messages)

	return messages

def get_description(i):
	descriptions = []
	left_out = []
	failed_to_download_d = []

	print i

	url = "https://www.codechef.com/api/contests/PRACTICE/problems/" + str(i)

	page = requests.get(url)

	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)

	html_content = page.text

	if re.search('"message":"requests limit exhausted"', html_content) != None:
		while re.search('message":"requests limit exhausted', html_content) != None:
			time.sleep(1)
			page = requests.get(url)
			html_content = page.text



	if html_content==None:
		failed_to_download_d.append(i)



	if re.search('src="https://s3.amazonaws.com/codechef_shared/download/upload', html_content.replace("\\", "")) == None and re.search('src="/download/extimages', html_content.replace("\\", "")) == None and re.search('"message":"Problem is not visible now. Please try again later."', html_content) == None:

		#first_clean = page.json()['body'].replace("<sup>", "<sup>^").replace(" <=", u" ≤").replace(" >=", u" ≥").replace("<=", u" ≤ ").replace(">=", u" ≥ ").replace(u"≤  ", u"≤ ").replace(u"≥  ", u"≥ ").replace("<h3>", "<h3>\n")
		first_clean = page.json()['body'].replace("<sup>", "<sup>^").replace(" <=", u" ≤").replace(" >=", u" ≥").replace("<=", u" ≤ ").replace(">=", u" ≥ ").replace(u"≤  ", u"≤ ").replace(u"≥  ", u"≥ ").replace("<h3>", "<h3>\n").replace("<b>", u'†').replace("</b>", u'‡')

		keep_lt = escape_lt(first_clean)

		#second_clean = keep_lt
		#'''
		second_clean = escape_gt(keep_lt)
		#'''

		body = BeautifulSoup(second_clean).get_text()

		w = body
		w = w.replace("\nAll submissions for this problem are available.", "")
		w = w.replace("All submissions for this problem are available.", "")

		w = re.sub('\n Read problems statements in (.+?)\n', '', w, re.M)
		w = re.sub('\nRead problems statements in (.+?)\n', '', w, re.M)
		w = re.sub(' Read problems statements in (.+?)\n', '', w, re.M)
		w = re.sub('Read problems statements in (.+?)\n', '', w, re.M)
		
		w = re.sub('Subtask(.+?)Example', 'Example', w, flags=re.M|re.S)

		w = w.replace("\u003C","<")
		w = w.replace("\u003E",">")

		raw = w

		raw = raw.replace(u"†Input† :", "Input")
		raw = raw.replace(u"†Input :†", "Input")
		raw = raw.replace(u"†Input†", "Input")
		raw = raw.replace(u"†Output† :", "Output")
		raw = raw.replace(u"†Output :†", "Output")
		raw = raw.replace(u"†Output†", "Output")
		raw = raw.replace(u"†Constraints† :", "Constraints")
		raw = raw.replace(u"†Constraints :†", "Constraints")
		raw = raw.replace(u"†Constraints†", "Constraints")
		raw = raw.replace(u"†Input:‡", "Input:")
		raw = raw.replace(u"†Output:‡", "Output:")

		raw = raw.replace(u"†For help on this problem, please check out our tutorial Input and Output (I/O)‡\n", '')

		raw = raw.replace(u"†Example case 1.‡", "Example case 1.")
		raw = raw.replace(u"†Example case 2.‡", "Example case 2.")
		raw = raw.replace(u"†Example case 3.‡", "Example case 3.")
		raw = raw.replace(u"†Example case 4.‡", "Example case 4.")
		raw = raw.replace(u"†Example case 5.‡", "Example case 5.")

		w = raw

		w = w.replace("\\","\\\\")

		descriptions.append(w.encode('utf-8').decode('string-escape'))
	else:
		left_out.append(i)

	return descriptions, left_out, failed_to_download_d

def get_solutions(solution_ids):
	solutions = {}
	failed_to_download_s = []
	with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
		future_to_url = {executor.submit(get_solution, i): i for i in solution_ids}
		for future in concurrent.futures.as_completed(future_to_url):
			data = future.result()

			if data[2] == None:
				solutions[data[0]] = data[1]

	return solutions

def get_solution(solution_id):
	#solutions = []
	#failed_to_download_s = []
	#for i in solution_ids:
	failed_to_download = None
	url = "https://www.codechef.com/viewplaintext/" + str(solution_id)
	
	page = requests.get(url)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	'''
	if html_content==None:
		failed_to_download = solution_id
		'''

	text = BeautifulSoup(html_content, "html.parser").get_text()

	#'''figure out if escape_lt needs to go here'''

	print len(text)
	#print text


	failed_to_download = None
	solution = None

	#print text
	if len(text)==0 or re.search('var _sf_startpt = (new Date()).getTime()', text) != None:
		failed_to_download = solution_id
	else:
		text = text.replace("\\","\\\\")
		solution = text.encode('utf-8').decode('string-escape')

	return solution_id, solution, failed_to_download



def download_all_challenge_names(filename):
	target = open(filename, 'w')

	problems = get_problem_list("https://www.codechef.com/problems/school/?sort_by=SuccessfulSubmission&sorting_order=desc")

	#print problems

	target.write(str("\neasy\n"))
	target.write(str(problems))

	#'''
	problems = get_problem_list("https://www.codechef.com/problems/easy/?sort_by=SuccessfulSubmission&sorting_order=desc")

	target.write(str("\nmedium\n"))
	target.write(str(problems))

	problems = get_problem_list("https://www.codechef.com/problems/medium/?sort_by=SuccessfulSubmission&sorting_order=desc")

	target.write(str("\nhard\n"))
	target.write(str(problems))

	problems = get_problem_list("https://www.codechef.com/problems/hard/?sort_by=SuccessfulSubmission&sorting_order=desc")

	target.write(str("\nharder\n"))
	target.write(str(problems))

	problems = get_problem_list("https://www.codechef.com/problems/challenge/?sort_by=SuccessfulSubmission&sorting_order=desc")

	target.write(str("\nhardest\n"))
	target.write(str(problems))

	problems = get_problem_list("https://www.codechef.com/problems/extcontest/?sort_by=SuccessfulSubmission&sorting_order=desc")

	target.write(str("\nexternal\n"))
	target.write(str(problems))
	#'''

#download_all_challenge_names('codechef_problem_names.txt')

#def download_descriptions_solutions(filename, index_n):
def download_descriptions_annotated(filename, index_n):
	#root_dir = 'codechef_alter_data'
	#root_dir = 'codechef_data_currently'
	root_dir = 'codechef'

	file = open(filename, 'r')
	f = open(filename, 'r')

	index_n_int = int(index_n)

	start = index_n_int + (500*index_n_int)
	end = start + 499

	print "start"
	print start

	print "end"
	print end 



	easy = []
	medium = []
	hard = []
	harder = []
	hardest = []
	external = []

	g = ""
	i=0
	for line in f:
		if str(line).find('type=') != -1:
			body = re.search('type=(.*)', line)
			g = body.group(1)
		else:
			if str(g) == "easy":
				easy = eval(line)
			elif str(g) == "medium":
				medium = eval(line)
			elif str(g) == "hard":
				hard = eval(line)
			elif str(g) == "harder":
				harder = eval(line)
			elif str(g) == "hardest":
				hardest = eval(line)
			elif str(g) == "external":
				external = eval(line)
			else:
				pass

	all_names = []
	all_names_p = []
	all_names =[["easy", easy], ["medium", medium], ["hard", hard], ["harder", harder], ["hardest", hardest], ["external", external]]
	
	#all_names =[["external", external]]

	already_scraped = []

	'''
	for ndx, n in enumerate(all_names_before[0][1]):
		if n not in already_scraped:
			all_names_p.append(n)
			'''

	print "all_names"
	#print all_names_p
	print len(all_names_p)

	for ndx, n in enumerate(all_names):
		category = all_names[ndx][0]
		problem_list = all_names[ndx][1]
		language = ["python", "c++"]

		for idx, i in enumerate(problem_list):
		#for idx, i in enumerate(['ACDEMY']):
			descriptions, left_out, failed_to_download_d = get_description(i)

			if i not in left_out:

				if not os.path.exists(root_dir):
				    os.makedirs(root_dir)

				cat_dir = root_dir + "/" + category

				if not os.path.exists(cat_dir):
				    os.makedirs(cat_dir)

				save_dir = cat_dir + "/" + i

				if not os.path.exists(save_dir):
					os.makedirs(save_dir)

				description_dir = save_dir + "/description"

				if os.path.exists(description_dir):
				    #os.makedirs(description_dir)

					description_file_path = description_dir + "/description_annotated.txt"
					description_file = open(description_file_path, 'w')
					description_file.write(str(descriptions[0]))


				'''
				ids_l = []
				for l in language:
					ids = get_solution_ids(i, l)
					ids_l.append(ids)

					print ids
					#solutions, failed_to_download_s = get_solutions(ids)
					solutions = get_solutions(ids)
					#print failed_to_download_s

					solution_dir = save_dir + "/solutions_" + l

					if not os.path.exists(solution_dir):
					    os.makedirs(solution_dir)

					#print solutions

					for jdx, j in enumerate(solutions):
						#print len(solutions[j])
						if len(solutions[j]) < 10000:
							#print jdx
							solution_file_path = solution_dir + "/" + j + ".txt"
							solution_file = open(solution_file_path, 'w')
							solution_file.write(solutions[j])

				#remove problems with zero solutions
				if len(ids_l[0]) == 0 and len(ids_l[1]) == 0:
					shutil.rmtree(save_dir)

			#url = 'https://www.codechef.com/status/%d?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)
			#'''

	#'''
	print "Finished download process"
	if len(failed_to_download) > 0:
		print "Following challenges failed to download: " + str(failed_to_download)
		#'''


#download_all_challenge_names('codechef_problem_names.txt')	
parser = argparse.ArgumentParser()
parser.add_argument('--index', type=str, default="index", help='')
args = parser.parse_args()

index_n = args.index

#get_description('INTEX1')
#print get_description('SNAKGAME')[0][0]
#a = get_description('INTEX1')
#print a[0][0]
'''
download_descriptions_solutions('codechef_problem_names.txt', index_n)
#'''

'''
download_descriptions_solutions('codechef_problem_names_left.txt', index_n)
#'''

#'''
download_descriptions_annotated('codechef_problem_names.txt', index_n)
#'''

#get_solutions(['10610556'])
#print get_solution_ids('FIBQ', 'c++')
#print get_solution_ids('CIELAB', 'c++')



#download_descriptions_solutions('codechef_problem_names_easy.txt')
#download_descriptions_solutions('codechef_problem_names_easy_short.txt')






