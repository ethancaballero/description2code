
import shutil
import os
import re
import requests
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import html2text
import time

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
	elif language == 'c++':
		url = 'https://www.codechef.com/status/%s?sort_by=All&sorting_order=asc&language=41&status=15&handle=&Submit=GO' % (name)
	else:
		pass

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

	    m = str(row).find('/viewsolution/')
	    if m != -1 and m != None:
			m_start_index = m+len('/viewsolution/')
			message = ""
			raw = str(row)
			for i in range(len(raw)):	
			    if raw[i] == '"' and raw[i+1] == ' ' and raw[i+2] == 't' and raw[i+3] == 'a':
			        break
			    elif i >= m_start_index:
			        message += raw[i]
			    else:
			        pass


			if message != 'easy' and message != 'medium' and message != 'hard' and message != 'challenge' and message != 'extcontest' and message != 'school':
				messages.append(message)

	return messages

def get_descriptions(problem_list):
	descriptions = []
	left_out = []
	failed_to_download_d = []
	for i in problem_list:
		url = "https://www.codechef.com/api/contests/PRACTICE/problems/" + str(i)

		page = requests.get(url)

		if str(page) == "<Response [503]>":
			while str(page) == "<Response [503]>":
				time.sleep(1)
				page = requests.get(url)

		html_content = page.text


		if html_content==None:
			failed_to_download_d.append(i)



		if re.search('<img src="https://s3.amazonaws.com/codechef_shared/download/upload', html_content.replace("\\", "")) == None:

			text = BeautifulSoup(html_content).get_text()

			body = re.search('","body":"(.*)","languages_supported":', text)
			language = re.search('","languages_supported":"(.*)","', text)

			w = body.group(1)
			w = w.replace("All submissions for this problem are available.", " ")

			w = re.sub('Read problems statements in (.+?)\\\\n', '', w, re.M)
			w = re.sub('Subtasks(.+?)Example', 'Example', w, re.S)
	
			w = w.replace("\u003C","<")
			w = w.replace("\u003E",">")

			descriptions.append(w.encode('utf-8').decode('string-escape'))
		else:
			left_out.append(i)

	return descriptions, left_out, failed_to_download_d


def get_solutions(solution_ids):
	solutions = []
	failed_to_download_s = []
	for i in solution_ids:
		url = "https://www.codechef.com/viewplaintext/" + str(i)
		
		page = requests.get(url)
		if str(page) == "<Response [503]>":
			while str(page) == "<Response [503]>":
				time.sleep(1)
				page = requests.get(url)
		html_content = page.text

		if html_content==None:
			failed_to_download_s.append(i)

		text = BeautifulSoup(html_content, "html.parser").get_text()

		solutions.append(text.encode('utf-8').decode('string-escape'))

	return solutions, failed_to_download_s



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

def download_descriptions_solutions(filename):
	root_dir = 'codechef_data'

	file = open(filename, 'r')
	f = open(filename, 'r')

	#problem_list = file.read()

	#print problem_list

	easy = []
	medium = []
	hard = []
	harder = []
	hardest = []
	external = []

	g = ""
	i=0
	for line in f:
		print "1"
		if str(line).find('type=') != -1:
			body = re.search('type=(.*)', line)
			g = body.group(1)
			print g
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

	print easy
	print medium
	print hard
	print harder
	print hardest
	print external

	all_names =[["easy", easy], ["medium", medium], ["hard", hard], ["harder", harder], ["hardest", hardest], ["external", external]]

	for ndx, n in enumerate(all_names):
		category = all_names[ndx][0]
		problem_list = all_names[ndx][1]
		descriptions, left_out, failed_to_download_d = get_descriptions(problem_list)

		language = ["python", "c++"]

		root_dir = 'codechef_data'


		for idx, i in enumerate(problem_list):
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

				if not os.path.exists(description_dir):
				    os.makedirs(description_dir)

				description_file_path = description_dir + "/description.txt"
				description_file = open(description_file_path, 'w')
				description_file.write(str(descriptions[idx]))

				for l in language:
					ids = get_solution_ids(i, l)
					print ids
					solutions, failed_to_download_s = get_solutions(ids)
					print failed_to_download_s

					solution_dir = save_dir + "/solutions_" + l

					if not os.path.exists(solution_dir):
					    os.makedirs(solution_dir)

					for jdx, j in enumerate(solutions):
					    solution_file_path = solution_dir + "/" + ids[jdx] + ".txt"
					    solution_file = open(solution_file_path, 'w')
					    solution_file.write(j)

				#remove problems with zero solutions
				if len(ids_l[0]) == 0 and len(ids_l[1]) == 0:
					shutil.rmtree(save_dir)

	        #url = 'https://www.codechef.com/status/%d?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)

	'''
    print "Finished download process"
    if len(failed_to_download) > 0:
        print "Following challenges failed to download: " + str(failed_to_download)
        '''


#download_all_challenge_names('codechef_problem_names.txt')	

download_descriptions_solutions('codechef_problem_names.txt')



#download_descriptions_solutions('codechef_problem_names_easy.txt')
#download_descriptions_solutions('codechef_problem_names_easy_short.txt')






