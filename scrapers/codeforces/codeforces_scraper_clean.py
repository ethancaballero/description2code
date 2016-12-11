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

def sub_strip(matchobj):   
    return matchobj.group(0).replace(u"\u2009", "")

def get_problem_list(url):
	page = requests.get(url)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	soup = BeautifulSoup(html_content, "html.parser") # making soap

	messages = []

	text = soup.select("body a")

	for row in text:
		message = ""
		raw = str(row)
		body = re.search(' href="/problemset/problem/(.*)">', raw)

		if body != None:
			w = body.group(1)
			message = str(w)
			c = message.split('/')
			#if message != 'easy' and message != 'medium' and message != 'hard' and message != 'challenge' and message != 'extcontest' and message != 'school':
			#messages.append(message)
			messages.append(c)

	return messages

def get_solution_ids(name, language):
	print language
	
	'''IF IT'S BEEN A LONG TIME SINCE THE LAST TIME YOU USED THIS CODE, YOU NEED TO LOG IN AGAIN AND SEE WHAT CURRENT JSESSIONID AND 39ce7 ARE'''
	d = {'JSESSIONID': 'FBAAF89D197D7A5C7E95C536A7D31A7A-n1', '39ce7': 'CFtRZMGC'}
	#d = {'JSESSIONID': '77C3B36AE19BC9CE0B75529825DDB926-n1', '39ce7': 'CFh6GVF2'}

	#JSESSIONID=77C3B36AE19BC9CE0B75529825DDB926-n1; 39ce7=CFh6GVF2

	url = 'http://codeforces.com/problemset/status/' + name[0] + '/problem/' + name[1]

	#c = requests.get('http://codeforces.com/problemset/status/1/problem/A', cookies = d)
	c = requests.get(url, cookies = d)

	m = re.search('meta name="X-Csrf-Token" content="(.*)"', c.text)
	if not m:
		raise 'unable to get csrf token'

	csrf_token = m.groups(1)


	#'''
	if language == 'python':
		print "python_search"
		#c = requests.post("http://codeforces.com/problemset/status/1/problem/A", 
		c = requests.post(url,
		data = {'csrf_token':csrf_token, 'action':'setupSubmissionFilter', 'frameProblemIndex':'A', 'verdictName':'OK', 'programTypeForInvoker':'python.2', 'comparisonType':'NOT_USED', 'judgedTestCount':'', '_tta':'199'},  
		headers = {'X-Csrf-Token':csrf_token},
		cookies = d
		)
	elif language == 'c++':
		print "c++_search"
		#c = requests.post("http://codeforces.com/problemset/status/1/problem/A", 
		c = requests.post(url, 
		data = {'csrf_token':csrf_token, 'action':'setupSubmissionFilter', 'frameProblemIndex':'A', 'verdictName':'OK', 'programTypeForInvoker':'cpp.g++', 'comparisonType':'NOT_USED', 'judgedTestCount':'', '_tta':'199'},  
		headers = {'X-Csrf-Token':csrf_token},
		cookies = d
		)
	else:
		pass

	page = requests.get(url, cookies = d)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	soup = BeautifulSoup(html_content, "html.parser") # making soap

	messages = []

	text = soup.select("body a")

	for row in text:
		#print row
		message = ""
		raw = str(row)
		body = re.search('submissionid="(.*)" t', raw)
		if body != None:
			w = body.group(1)
			#print w
			message = str(w)
			messages.append(message)

	#print "messages"
	#print messages

	return messages

def get_description(i):
	descriptions = []
	left_out = []
	failed_to_download_d = []

	url = 'http://codeforces.com/problemset/problem/' + str(i[0]) + '/' + str(i[1])
	#url = "https://www.codechef.com/api/contests/PRACTICE/problems/" + str(i)

	print url

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

	#print html_content

	if re.search('src="http://codeforces.com/predownloaded', html_content.replace("\\", "")) == None and re.search('src="http://espresso.codeforces.com', html_content.replace("\\", "")) == None and re.search('"message":"Problem is not visible now. Please try again later."', html_content) == None and re.search('Statement is not available', html_content) == None:

		body = re.findall('</div></div><div>(.+?)<script type="text/javascript">', html_content, flags=re.S)
		
		#if body == None:

		#body = BeautifulSoup(page.json()['body']).get_text()

		print i
		#print body

		#w = body.group(1)
		w = body[0]
		w = w.replace('class="upper-index">', 'class="upper-index">^')

		'''NEED TO PUT PUT CODE HERE TO REMOVE SPACES IN NEGATIVE EXPONENTS'''
		w = re.sub('class="upper-index">(.+?)</sup>', sub_strip, w, re.S)

		w = w.replace("</p>", "\n</p>")
		w = w.replace("<br", "\n<br")

		w = w.replace("</div>", "\n</div>")
		w = w.replace("</center>", "\n</center>")

		w = BeautifulSoup(w, "html.parser").get_text()
		w = w.replace("All submissions for this problem are available.", "")

		w = re.sub('Read problems statements in (.+?)\\\\n', '', w, re.M)
		w = re.sub('Subtasks(.+?)Example', 'Example', w, re.S)

		w = w.replace("\u003C","<")
		w = w.replace("\u003E",">")

		w = w.replace("\n\n\n\n\n\n","\n\n\n")
		w = w.replace("\n\n\n\n","\n\n\n")

		w = w.replace("\\","\\\\")

		descriptions.append(w.encode('utf-8').decode('string-escape'))
	else:
		left_out.append(i)


	return descriptions, left_out, failed_to_download_d


