# -*- coding: utf-8 -*-
from sys import argv
import time
import argparse
import shutil
import os
import re
import requests
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import html2text
import concurrent.futures
import time
import subprocess


#p = subprocess.Popen(['pgrep phantomjs | xargs kill'], stdout=subprocess.PIPE, shell=True)

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'



def get_solution_ids(n, l):

    print n

    url="https://www.hackerearth.com/problem/algorithm/" + n + "/activity/"
    t = requests.get(url)
    tmp_string = t.headers["set-cookie"]
    csrf_token = re.findall(r"csrftoken=\w*", tmp_string)[0][10:]
    problem_id = re.findall(r"/AJAX/submissions/problem/algorithm/(.*?)/',", t.text)
    #print problem_id

    response = {}
    response["host"] = "www.hackerearth.com"
    response["user-agent"] = user_agent
    response["accept"] = "application/json, text/javascript, */*; q=0.01"
    response["accept-language"] = "en-US,en;q=0.5"
    response["accept-encoding"] = "gzip, deflate"
    response["content-type"] = "application/x-www-form-urlencoded"
    response["X-CSRFToken"] = csrf_token
    response["X-Requested-With"] = "XMLHttpRequest"
    #response["Referer"] = "https://www.hackerearth.com/submissions/" + handle + "/"
    response["Referer"] = url
    response["Connection"] = "keep-alive"
    response["Pragma"] = "no-cache"
    response["Cache-Control"] = "no-cache"
    response["Cookie"] = tmp_string

    #'''
    trs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_url = {executor.submit(get_solution_id, problem_id, response, i, l): i for i in xrange(1, 25)}
        for future in concurrent.futures.as_completed(future_to_url):
            data = future.result()

            for i in data:
                trs.append(i)

    links = []

    print len(trs)

    for tr in trs:
        #print "wtf"
        partial = False
        for i in tr.find_all('i', class_=True):
            #print str(i)
            if "fa-orange" in str(i):
                #print "partial"
                partial = True

        if partial == False:
            #print 'how'
            #print tr
            for a in tr.find_all('a', class_='link-13'):
                #print a
                link = re.search('"/submission/(.*?)/"', str(a)).group(1)
                #print "link"
                #print link
            if len(links) < 50:
                links.append(link)
            else:
                break

    #print len(links)
    #print i
    print l
    print len(links)
    print links

    #fdghfdh

    return links

def get_solution_id(problem_id, response, i, l):
    if l == 'python':
        url = "https://www.hackerearth.com/AJAX/submissions/problem/algorithm/" + str(problem_id[0]) + "/?result=AC&lang=Python&page=" + str(i)
        page = requests.get(url, headers=response)
        if str(page) == "<Response [503]>":
            while str(page) == "<Response [503]>":
                time.sleep(1)
                page = requests.get(url, headers=response)

        trs = []
        if len(page.text) > 15:
            body = page.json()["data"]
            #print len(body)
            soup = BeautifulSoup(body, "lxml")
            trsub = soup.find("tbody").find_all("tr")
            '''
            for i in trsub:
                trs.append(i)
                '''
        #pages.append(page)
    elif l == 'c++':
        url = "https://www.hackerearth.com/AJAX/submissions/problem/algorithm/" + str(problem_id[0]) + "/?result=AC&lang=C%2B%2B&page=" + str(i)
        page = requests.get(url, headers=response)
        if str(page) == "<Response [503]>":
            while str(page) == "<Response [503]>":
                time.sleep(1)
                page = requests.get(url, headers=response)

        trs = []
        if len(page.text) > 15:
            body = page.json()["data"]
            #print len(body)
            soup = BeautifulSoup(body, "lxml")
            trsub = soup.find("tbody").find_all("tr")
            '''
            for i in trsub:
                trs.append(i)
                '''
        #pages.append(page)
    else:
        pass

    return trsub

