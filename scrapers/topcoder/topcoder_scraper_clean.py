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

cookies = dict()
cookies['tcsso'] = '40451530|b0be8a6e3acae9d8743c91ada7294a5b65a698b0dfa82cda539d54a7d41e7584'


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

def get_rounds(url):
	page = requests.get(url, cookies=cookies)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url, cookies=cookies)
	html_content = page.text

	#print html_content
	#print repr(html_content)

	round_content = re.search('Select a Round:</OPTION>(.+?)Select a Room:</OPTION>', html_content.replace("\\", ""), flags=re.S)
	#room_content = re.search('Select a Room:</OPTION>(.+?)COLSPAN="4" CLASS="statText"', html_content.replace("\\", ""), flags=re.S)
	
	#body = re.findall('<OPTION value="/stat\\?c=room_stats(.+?)</OPTION>', html_content.replace("\\", ""), flags=re.S)

	body = re.findall('<OPTION value="/stat\\?c=room_stats(.+?)</OPTION>', round_content.group(1).replace("\\", ""), flags=re.S)

	#print body

	rounds = []

	for sub_body in body:
		message = str(sub_body)
		if re.search('">', message, flags=re.S):
			c = message.split('">')
		else:
			c = message.split('" selected>')
		#print c
		rounds.append(c)

	#print rounds

	return rounds

def get_rooms(url):
	page = requests.get(url, cookies=cookies)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url, cookies=cookies)
	html_content = page.text

	#print html_content
	#print repr(html_content)

	#round_content = re.search('Select a Round:</OPTION>(.+?)Select a Room:</OPTION>', html_content.replace("\\", ""), flags=re.S)
	room_content = re.search('Select a Room:</OPTION>(.+?)COLSPAN="4" CLASS="statText"', html_content.replace("\\", ""), flags=re.S)
	
	#body = re.findall('<OPTION value="/stat\\?c=room_stats(.+?)</OPTION>', html_content.replace("\\", ""), flags=re.S)

	body = re.findall('<OPTION value="/stat\\?c=room_stats(.+?)</OPTION>', room_content.group(1).replace("\\", ""), flags=re.S)

	#print body

	rooms = []

	for sub_body in body:
		message = str(sub_body)
		if re.search('">', message, flags=re.S):
			c = message.split('">')
		else:
			c = message.split('" selected>')
		#print c
		rooms.append(c)

	print rooms

	return rooms

def get_authors(url1):
	page = requests.get(url1, cookies=cookies)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url1, cookies=cookies)
	author_content = page.text

	body_score = re.findall('module=MemberProfile(.+?)\\.[0-9][0-9]</TD>', author_content.replace("\\", ""), flags=re.S)

	'''
	print 'wtf'

	for i in body_score:
		print i
		print '\n'
		#'''

	#dsgfsfd

	authors = []

	for i in body_score:
		if re.search('ALIGN="right">(.+?)</TD>', i) != str(0):
			#author = re.search('&cr=(.+?)" C', i)
			author = re.search('(.+?)" CLASS', i)
			authors.append(author.group(1))

			#print '\n'

	#if 
	#body = re.findall('/tc\\?module=MemberProfile(.+?)" C', author_content.group(1).replace("\\", ""), flags=re.S)

	
	'''URL OF PAGE YOU WERE VIEWING'''
	#https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329101
	''''''

	#dsgfsfd	

	#CLASS="statText" ALIGN="right">2</TD>

	print authors

	return authors


'''
def get_pages():
	#all_rounds = get_rounds('https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329100')
	all_rounds = get_rounds('https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329101')
	#print all_rounds
	for i in all_rounds:
		url = 'https://community.topcoder.com/stat?c=room_stats' + i[0]
		#get_rooms(url)
		for j in get_rooms(url):
			url1 = 'https://community.topcoder.com/stat?c=room_stats' + j[0]
			print url1
			#sgf
			for k in get_authors(url1):
				url2 = "https://community.topcoder.com/stat?c=coder_room_stats" + j[0] + k
				
				a = k
				'''

def get_solution_ids(url2):
	#body_score = re.findall('<TD CLASS="statText" HEIGHT="13">(.+?)<TD COLSPAN="8"><IMG SRC="/i/clear.gif" ALT="" WIDTH="1" HEIGHT="3" BORDER="0"></TD>', author_content.replace("\\", ""), flags=re.S)

	print url2

	page = requests.get(url2, cookies = cookies)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url2)
	html_content = page.text

	#print html_content

	body_score = re.findall('<TD CLASS="statText" HEIGHT="13">(.+?)<TD COLSPAN="8"><IMG SRC="/i/clear.gif" ALT="" WIDTH="1" HEIGHT="3" BORDER="0"></TD>', html_content.replace("\\", ""), flags=re.S)

	#print body_score

	solution_ids_sub = []

	for i in body_score:
		if "Passed System Test" in i:
			solution_id = re.search('&pm=(.+?)&cr', i)
			'''MAYBE ADD SOME CODE HERE TO GET NAME AND NOT JUST NUMBER REPRESENTING NAME'''
			solution_ids_sub.append(solution_id.group(1))

	print solution_ids_sub

	#sfdsg

	return solution_ids_sub