def get_solutions(contest, solution_ids):
	solutions = {}
	#failed_to_download_s = []
	with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
		future_to_url = {executor.submit(get_solution, contest, i): i for i in solution_ids}
		for future in concurrent.futures.as_completed(future_to_url):
			data = future.result()

			if data[2] == None:
				solutions[data[0]] = data[1]

	return solutions

def get_solution(contest, solution_id):
	url = 'http://codeforces.com/contest/' + str(contest[0]) + '/submission/' + str(solution_id)
	
	print url

	page = requests.get(url)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	#print html_content

	soup = BeautifulSoup(html_content, "html.parser")

	text = soup.select("body > div > div > div > div > pre")

	failed_to_download = None
	solution = None


	if len(text)==0:
		failed_to_download = solution_id
	else:
		body = BeautifulSoup(str(text[0]), "html.parser").get_text()

		body = body.replace("\\","\\\\")
		solution = body.encode('utf-8').decode('string-escape')

	return solution_id, solution, failed_to_download



def download_all_challenge_names(filename):
	target = open(filename, 'w')

	problem_list = []

	for i in range(0,30):
		a = 'http://codeforces.com/problemset/page/' + str(i+1)
		l = get_problem_list(a)
		for jdx, j in enumerate(l):
			if jdx % 2 == 0:
				problem_list.append(j)
	target.write(str(problems))


#download_all_challenge_names('codechef_problem_names.txt')

def download_descriptions_solutions(filename, index_n):
	root_dir = 'codeforces_data'

	file = open(filename, 'r')
	f = open(filename, 'r')

	index_n_int = int(index_n)

	start = index_n_int + (600*index_n_int)
	end = start + 599

	all_names = []

	for line in f:
		raw = eval(str(line))

	#print raw

	a = ""
	b = ""

	all_names = raw
	#all_names = raw[start:end]

	#language = ["python"]
	language = ["python", "c++"]

	for idx, i in enumerate(all_names):

		descriptions, left_out, failed_to_download_d = get_description(i)
		print i
		if i not in left_out:
			if not os.path.exists(root_dir):
			    os.makedirs(root_dir)

			'''
			cat_dir = root_dir + "/" + category

			if not os.path.exists(cat_dir):
			    os.makedirs(cat_dir)

			save_dir = cat_dir + "/" + i
			#'''

			save_dir = root_dir + "/" + i[0] + "_" + i[1]

			#'''
			if not os.path.exists(save_dir):
			    os.makedirs(save_dir)

			description_dir = save_dir + "/description"

			if not os.path.exists(description_dir):
			    os.makedirs(description_dir)

			description_file_path = description_dir + "/description.txt"
			description_file = open(description_file_path, 'w')
			description_file.write(descriptions[0])

			ids_l = []
			print language
			for l in language:
				print "l"
				print l
				ids = get_solution_ids(i, l)
				ids_l.append(ids)

				print ids
				#solutions, failed_to_download_s = get_solutions(i, ids)
				solutions = get_solutions(i, ids)
				#print failed_to_download_s

				solution_dir = save_dir + "/solutions_" + l

				if not os.path.exists(solution_dir):
				    os.makedirs(solution_dir)

				#print solutions

				print 'len(solutions)'
				print len(solutions)
				'''
				if len(solutions) != 50:
					hdghfdhgf
					'''
				for jdx, j in enumerate(solutions):
					#solutions[j]

					print len(solutions[j])
					if len(solutions[j]) < 10000:
						#solution_file_path = solution_dir + "/" + ids[jdx] + ".txt"
						solution_file_path = solution_dir + "/" + j + ".txt"
						solution_file = open(solution_file_path, 'w')
						solution_file.write(solutions[j])


			#remove problems with zero solutions
			#'''
			if len(ids_l[0]) == 0 and len(ids_l[1]) == 0:
				shutil.rmtree(save_dir)
				#'''

	        #url = 'https://www.codechef.com/status/%d?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)

	#'''
	print "Finished download process"
	if len(failed_to_download) > 0:
	    print "Following challenges failed to download: " + str(failed_to_download)
	    #'''
	
parser = argparse.ArgumentParser()
parser.add_argument('--index', type=str, default="index", help='')
args = parser.parse_args()

index_n = args.index

'''
download_all_challenge_names('challenges_all.txt')
#'''

#'''
download_descriptions_solutions('challenges_all.txt', index_n)
#'''