def get_solutions(solution_ids, sample_dir):
    '''
    print "solution_ids"
    print solution_ids
    '''

    #asdfas

    '''YOU NEED TO RELOOK UP THIS VALUE AND UPDATE IT REGULARLY'''
    '''when logeed in on a description: inpsector -> Application -> Cookies -> www.hackerearth.com -> lordoftherings'''
    lotr_cookie_value="13c082ac336859d586aa5364c086d26f:cc68c8202d59204d2d85eda67df114bc"

    if not os.path.exists(sample_dir):
        sample_inputs, sample_outputs = get_samples(solution_ids[0], lotr_cookie_value)
    elif len(os.listdir(sample_dir)) < 2:
        sample_inputs, sample_outputs = get_samples(solution_ids[0], lotr_cookie_value)
    else:
        sample_inputs = []
        sample_outputs = []
    solutions = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_url = {executor.submit(get_solution, i, lotr_cookie_value): i for i in solution_ids}
        for future in concurrent.futures.as_completed(future_to_url):
            data = future.result()

            if data[2] == None:
                solutions.append([data[0], data[1]])
                #solutions[data[0]] = data[1]

    return sample_inputs, sample_outputs, solutions


#'''
#def get_solution(idx, i):
def get_solution(i, lotr_cookie_value):
    #url = "https://www.hackerearth.com/submission/5159653/"
    url = "https://www.hackerearth.com/submission/" + i
    cookies = {}
 
    '''YOU NEED TO RELOOK UP THIS VALUE AND UPDATE IT REGULARLY via get_solutions function'''
    cookies["lordoftherings"]=lotr_cookie_value

    t = requests.get(url, cookies=cookies)
    if str(t) == "<Response [503]>":
        while str(t) == "<Response [503]>":
            time.sleep(1)
            t = requests.get(url, cookies=cookies)

    solution_url_clones = re.findall('submission/key/(.+?)/', t.text)

    #print "solution_url_clones"
    #print solution_url_clones

    solution_key = solution_url_clones[0]

    solution_url = "https://www.hackerearth.com/submission/key/" + solution_key

    solution_request = requests.get(solution_url)
    if str(solution_request) == "<Response [503]>":
        while str(solution_request) == "<Response [503]>":
            time.sleep(1)
            solution_request = requests.get(solution_url)

    #print solution_request.text

    html_content = solution_request.text

    soup = BeautifulSoup(html_content)

    text = soup.select("pre")

    #print 'text'
    #print text

    #failed_to_download_s = []
    failed_to_download_s = None
    solution = ''
    if len(text)==0:
        #failed_to_download_s.append(i)
        failed_to_download_s = solution_id
    else:
        body = BeautifulSoup(str(text[0]), "html.parser").get_text()

        body = body.replace("\\","\\\\").encode('utf-8').decode('string-escape')
        #solutions.append([i, body.encode('utf-8').decode('string-escape')])
        #print "body"
        #print body
        solution = body

    #return solutions, failed_to_download_s

    #return solution

    #print i

    return i, solution, failed_to_download_s
    #'''

