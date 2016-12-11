
#from bs4 import BeautifulSoup

'''
description url = "https://www.codechef.com/api/contests/PRACTICE/problems/KOL1502"

solution url = "https://www.codechef.com/viewplaintext/9863461"

"https://www.codechef.com/ssubmission/prob?page=undefined&pcode=CIELAB"
#'''

from pprint import pprint
from bs4 import BeautifulSoup
import requests
import urllib2
import re

'''
info = 'http://codeforces.com/api/user.status?handle=tacklemore&from=1&count=1'
solution = 'view-source:http://codeforces.com/contest/686/submission/18671530'
do not include problems with http://codeforces.com/predownloaded/
'''



'''
def get_problem_list(url):
	response = urllib2.urlopen(url)
	
	html_content = response.read()

	soup = BeautifulSoup(html_content, "html.parser") # making soap


	messages = []

	text = soup.select("body > table > tbody a")
	for row in text:
	    print row

	    m = str(row).find('https://www.codechef.com/problems/')
	    print m 
	    if m != -1 and m != None:
			m_start_index = m+34
			message = ""
			raw = str(row)
			for i in range(len(raw)):
			    if raw[i] == '/' and raw[i+1] == '"' and raw[i+2] == ' ' and raw[i+3] == 't' and raw[i+4] == 'a':
			        break	
			    elif raw[i] == '"' and raw[i+1] == ' ' and raw[i+2] == 't' and raw[i+3] == 'a':
			        break
			    elif i >= m_start_index:
			        message += raw[i]
			    else:
			        pass


			if message != 'easy' and message != 'medium' and message != 'hard' and message != 'challenge' and message != 'extcontest' and message != 'school':
				messages.append(message)


	#print messages
	return messages
	'''

#body = re.search(' data-submission-id="(.*)" data-a=', raw)

def get_problem_list(url):
	page = requests.get(url)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url)
	html_content = page.text

	soup = BeautifulSoup(html_content, "html.parser") # making soap

	messages = []
	tags = []
	problem_and_tags = {}
	problem_and_tags_array = []

	text = soup.select("body a")
	body_problem_prev = None
	b_p = None

	for row in text:
		message = ""
		raw = str(row)
		#body_problem = re.search(' href="/problemset/problem/(.*)">', raw)
		body_problem = re.search(' href="/problemset/submit/(.*)">', raw)
		body_tag = re.search(' href="/problemset/tags/(.*)" style', raw)
		#second_tag = re.search('style="float:right', raw)

		'''
		if body_problem != None:
		#if body_problem != None and body_problem != body_problem_prev:
			if body_problem.group(1) == body_problem_prev:
				#body_problem_prev = body_problem
				body_problem_prev = None
				problem_and_tags[b_p] = tags
				#problem_and_tags = {}
				problem_and_tags_array.append(problem_and_tags)
				problem_and_tags = {}
				#print problem_and_tags
				tags = []
			else:
				body_problem_prev = body_problem.group(1)
				'''

		if body_problem != None:
			#body_problem_prev = body_problem
			w = body_problem.group(1)
			message = str(w)
			b_p = message.replace('/', '_')
			problem_and_tags[b_p] = tags
			#problem_and_tags = {}
			problem_and_tags_array.append(problem_and_tags)
			problem_and_tags = {}
			tags = []
			#print b_p


		if body_tag != None:
			w = body_tag.group(1)
			message = str(w)
			b_t = message
			tags.append(b_t)




	#return problem_and_tags
	return problem_and_tags_array
#'''


#problem_list = {}
problem_list = []
'''
for i in range(0,30):
	a = 'http://codeforces.com/problemset/page/' + str(i+1) + '?order=BY_SOLVED_DESC'
	'''
'''
for i in range(0,30):
	a = 'http://codeforces.com/problemset/page/' + str(i+1)
	l = get_problem_list(a)
	for jdx, j in enumerate(l):
		if jdx % 2 == 0:
			problem_list.append(j)

print problem_list
'''
for i in range(0,30):
#for i in range(29,30):
	a = 'http://codeforces.com/problemset/page/' + str(i+1)
	l = get_problem_list(a)
	#problem_list.update(l)
	problem_list += l



#print problem_list
#print sorted(problem_list.items())
#del problem_list[None]
#a = problem_list.keys()
print problem_list
#print sorted(a)
#print sorted(problem_list.keys())
'''
for k in sorted(problem_list):
   print k.replace(' ', '_'), problem_list[k]
   '''
description_file = open("tags.txt", 'w')
description_file.write('')

for k in problem_list:
	#print k
	description_file = open("tags.txt", 'a')
	description_file.write(str(k) + "\n")