def get_samples(url2):

	page = requests.get(url2, cookies=cookies)
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url2, cookies=cookies)
	html_content = page.text

	#print html_content[0:100000]

	#soup = BeautifulSoup(html_content, "html.parser")

	#text = soup.select("body > table > tbody > tr > td.bodyText > table.paddingTable > tbody > tr:nth-child(1) > td > table:nth-child(4) > tbody > tr:nth-child(13) > td")

	body = re.findall('<TR VALIGN="top" class="alignTop">(.+?)CLASS="statText" ALIGN="right">Passed</TD>', html_content, flags=re.S)

	inputs = []
	outputs = []

	for i in body:
		inp = re.search('CLASS="statText" ALIGN="left">(.+?)</TD>', i)
		out = re.search('CLASS="statText" ALIGN="right">(.+?)</TD>', i)
		inputs.append(inp.group(1))
		outputs.append(out.group(1))
		print i

	print inputs
	print outputs
	asdf

	'''
	if len(text)==0:
		failed_to_download = solution_id
	else:
		body = BeautifulSoup(str(text), "html.parser").get_text()

		body = body.replace("\\","\\\\")
		solution = body.encode('utf-8').decode('string-escape')

		#print repr(solution)
		#print solution
		'''

	return solution



def get_pages():
	#all_rounds = get_rounds('https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329100')
	all_rounds = get_rounds('https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329101')
	#print all_rounds
	for i in all_rounds:
		url = 'https://community.topcoder.com/stat?c=room_stats' + i[0]
		#get_rooms(url)
		for j in get_rooms(url):
			url1 = 'https://community.topcoder.com/stat?c=room_stats' + j[0]
			if "Division-II" in str(j[1]):
				for k in get_authors(url1):
					url2 = "https://community.topcoder.com/stat?c=coder_room_stats" + j[0] + k
					solution_ids = get_solution_ids(url2)


					'''get_sample PROBABLY BELONGS ELSEWHERE'''
					url_sample = "https://community.topcoder.com/stat?c=problem_solution" + j[0] + k + "&pm=" + solution_ids[0]
					get_samples(url_sample)
					

					for m in get_solution_ids(url2):
						url3 = "https://community.topcoder.com/stat?c=problem_solution" + j[0] + k + "&pm=" + m
						get_solution(url3)

			else:
				for k in get_authors(url1):
					url2 = "https://community.topcoder.com/stat?c=coder_room_stats" + j[0] + k

def get_description(i):
	descriptions = []
	left_out = []
	failed_to_download_d = []

	#url = 'http://codeforces.com/problemset/problem/' + str(i[0]) + '/' + str(i[1])
	#url = "https://www.codechef.com/api/contests/PRACTICE/problems/" + str(i)
	#url = "https://community.topcoder.com/stat?c=problem_statement&pm=14346&rd=16790"
	#url = "https://community.topcoder.com/stat?c=problem_statement&pm=14360&rd=16775&rm=329103&cr=22853544"
	#url = "https://community.topcoder.com/stat?c=problem_statement&pm=14115"

	url = i

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

	if re.search('img src="http://www.topcoder.com/contest/problem/', html_content.replace("\\", "")) == None and re.search('src="http://espresso.codeforces.com', html_content.replace("\\", "")) == None and re.search('"message":"Problem is not visible now. Please try again later."', html_content) == None and re.search('Statement is not available', html_content) == None:

		body = re.findall('Problem Statement</h3></td></tr><tr>(.+?)</td></tr></table><hr><p>', html_content, flags=re.S)
		
		#if body == None:

		#body = BeautifulSoup(page.json()['body']).get_text()

		print i
		#print body

		#w = body.group(1)
		w = body[0]
		w = w.replace('class="upper-index">', 'class="upper-index">^')
		w = w.replace("&#160;&#160;&#160;&#160;", "")
		#w = w.replace(':</td><td class="statText">', ':\t</td><td class="statText">')
		w = w.replace(':</td><td class="statText">', ':    </td><td class="statText">')

		'''NEED TO PUT PUT CODE HERE TO REMOVE SPACES IN NEGATIVE EXPONENTS'''
		w = re.sub('class="upper-index">(.+?)</sup>', sub_strip, w, re.S)

		#w = w.replace("<h3>", "<h3>\n")
		#w = w.replace("</p>", "\n</p>")
		#w = w.replace("<br", "\n<br")
		w = w.replace("</td></tr><tr>", "\n</td></tr><tr>")
		w = w.replace("<ul>\n", "<ul>")
		w = w.replace("<li>", u"• ")
		w = w.replace("</li>\n</ul>", "</li></ul>")
		#</li>\n</ul>
		w = w.replace('<td align="center" valign="top" class="statText">-', '<td align="center" valign="top" class="statText">- ')


		#w = w.replace("</div>", "\n</div>")
		#w = w.replace("</center>", "\n</center>")

		w = BeautifulSoup(w, "html.parser").get_text()
		w = w.replace("All submissions for this problem are available.", "")

		w = re.sub('Read problems statements in (.+?)\\\\n', '', w, re.M)
		w = re.sub('Subtasks(.+?)Example', 'Example', w, re.S)
		#w = re.sub('[^\\\\n]\\\\n[0-9]\)\\\\n', '\\\\n\\\\n[0-9]\)\\\\n', w, flags=re.M)
		#[0-9]

		#w = re.sub('Subtasks(.+?)Example', 'Example', w, re.S)

		w = w.replace("\u003C","<")
		w = w.replace("\u003E",">")

		#w = w.replace("\n\n\n\n\n\n","\n\n\n")
		#w = w.replace("\n\n\n\n","\n\n\n")

		'''
		w = w.replace("\n\n\n\n\n\n","\n\n\n\n\n")
		w = w.replace("\n\n\n\n\n","\n\n\n\n")
		w = w.replace("\n\n\n\n","\n\n\n")
		#'''

		w = w.replace(u"\u00A0","\n")


		w = re.sub("\n\n\n\n\n\n", "\n\n\n\n\n", w, flags=re.M)
		w = re.sub("\n\n\n\n\n", "\n\n\n\n", w, flags=re.M)
		w = re.sub("\n\n\n\n", "\n\n\n", w, flags=re.M)

		#w = re.sub('[^\n]\n[0-9]\\)\n', '\n\n\1)\n', w, flags=re.M)
		w = re.sub('([^\n])(\n[0-9])(\\))(\n)', '\n\\2)\n', w, flags=re.M)
		w = re.sub('(Example\n)(\n[0-9])(\\))(\n)', 'Example\\2)\n', w, flags=re.M)


		w = w.replace("\\","\\\\")

		print w.encode('utf-8').decode('string-escape')
		#print repr(w.encode('utf-8').decode('string-escape'))
		#gsdh

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