def get_samples(i, lotr_cookie_value):
    print i
    #url = "https://www.hackerearth.com/response/submission/5159653/"
    url = "https://www.hackerearth.com/response/submission/" + i + "/"
    #url = "https://www.hackerearth.com/submission/" + i
    cookies = {}

    '''YOU NEED TO RELOOK UP THIS VALUE AND UPDATE IT REGULARLY via get_solutions function'''
    cookies["lordoftherings"]=lotr_cookie_value

    t = requests.get(url, cookies=cookies)
    if str(t) == "<Response [503]>":
        while str(t) == "<Response [503]>":
            time.sleep(1)
            t = requests.get(url, cookies=cookies)

    tmp_string = t.headers["set-cookie"]
    csrf_token = re.findall(r"csrftoken=\w*", tmp_string)[0][10:]

    response = {}
    response["host"] = "www.hackerearth.com"
    response["user-agent"] = user_agent
    response["accept"] = "application/json, text/javascript, */*; q=0.01"
    response["accept-language"] = "en-US,en;q=0.5"
    response["accept-encoding"] = "gzip, deflate"
    response["content-type"] = "application/x-www-form-urlencoded"
    response["X-CSRFToken"] = csrf_token
    response["X-Requested-With"] = "XMLHttpRequest"

    response["Referer"] = url
    response["Connection"] = "keep-alive"
    response["Pragma"] = "no-cache"
    response["Cache-Control"] = "no-cache"
    response["Cookie"] = tmp_string

    url += "/AJAX/"
    #url = "https://www.hackerearth.com/response/submission/5159653/AJAX/"


    tmp = requests.get(url, headers=response)
    if str(tmp) == "<Response [503]>":
        while str(tmp) == "<Response [503]>":
            time.sleep(1)
            tmp = requests.get(url, headers=response)

    #sgfdsgd

    test_urls = re.findall('<a href="(.+?)\\?Signature=', tmp.text)
    #print test_urls
    input_urls=[]
    output_urls=[]
    all_io_urls=[]

    for i in range(len(test_urls)):
        if i % 3 == 0:
            #input_urls.append([test_urls[i], "input"])
            all_io_urls.append([test_urls[i], "input"])
        elif i % 3 == 2:
            #output_urls.append([test_urls[i], "output"])
            all_io_urls.append([test_urls[i], "output"])
        else:
            pass

    inputs = []
    outputs = []
    trs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_url = {executor.submit(get_sample, k[0], k[1]): k for k in all_io_urls}
        for future in concurrent.futures.as_completed(future_to_url):
            data = future.result()

            if data[1] == 'input':
                inputs.append(data[0])
            elif data[1] == 'output':
                outputs.append(data[0])

    '''
    print "inputs"
    print len(inputs)

    print "outputs"
    print len(outputs)
    '''

    return inputs, outputs
    #'''

def get_sample(j, label):
    input_request = requests.get(j)
    if str(input_request) == "<Response [503]>":
        while str(input_request) == "<Response [503]>":
            time.sleep(1)
            input_request = requests.get(j)

    #print j

    return input_request.text, label
    #inputs.append(input_request.text)


def get_tags():
    '''
    <tr id="row">
    <a href="/problem/algorithm/mancunian-and-nancy-play-a-game-1/" class="link-13 track-problem-link">
    <td class="medium-col dark track-tags">
                    Graph Theory, Medium
                </td>
    '''
    pass


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
            #if message != 'easy' and message != 'medium' and message != 'hard' and message != 'challenge' and message != 'extcontest' and message != 'school':
            messages.append(message)

    return messages

def parse_description(raw):
    raw = raw.replace("\n\n\n\n\n\n", "")
    #raw = raw.replace("\n\n\n\n\n", "\n")

    raw = raw.replace("\n\n\n", "\n")
    raw = raw.replace("\n\n\n", "\n\n")

    raw = raw.replace("\n\n\n", "\n\n")

    raw = raw.replace("<sup>", "<sup>^")

    raw = raw.replace("\in", u"∈")
    #raw = raw.replace("\in", u"∈").replace('$$', '')

    raw = raw.replace(" <=", u" ≤").replace(" >=", u" ≥").replace("<=", u" ≤ ").replace(">=", u" ≥ ").replace(u"≤  ", u"≤ ").replace(u"≥  ", u"≥ ").replace("\le", u"≤").replace("\ge", u"≥").replace("\lt", "<").replace("\gt", ">")

    raw = re.sub('Subtasks(.+?)SAMPLE INPUT', 'SAMPLE INPUT', raw, flags=re.S)

    raw = re.sub('Time Limit:(.+)', '', raw, flags=re.S)

    raw = re.sub('See Russian translation\n\n', '', raw, flags=re.S)
    raw = re.sub('See Russian translation', '', raw, flags=re.S)

    '''
    raw = raw.replace(u"†Input† :", "Input :")
    raw = raw.replace(u"†Input :†", "Input :")
    raw = raw.replace(u"†Input†", "Input :")
    raw = raw.replace(u"†Output† :", "Output :")
    raw = raw.replace(u"†Output :†", "Output :")
    raw = raw.replace(u"†Output†", "Output :")
    raw = raw.replace(u"†Constraints† :", "Constraints :")
    raw = raw.replace(u"†Constraints :†", "Constraints :")
    raw = raw.replace(u"†Constraints†", "Constraints :")
    '''

    raw = raw.replace(u"†Input† :", "Input")
    raw = raw.replace(u"†Input :†", "Input")
    raw = raw.replace(u"†Input†", "Input")
    raw = raw.replace(u"†Output† :", "Output")
    raw = raw.replace(u"†Output :†", "Output")
    raw = raw.replace(u"†Output†", "Output")
    raw = raw.replace(u"†Constraints† :", "Constraints")
    raw = raw.replace(u"†Constraints :†", "Constraints")
    raw = raw.replace(u"†Constraints†", "Constraints")

    #print 'b'
    #print raw

    #raw = re.sub(r'†([^†]*(?:†|$))', r'‡\1', raw)
    raw = re.sub(u'†(.+?)†', u'†' + r'\1' + u'‡', raw, flags=re.S)
    #(.+?)

    #print 'a'
    #print raw

    raw = raw.replace("\\","\\\\")

    return raw


