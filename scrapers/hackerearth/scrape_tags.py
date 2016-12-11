import requests
import re

def get_tags():
    url1 = "https://www.hackerearth.com/problems/"
    url2 = "https://www.hackerearth.com/college-challenges/problems/"
    cookies = {}
 
    '''YOU NEED TO RELOOK UP THIS VALUE AND UPDATE IT REGULARLY via get_solutions function'''
    lotr_cookie_value="13c082ac336859d586aa5364c086d26f:cc68c8202d59204d2d85eda67df114bc"
    cookies["lordoftherings"]=lotr_cookie_value

    t = requests.get(url1, cookies=cookies)
    if str(t) == "<Response [503]>":
        while str(t) == "<Response [503]>":
            time.sleep(1)
            t = requests.get(url1, cookies=cookies)



    problems = re.findall('<span class="dark" id="(.+?)-solved">', t.text, re.S)
    tags = re.findall('dark track-tags">(.+?)</td>', t.text, re.S)

    #print "solution_url_clones"
    #print solution_url_clones

    #solution_key = solution_url_clones[0]

    print len(problems)
    print len(tags)

    problem_and_tags = {}

    for i in range(len(problems)):
        if '   \n   ' in tags[i]:
            tags[i] = ''

    	problem_and_tags[problems[i]] = tags[i].replace(' ','').replace('\n','').split(',')


    t = requests.get(url2, cookies=cookies)
    if str(t) == "<Response [503]>":
        while str(t) == "<Response [503]>":
            time.sleep(1)
            t = requests.get(url2, cookies=cookies)



    problems = re.findall('<span class="dark" id="(.+?)-solved">', t.text, re.S)
    tags = re.findall('dark track-tags">(.+?)</td>', t.text, re.S)

    #print "solution_url_clones"
    #print solution_url_clones

    #solution_key = solution_url_clones[0]

    print len(problems)
    print len(tags)

    for i in range(len(problems)):
        if '   \n   ' in tags[i]:
            tags[i] = ''

        problem_and_tags[problems[i].encode("utf-8")] = tags[i].replace(' ','').replace('\n','').encode("utf-8").split(',')


    print len(problem_and_tags)

    return problem_and_tags


a=get_tags()
print a 
print len(a)
print a.items()[0]

for k in a.items():
    #print k
    description_file = open("tags.txt", 'a')
    description_file.write(str(k).replace('(','{').replace(')','}').replace("{u'", "{'").replace("[u'", "['").replace(", u'", ", '").replace("', [", "': [").encode("utf-8") + "\n")
    #description_file.write(str(k).replace('(','{').replace(')','}') + "\n")