#def get_solution(contest, solution_id):
def get_solution(url):
	#url = 'https://community.topcoder.com/stat?c=problem_solution&cr=40440099&rd=16747&pm=14278'
	
	#url = 'https://community.topcoder.com/stat?c=problem_solution&rm=329103&rd=16775&pm=14340&cr=23089515'

	#url = 'https://community.topcoder.com/stat?c=problem_solution&cr=40364957&rd=16747&pm=14278'

	print url

	#tcsso = 'b0be8a6e3acae9d8743c91ada7294a5b65a698b0dfa82cda539d54a7d41e7584'

	#cookies = dict()
	#cookies['tcsso'] = '40451530|b0be8a6e3acae9d8743c91ada7294a5b65a698b0dfa82cda539d54a7d41e7584'
	#'40451530|b0be8a6e3acae9d8743c91ada7294a5b65a698b0dfa82cda539d54a7d41e7584'

	#cookies['JSESSIONID'] = 'UYKd7Rv1-OY-6bmewBWJDw**.tomcat_tc01'

	print cookies

	page = requests.get(url, cookies=cookies)
	#print page
	if str(page) == "<Response [503]>":
		while str(page) == "<Response [503]>":
			time.sleep(1)
			page = requests.get(url, cookies=cookies)
	html_content = page.text

	#print html_content[0:100000]

	#soup = BeautifulSoup(html_content, "html.parser")

	#text = soup.select("body > table > tbody > tr > td.bodyText > table.paddingTable > tbody > tr:nth-child(1) > td > table:nth-child(4) > tbody > tr:nth-child(13) > td")

	body = re.findall('<TD CLASS="problemText" COLSPAN="8" VALIGN="middle" class="alignMiddle" ALIGN="left">\n            (.+?)<BR>\n        </TD>', html_content, flags=re.S)

	text = body[0]

	text = text.replace("<BR>","\n")

	#print w

	#print repr(text)
	print text

	failed_to_download = None
	solution = None


	if len(text)==0:
		failed_to_download = solution_id
	else:
		body = BeautifulSoup(str(text), "html.parser").get_text()

		body = body.replace("\\","\\\\")
		solution = body.encode('utf-8').decode('string-escape')

		#print repr(solution)
		#print solution

	return solution

	#return solution_id, solution, failed_to_download



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

'''
download_descriptions_solutions('challenges_all.txt', index_n)
#'''

#url = "https://community.topcoder.com/stat?c=problem_statement&pm=14346&rd=16790"
#url = "https://community.topcoder.com/stat?c=problem_statement&pm=14368"
#url = 'https://community.topcoder.com/stat?c=problem_solution&rm=329103&rd=16775&pm=14340&cr=23089515'
url = 'https://community.topcoder.com/stat?c=room_stats&rd=16775&rm=329100'

#get_description(url)
#get_solution(url)
#get_rounds(url)
#get_rooms(url)
get_pages()