def get_descriptions(problem):
    descriptions = []
    descriptions_annotated = []
    left_out = []
    failed_to_download_d = []
    #print problem_list
    #for i in problem_list:

    url = 'https://www.hackerearth.com/problem/algorithm/' + problem

    #print url

    page = requests.get(url)

    if str(page) == "<Response [503]>":
        while str(page) == "<Response [503]>":
            time.sleep(1)
            page = requests.get(url)

    html_content_all = page.text

    if re.search('"message":"requests limit exhausted"', html_content_all) != None:
        while re.search('message":"requests limit exhausted', html_content_all) != None:
            time.sleep(1)
            page = requests.get(url)
            html_content_all = page.text

    if html_content_all==None:
        failed_to_download_d.append(i)

    soup = BeautifulSoup(html_content_all)

    html_content_1 = soup.findAll("div", { "class" : "starwars-lab" })
    html_content_2 = soup.findAll("div", { "class" : "less-margin-2 input-output-container" })
    html_content_3 = soup.findAll("div", { "class" : "standard-margin" })

    #print html_content_1[0], html_content_2[0], html_content_3[0]

    #raw = BeautifulSoup(str(html_content[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^").replace("\le", u"≤").replace("\ge", u"≥").replace("\lt", "<").replace("\gt", ">"), "html.parser").get_text()
    #raw_text = BeautifulSoup(str(html_content_1[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_2[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_3[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text()
    raw_text = BeautifulSoup(str(html_content_1[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^").replace('$$', ''), "html.parser").get_text() + BeautifulSoup(str(html_content_2[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^").replace('$$', ''), "html.parser").get_text() + BeautifulSoup(str(html_content_3[0]).replace("</p>", "\n</p>").replace("<sup>", "<sup>^").replace('$$', ''), "html.parser").get_text()
    #annotated_text = BeautifulSoup(str(html_content_1[0]).replace("<strong>", "†").replace("</strong>", "‡").replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_2[0]).replace("<strong>", "†").replace("</strong>", "‡").replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_3[0]).replace("<strong>", "†").replace("</strong>", "‡").replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text()
    annotated_text = BeautifulSoup(str(html_content_1[0]).replace("<strong>", "†").replace("</strong>", "†").replace('$$', '†').replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_2[0]).replace("<strong>", "†").replace("</strong>", "†").replace('$$', '†').replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text() + BeautifulSoup(str(html_content_3[0]).replace("<strong>", "†").replace("</strong>", "†").replace('$$', '†').replace("</p>", "\n</p>").replace("<sup>", "<sup>^"), "html.parser").get_text()



    #print "raw"
    #print raw

    #sfgds

    #if re.search("https://d320jcjashajb2.cloudfront.net/media/uploads", str(html_content_all)) == None and re.search('"message":"Problem is not visible now. Please try again later."', str(html_content_all)) == None and re.search('Statement is not available', str(html_content_all)) == None:
    if re.search("https://d320jcjashajb2.cloudfront.net/media/uploads", html_content_all) == None and re.search('"message":"Problem is not visible now. Please try again later."', html_content_all) == None and re.search('Statement is not available', html_content_all) == None:
        raw = parse_description(raw_text)
        annotated = parse_description(annotated_text)

        descriptions.append(raw.encode('utf-8').decode('string-escape'))
        descriptions_annotated.append(annotated.encode('utf-8').decode('string-escape'))
    else:
        #left_out.append(i)
        #descriptions.append(raw.encode('utf-8').decode('string-escape'))
        left_out.append(problem)

        #hjgf

    #print 'descriptions'    
    #print descriptions[0]

    #asasdf

    return descriptions, descriptions_annotated, left_out, failed_to_download_d
    #return descriptions, left_out, failed_to_download_d


def download_all_challenge_names(filename):
    target = open(filename, 'w')

    problems = []
    
    target.write(str(problems))

    #'''
    
    #'''

#download_all_challenge_names('codechef_problem_names.txt')

def download_descriptions_solutions(filename, index_n):
    #root_dir = 'hackerearth_data'
    root_dir = 'hackerearth_data_working'

    if filename == 'problems.txt':
        category = "problems_normal"
    elif filename == 'problems_college.txt':
        category = "problems_college"

    file = open(filename, 'r')
    f = open(filename, 'r')

    index_n_int = int(index_n)

    start = index_n_int + (500*index_n_int)
    end = start + 499

    all_names = []
    not_available = []

    for line in f:
        raw = eval(str(line))

    #print raw

    a = ""
    b = ""

    all_names = raw

 
    language = ["python", "c++"]
    #language = ["c++", "python"]

    #print "wtf"

    #print descriptions, left_out, failed_to_download_d

    for idx, i in enumerate(all_names):
        print i
        #descriptions, left_out, failed_to_download_d = get_descriptions(i)
        '''IT'S SET TO THE SAME ONE EVERY TIME RIGHT HERE; NEED TO REMOVE'''
        #i = "sort-the-array-5"
        #i = "bits-transformation-1"
        #i = "string-division"
        #i = "little-achraf-in-who-wants-to-be-a-millionaire"
        #i = "terrible-chandu"
        #i = "little-shino-and-fibonacci"
        #i = "interval-count-12"
        #description, left_out, failed_to_download_d = get_descriptions(i)

        try:
            cat_dir = root_dir + "/" + category
            save_dir = cat_dir + "/" + i

            if not os.path.exists(save_dir):
                description, description_annotated, left_out, failed_to_download_d = get_descriptions(i)
                #print i
                if i not in left_out:
                    print "folder_name^"

                    if not os.path.exists(root_dir):
                        os.makedirs(root_dir)

                    #'''
                    cat_dir = root_dir + "/" + category

                    if not os.path.exists(cat_dir):
                        os.makedirs(cat_dir)

                    save_dir = cat_dir + "/" + i
                    #'''

                    #save_dir = root_dir + "/" + i[0] + "_" + i[1]

                    if not os.path.exists(save_dir):
                        os.makedirs(save_dir)

                    description_dir = save_dir + "/description"

                    if not os.path.exists(description_dir):
                        os.makedirs(description_dir)

                    #print description
                    #print description[0]
                    #print 'description'

                    description_file_path = description_dir + "/description.txt"
                    description_file = open(description_file_path, 'w')
                    description_file.write(description[0])

                    description_file_path = description_dir + "/description_annotated.txt"
                    description_file = open(description_file_path, 'w')
                    description_file.write(description_annotated[0])

                    #asdf

                    ids = []

                    ids_l = []

                    #ids_p, ids_c = get_solution_ids(i, language)
                    try:
                        for l in language:
                            ids = get_solution_ids(i, l)
                            ids_l.append(ids)

                            #ids_p, ids_c = get_solution_ids(i, language)

                            print l

                            '''
                            if l == 'python':
                                ids = ids_p
                            elif l == 'c++':
                                ids = ids_c
                                '''

                            solution_dir = save_dir + "/solutions_" + l

                            if not os.path.exists(solution_dir):
                                os.makedirs(solution_dir)


                            '''
                            sample_dir = save_dir + "/samples"

                            if not os.path.exists(sample_dir):
                                os.makedirs(sample_dir)
                                '''
                            


                            print ids
                            #solutions, failed_to_download_s = get_solutions(i, ids)
                            #solutions, failed_to_download_s = get_solutions(ids)
                            print "len(ids)"
                            print len(ids)
                            if len(ids) > 0:

                                sample_dir = save_dir + "/samples"

                                sample_inputs, sample_outputs, solutions = get_solutions(ids, sample_dir)
                                #print failed_to_download_s

                                if not os.path.exists(sample_dir):
                                    os.makedirs(sample_dir)

                                solution_dir = save_dir + "/solutions_" + l

                                print "solutions"
                                print len(solutions)

                                print 'inputs'
                                print len(sample_inputs)

                                print 'outputs'
                                print len(sample_outputs)
                                #print solutions

                                for jdx, j in enumerate(sample_inputs):
                                    #print j
                                    if len(sample_inputs[jdx]) < 1000000:
                                    #if len(sample_inputs[jdx]) < 2000000:
                                        #j_num = re.findall('submission/(.+?)/', str(j))
                                        solution_file_path = sample_dir + "/" + str(jdx+1) + "_input" + ".txt"
                                        solution_file = open(solution_file_path, 'w')
                                        solution_file.write(sample_inputs[jdx])
                                        solution_file.close()

                                for jdx, j in enumerate(sample_outputs):
                                    #print j
                                    if len(sample_outputs[jdx]) < 1000000:
                                        #j_num = re.findall('submission/(.+?)/', str(j))
                                        solution_file_path = sample_dir + "/" + str(jdx+1) + "_output" + ".txt"
                                        solution_file = open(solution_file_path, 'w')
                                        solution_file.write(sample_outputs[jdx])
                                        solution_file.close()

                                for jdx, j in enumerate(solutions):
                                    #print j
                                    if len(j[1]) < 10000:
                                        '''probably need to change this line'''
                                        #j_num = re.findall('submission/(.+?)/', str(j))
                                        solution_file_path = solution_dir + "/" + str(j[0]) + ".txt"
                                        solution_file = open(solution_file_path, 'w')
                                        solution_file.write(j[1])
                                        solution_file.close()
                            else:
                                pass

                        #remove problems with zero solutions
                        if len(ids_l[0]) == 0 and len(ids_l[1]) == 0:
                        #if len(ids_p) == 0 and len(ids_c) == 0:
                            shutil.rmtree(save_dir)

                    except UnboundLocalError:
                        shutil.rmtree(save_dir)
                        not_available.append(i)
                        print i, "not available anymore"
        #'''
        except IndexError:
            not_available.append(i)
            print i, "not available anymore"
            #'''

    print 'list of not_available'
    print not_available

    #sasdsdfasd

    #url = 'https://www.codechef.com/status/%d?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)

'''
print "Finished download process"
if len(failed_to_download) > 0:
    print "Following challenges failed to download: " + str(failed_to_download)
    '''


#download_all_challenge_names('codechef_problem_names.txt') 
parser = argparse.ArgumentParser()
parser.add_argument('--index', type=str, default="index", help='')
args = parser.parse_args()

index_n = args.index

#download_descriptions_solutions('challenges.txt', index_n)

'''ADD MODULE TO GRAB DESCRIPTIONS WITH/WITHOUT ANNOTATIONS FOR TOKENS TO BE CONVERTED TO VARIABLES'''
#'''
#download_descriptions_solutions('problems_college.txt', index_n)
download_descriptions_solutions('problems.txt', index_n)
#'''
#'''
#get_solutions(ids)
'''
get_solutions('https://www.hackerearth.com/submission/4634147/')
#'''

#browser.close()
#browser.quit()

#download_descriptions_solutions('challenges_1.txt', index_n)

#get_descriptions(['interval-count-12', 'final-battle', 'benny-and-universal-numbers'])

#download_descriptions_solutions('codechef_problem_names_easy.txt')
#download_descriptions_solutions('codechef_problem_names_easy_short.txt')

"""

    
print get_solution('5159653')
a = get_samples('5159653')
print a
print a[0]
print a[0][0]
#"""






