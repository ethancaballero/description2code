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

def escape_lt(html):
    html_list = list(html)
    for index in xrange(0, len(html) - 1):
        if html_list[index] == '<' and html_list[index + 1] == ' ':
            html_list[index] = '&lt;'
    return ''.join(html_list)


def get_solution_ids(name, language):

	if language == 'python':
		#FIBQ
		#url = 'https://www.codechef.com/status/FIBQ?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO'
		url = 'https://www.codechef.com/status/%s?sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)
		url2 = 'https://www.codechef.com/status/%s?page=1&sort_by=All&sorting_order=asc&language=4&status=15&handle=&Submit=GO' % (name)
	elif language == 'c++':
		#url = 'https://www.codechef.com/status/FIBQ?sort_by=All&sorting_order=asc&language=41&status=15&handle=&Submit=GO'
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

	#html_content = page.text
	html_content = page1.text + page2.text

	#soup = BeautifulSoup(html_content, "html.parser") # making soap

	messages = []

	#text = soup.select("body a")
	#solution_id_b = re.search("<href='/viewsolution/(.*)' target='_blank'>View", html_content)
	#pts_b = re.search('/>[(.*)pts]<', html_content)

	print url

	#print html_content

	solution_id = re.findall("href='/viewsolution/(.+?)' target='_blank'>View", html_content)
	pts = re.findall("/>\\[(.+?)pts\\]<", html_content)

	print solution_id
	print pts
	print len(pts)
	print len(solution_id)



	#solution_id = solution_id_b.group(1)

	solution_ids = []
	#for s in 

	#if pts_b != None:
	if len(pts) != 0 and len(solution_id) != 0:

		#print 'len(solution_id)'
		#print len(solution_id)
		#print 'len(pts)'
		#print len(pts)

		for i in range(len(pts)):
			#pts = pts_b.group(1)
			#print pts
			#print i
			messages.append([str(solution_id[i]), str(pts[i])])

	return messages

def download_descriptions_solutions(filename, index_n):
	#root_dir = 'codechef_alter_data'
	root_dir = 'codechef_pts_data'

	file = open(filename, 'r')
	f = open(filename, 'r')

	index_n_int = int(index_n)

	start = index_n_int + (500*index_n_int)
	end = start + 499

	print "start"
	print start

	print "end"
	print end 

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
		#print "1"
		#print line
		if str(line).find('type=') != -1:
			body = re.search('type=(.*)', line)
			g = body.group(1)
			#print g
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

	'''
	print easy
	print medium
	print hard
	print harder
	print hardest
	print external
	'''

	all_names = []
	all_names_p = []
	all_names =[["easy", easy], ["medium", medium], ["hard", hard], ["harder", harder], ["hardest", hardest], ["external", external]]
	#all_names =[["hard", hard], ["harder", harder], ["hardest", hardest]]
	#all_names =[["external", external]]
	#all_names =[["easy", easy], ["medium", medium], ["external", external]]

	"""
	'''all_names_before =[["external", external[start:end]]]'''
	all_names_before =[["external", external]]

	'''
	print "all_names"
	print all_names
	'''

	#already_scraped = ['A001', 'A002', 'A003', 'A6', 'AADIV1', 'ABA14A', 'ABA14F', 'ABACUS03', 'ABHSTR', 'ABSNUM', 'ACDEMY', 'ACM14AM1', 'ACM14AM3', 'ACM14AM4', 'ACM14AM5', 'ACM14KG1', 'ACM14KG2', 'ACM14KG3', 'ACM14KG4', 'ACM14KG5', 'ACM14KN1', 'ACM14KN2', 'ACM14KN3', 'ACM14KN4', 'ACM14KP2', 'ACM14KP4', 'ACM14KP5', 'ACMICL2', 'ACMICL3', 'ACMICL4', 'ACULIST', 'AD2', 'AD3', 'AD5', 'AGRAPH', 'AI04', 'AKASHPRB', 'ALFZ01', 'ALFZ02', 'ALG2N', 'ALGBBQ', 'ALGFACT', 'ALGINT', 'ALGPAN', 'ALGPRX', 'ALIENC', 'ALK01', 'ALK1101', 'ALK1102', 'ALK1104', 'ALK1105', 'ALK13B', 'ALK13C', 'ALK13E', 'ALK13G', 'ALMA01', 'ALMA02', 'ALMA03', 'ALMOSTPR', 'ALNPD', 'ALNUM', 'ALPHA', 'ALTRTREE', 'AMCAS', 'AMCOINS', 'AMCS05', 'AMCS06', 'AMGIT', 'AMR14B', 'AMR14C', 'AMR14D', 'AMR14E', 'AMR14H', 'AMR14I', 'AMR14J', 'ANUUND', 'AOU', 'APGE01', 'APOWB', 'APPUZZLE', 'AQS', 'ARAN01', 'ARAN03', 'ARAN06', 'ARAN07', 'ARB', 'ARFF', 'ARHN01', 'ARHN07', 'ARHN09', 'ARITHM', 'ARRAY', 'ARTHMNCY', 'ASYA1', 'ASYA3', 'ATKCTR', 'ATM5', 'ATOM', 'AUPM', 'AVISKR02', 'AVISKR03', 'AVISKR04', 'AWTHR', 'AX01', 'AX04', 'AXR1P2', 'AXR1P3', 'AXR3P3', 'AXR3P4', 'BACO1605', 'BALLS', 'BALPRIME', 'BANKPASS', 'BAO', 'BASECHG', 'BEATRICE', 'BESTBATS', 'BHAV', 'BI01', 'BIGO05', 'BIGOF02', 'BIGOF03', 'BIGOF06', 'BIGP', 'BINOP', 'BIT', 'BIT1506', 'BITCJ3', 'BITCJ5', 'BITSACM5', 'BLDNGS', 'BLZ004', 'BOW15D', 'BPHC03', 'BSTCLASS', 'BTCD14B', 'BTCD14C', 'BTCD1502', 'BTCODE_C', 'BTCODE_D', 'BTCODE_I', 'BTCODE_J', 'BTCODE_K', 'BTREAT', 'BUSCON', 'BUY1GET1', 'BUYORNOT', 'BWTREE', 'BYCD1603', 'BYTES1', 'BYTES13', 'BYTES2', 'BYTES3', 'BYTESA', 'BYTESC', 'BYTESG', 'C3003', 'C3004', 'C4', 'CAKE1AM', 'CAMERAS', 'CAMERAS2', 'CAN1', 'CANDIS', 'CANDLE', 'CANDYPK', 'CARCOUNT', 'CARDINAL', 'CATCH', 'CB01', 'CB03', 'CB04', 'CB05', 'CB06', 'CB1', 'CB2', 'CB20Q5', 'CB3', 'CBLOCKS', 'CC', 'CC2', 'CC4', 'CCCB03', 'CCCS1', 'CCCS2', 'CCUBE03', 'CCUBE04', 'CD101', 'CD103', 'CD1IT1', 'CD1IT2', 'CD1IT3', 'CD1IT4', 'CD1IT5', 'CD202', 'CDBSTR5', 'CDBSTR7', 'CDCR15_1', 'CDFX05', 'CDM02', 'CDM03', 'CDME02', 'CDME05', 'CDMN01', 'CDMN04', 'CDMT06', 'CDMU01', 'CDMU03', 'CDMU05', 'CDOLP3', 'CDOUT1', 'CDQU05', 'CDQU1', 'CDQU10', 'CDQU2', 'CDQU4', 'CDS001', 'CDS003', 'CDS007', 'CDS008', 'CDSW152', 'CDSW153', 'CDVA1501', 'CDVA1502', 'CDVA1504', 'CDVA1507', 'CDVA1510', 'CDVA1607', 'CDWRS01', 'CDWRS04', 'CDWRS06', 'CDWY01', 'CDXM1', 'CDZ1302', 'CDZ1304', 'CE02', 'CE06', 'CE07', 'CENCODE', 'CEXP03', 'CEXP05', 'CF01', 'CF02', 'CF220', 'CF221', 'CF222', 'CF224', 'CFR101', 'CFR103', 'CFR201', 'CFR203', 'CFR302', 'CFR303', 'CFR304', 'CG01', 'CG02', 'CG04', 'CHAP', 'CHAPD', 'CHCOINSG', 'CHCOM', 'CHDISH', 'CHEARMY', 'CHEFARK', 'CHEFARR', 'CHEFBWN', 'CHEFCYCL', 'CHEFGARD', 'CHEFHAR', 'CHEFHILL', 'CHEFLAPT', 'CHEFLUCK', 'CHEFPOW', 'CHEFTIC', 'CHEFTR', 'CHFBOOKS', 'CHFFIELD', 'CHFMAX', 'CHKTRE', 'CHN15A', 'CHN15C', 'CHN15F', 'CHOC', 'CHOCOLAT', 'CHOCS', 'CHSQARR', 'CHTKN', 'CI1', 'CKTFEV', 'CLCO02', 'CLCO03', 'CLCO04', 'CLCO05', 'CLCO06', 'CLNDR', 'CLNFORUM', 'CLOCK01', 'CLTGAME', 'CM01', 'CM04', 'CM1401', 'CM1403', 'CM1404', 'CM1505', 'CMAN', 'CMB01', 'CMB02', 'CMB03', 'CME04', 'CN01', 'CN03', 'CN04', 'CN05', 'CNG', 'CNT1S', 'COAD01', 'COAD03', 'COADIES1', 'COADIES2', 'COADIES4', 'COCR03', 'COCR09', 'COCRMR01', 'COCRMR04', 'COD04', 'COD07', 'COD08', 'COD09', 'CODEIT1', 'CODEIT2', 'CODEIT4', 'CODEIT7', 'CODEN01', 'CODEN03', 'CODQ2', 'CODQ3', 'CODQ4', 'CODQ7', 'COG14A', 'COG14B', 'COLTREE', 'COMA01', 'COMA02', 'COMA03', 'COMAF02', 'COMP02', 'COMP03', 'COMR01', 'COMR02', 'COMR03', 'COOKIES', 'COOLING', 'COOP5', 'COPSUM', 'CORE1', 'CORE2', 'CORE9', 'COSH1502', 'COSH1505', 'COTR01', 'COTR02', 'COTR03', 'COUNTC', 'COUNTSTR', 'COWA7', 'COWA8', 'CPOINT', 'CR01', 'CR02', 'CR03', 'CR04', 'CR06', 'CRACE', 'CRAFT01', 'CRAFT05', 'CRANBROM', 'CRANCBOY', 'CRANCRD', 'CRBREAK', 'CREDCS3', 'CREDE2', 'CREDEXAM', 'CREDF2', 'CREDF3', 'CREDF4', 'CREDLEAD', 'CREDNCSM', 'CREDPLWD', 'CREDROPE', 'CREDVOLC', 'CRES102', 'CRES103', 'CRGM', 'CRICINFO', 'CRNGFLSH', 'CRNGSLDN', 'CRNM1203', 'CRNM1205', 'CRNM1206', 'CRNM1207', 'CRNM1301', 'CRNM1302', 'CRNM1303', 'CRNM1305', 'CRYPT', 'CRYPT05', 'CRZ04', 'CRZMNR', 'CS001', 'CS04', 'CS05', 'CS07', 'CS08', 'CSEA1', 'CSEA2', 'CSEA4', 'CSIXIEPA', 'CSIXIERL', 'CSIXIEVR', 'CSS', 'CSTRIKE2', 'CSTRIKE3', 'CSTRIKE4', 'CTRA01', 'CTRA04', 'CUBTOWER', 'CW02', 'CW03', 'CW04', 'CW05', 'CW08', 'CW1', 'CWAM1501', 'CWAMR103', 'CWAMR404', 'CWAYS', 'CYCLIST', 'CYSM', 'CYW03', 'CYW04', 'CYW05', 'CYW12', 'D04', 'D1', 'DBYZ15A', 'DBYZ15B', 'DBYZ15F', 'DBZ16RS', 'DBZ16XS1', 'DCE03', 'DCE04', 'DCE05', 'DCL2015B', 'DCL2015G', 'DCL2015H', 'DCL2015I', 'DCL2015J', 'DCOL', 'DECA03', 'DELSUM', 'DETDET', 'DEVARRAY', 'DEVILNUM', 'DIGIT', 'DIGROT', 'DISHMIX', 'DISPLAY', 'DLCT02', 'DLCT04', 'DMILK', 'DMNOS', 'DMSG', 'DOORS', 'DOUBLE', 'DPC101', 'DPC103', 'DPC104', 'DPC107', 'DPC201', 'DPC202', 'DPC204', 'DPC206', 'DPC207', 'DPC210', 'DQPERMS', 'DRTVG', 'DS04', 'DS05', 'DS06', 'DS07', 'DS08', 'DS09', 'DS10', 'DS14', 'DS15', 'DS19', 'DS22', 'DS24', 'DSPATNA1', 'DSPATNA2', 'DSPATNA3', 'DSPC302', 'DSPC308', 'DZ16HITE', 'DZ16SHOP', 'DZ16SUBA', 'EDITLIST', 'EGYPT', 'EGYPTFRA', 'EMS07', 'EN03', 'EN04', 'ENC2', 'ENC3', 'ENCD01', 'ENCD06', 'ENCD08', 'ENCD10', 'ENCD12', 'ENCODE01', 'ENCODE04', 'ENCODE11', 'ENCODE13', 'EPI01', 'EPI02', 'EPI03', 'EQCANDY', 'EQUINUM', 'ESYYSE', 'ETMX01', 'ETMX05', 'ETMX06', 'ETMX07', 'EVILHACK', 'EXAM', 'EXEBIT03', 'EXORO', 'FACT25', 'FACTEASY', 'FBFRW1', 'FBFRW3', 'FCTRIZE', 'FIBGCD', 'FINDHOLE', 'FISHY', 'FLCM', 'FLOOR', 'FOOT', 'FORCES', 'FP03', 'FP04', 'FP08', 'FP09', 'FR22', 'FRJUMP', 'FRSTDATE', 'FSSYNC', 'FTH', 'FUNN', 'FUZZYADD', 'GAME2048', 'GCDMAX1', 'GCDQ', 'GGAME', 'GMB01', 'GOALIE', 'GOC01', 'GOC04', 'GOC203', 'GOOGOL01', 'GOOGOL03', 'GOOGOL05', 'GOOGOL06', 'GOPJ', 'GOPR', 'GOT', 'GOTT', 'GOVT', 'GPRIME', 'GPYRD', 'GRAYCODE', 'GRECT', 'GREEDY', 'GRID01', 'GUARDS', 'GUESS', 'HES', 'HFCQ5', 'HLPSUG', 'HOBB', 'HOLES', 'HOLES2', 'HOTEL', 'HPYBDAY', 'HSTRY', 'HTLPLM', 'I13POF', 'I13TS', 'ICD01', 'ICD02', 'ICD03', 'ICD04', 'ICECREAM', 'ICGO', 'ICLFIN05', 'ICODER3', 'ICQ1', 'ICQ2', 'ICQ4', 'IDCLOVE', 'IEEET02', 'IEEET03', 'IEEEUOM', 'IFC03P02', 'IG01', 'IG03', 'IG04', 'IGNUS14B', 'IGNUS14C', 'IIITA02', 'IIITA206', 'IIITBH10', 'IIITBH11', 'IIITBH13', 'IITI00', 'IITI01', 'IITI03', 'IITI05', 'IITI10', 'IITI13', 'IITI15', 'IITK1P01', 'IITK1P02', 'IITK1P04', 'IITK1P05', 'IITK1P06', 'IITK1P07', 'IITK1P10', 'IITK1P11', 'IITK2P01', 'IITK2P02', 'IITK2P03', 'IITK2P06', 'IITK2P07', 'IITK2P08', 'IITK2P09', 'IITK2P10', 'INC3', 'INC4', 'INC5', 'INS0902', 'INSCTS4', 'INSM02', 'INSM06', 'INSOMA1', 'INSOMA3', 'INSOMA4', 'INSOMA5', 'INSOMB1', 'INSOMB3', 'INSOMB6', 'INSQ15_A', 'INSQ15_D', 'INSQ15_E', 'INSQ15_G', 'INSQ15_H', 'INTEX1', 'INTEX10', 'INTEX12', 'INTEX2', 'INTEX7', 'INTEX8', 'INTEX9', 'INTRESEC', 'INTROSRM', 'IOPC06', 'IOPC1104', 'IOPC1105', 'IOPC1107', 'IOPC1108', 'IOPC1109', 'IOPC1110', 'IOPC1111', 'IOPC1112', 'IOPC1113', 'IOPC1114', 'IOPC1200', 'IOPC1208', 'IOPC1211', 'IOPC1212', 'IOPC1214', 'IOPC1216', 'IOPC13D', 'IOPC13I', 'IOPC13K', 'IOPC13N', 'IOPC13O', 'IOPC13Q', 'IOPC13S', 'IOPC14A', 'IOPC14B', 'IOPC14C', 'IOPC14D', 'IOPC14G', 'IOPC14J', 'IOPC14L', 'IOPC14N', 'IOPC14O', 'IOPC14Q', 'IOPC15A', 'IOPC15D', 'IOPC15I', 'IOPC15Q', 'IOPC16L', 'IOPC16Q', 'ISD', 'ITM002', 'ITM003', 'ITM004', 'IWIN', 'JACKPOT', 'JADEJA', 'JADMST', 'JAGE', 'JERYFIBO', 'JMI01', 'JMI04', 'JNTUV1', 'JNTUV2', 'JNTUV3', 'JNTUV4', 'JOV', 'K15A', 'K16F', 'KAN13A', 'KAN13C', 'KAN13F', 'KAN13G', 'KAN15RTA', 'KAN15RTC', 'KAN15RTE', 'KAN15RTF', 'KAN15RTI', 'KAN15RTJ', 'KAN15RTK', 'KC01', 'KC03', 'KC05', 'KC204', 'KC205', 'KGP13A', 'KGP13B', 'KGP13C', 'KGP13D', 'KGP13E', 'KGP13F', 'KGP13G', 'KGP13I', 'KGP14A', 'KGP14B', 'KGP14C', 'KGP14D', 'KGP14F', 'KGP14G', 'KGP14H', 'KGP14J', 'KING', 'KJCC02', 'KNIGHT01', 'KOKT03', 'KOKT05', 'KOL15A', 'KOL15B', 'KOL15C', 'KOL15D', 'KTHPATH', 'L2', 'L3', 'L4', 'LASTDIG', 'LASTRIDE', 'LECANDY', 'LELOUCH3', 'LELOUCH4', 'LEOX', 'LETRI', 'LGCR02', 'LIGHTS', 'LINCAN', 'LINEPROB', 'LM', 'LMDP1102', 'LMDP1104', 'LN', 'LOCKS', 'LOLOL', 'LPUACE02', 'LUCKY', 'LUKYDRIV', 'MAC01', 'MAGICSTR', 'MAJNUM', 'MANIP2', 'MANIP3', 'MARS', 'MASNUM', 'MAXCOUNT', 'MAXSUM', 'MDLREN', 'MDOSA', 'MES', 'MHTBAG', 'MHTCLASS', 'MINION', 'MIRRORS', 'MISNUM', 'MISSNUM', 'MISTERM', 'MOD', 'MPREF', 'MPROB', 'MPS08', 'MPSTME3', 'MPSTME5', 'MQRY', 'MRGSRT', 'MRIU11', 'MRIU12', 'MRIU4', 'MSTICK', 'MSTRINGS', 'MTRANS', 'MULDIV', 'MULMAGIC', 'MULTIPLY', 'MUTRUSH', 'NBSUM', 'NCC8', 'NEURON1', 'NEURON3', 'NEURONB1', 'NEURONE3', 'NEXUS03', 'NF02', 'NF03', 'NFEB4', 'NGAME', 'NICENESS', 'NICEQUAD', 'NICPRM', 'NITA01', 'NITA02', 'NITA04', 'NITA05', 'NITA09', 'NITA10', 'NITA11', 'NMAGIC', 'NOPC1', 'NOPC10', 'NOPC3', 'NOPC6', 'NOPC9', 'NOWAYS', 'NPRM', 'NPT', 'NSIT13', 'NSIT15', 'NUMGAME', 'NUMSET', 'NXTPALIN', 'NYUMAT', 'NYUMTEA', 'NYUSTONE', 'ODDEVENX', 'OPC1602', 'OPC1603', 'OPC1604', 'OV1', 'OVERTAKE', 'P10', 'P1306', 'P1308', 'P1310', 'P1311', 'P1313', 'P6', 'P8', 'PAINT', 'PALHAPPY', 'PARKWOE', 'PASCAL', 'PATH01', 'PATHSG', 'PBUZZ1', 'PBUZZ2', 'PBUZZ3', 'PBUZZ4', 'PBUZZ7', 'PBUZZ9', 'PC02', 'PC03', 'PC05', 'PCHIPS', 'PCJ1', 'PCSC1', 'PCSC2', 'PCSC3', 'PD12', 'PD13', 'PD22', 'PD31', 'PD32', 'PD33', 'PERM', 'PEWPEW', 'PILEGAME', 'PINOCH1', 'PINOCH2', 'PLAYNUM', 'PLGRM', 'PLTGRP', 'PNUM', 'POFACT', 'POMUSE', 'POSTIT', 'POWER2', 'POWHIKE', 'POWRS', 'POYTPP', 'POYTTC', 'PPOW', 'PRAC', 'PRAYAS01', 'PRAYAS05', 'PRAYAS07', 'PRCNSR1', 'PRCNSR4', 'PRCNSR5', 'PRDEL', 'PRDIV', 'PREE03', 'PREE04', 'PREE05', 'PRESTI', 'PRI01', 'PRIM2', 'PRIME', 'PRIMEOB', 'PRIMPAL', 'PRIMPATT', 'PRMARTH', 'PRMRL', 'PROM01', 'PRPALIN', 'PRQUIN', 'PRSN', 'PRST', 'PRYS01', 'PRYS02', 'PRYS08', 'PSG02', 'PSTRINGS', 'PSUDO4', 'PT1', 'PT2', 'PT8', 'PUCK', 'QCJ1', 'QCJ2', 'QCJ3', 'QUARK2', 'QUARK5', 'QUCOATO', 'QUCOITA', 'QUCOLCM', 'QUEST', 'R101', 'R103', 'R202', 'R205', 'R303', 'RACEWARS', 'RAILGADI', 'RBX12R03', 'RBX1301', 'RBX1312', 'RBX1316', 'RD04', 'RDIOACTV', 'RECAREA', 'RECCKT', 'RECIIBKS', 'RECIIDCD', 'RECIITRK', 'RECMSG', 'RECPLA', 'RECREP', 'RECSQU', 'RECT', 'REN2013A', 'REN2013B', 'REN2013E', 'REN2013G', 'REN2013I', 'REN2013K', 'REPDEC', 'REPUB', 'RESIST', 'RESN01', 'RESN02', 'RESN04', 'RESN05', 'REUNION', 'REVER', 'RG04', 'RG202', 'RG204', 'RG206', 'RG207', 'RG208', 'RGHW06', 'RGPVR101', 'RGPVR102', 'RGPVR103', 'RGPVR201', 'RGPVR203', 'RIDDLE', 'RIT01', 'RIT02', 'RIT04', 'RIVALRY', 'RMATH', 'RNGMOD', 'ROLLDEEP', 'RRATING', 'RRMATRIX', 'RSJS', 'RTB', 'RUBIX2', 'RUBIX4', 'RWALK', 'SAARC01', 'SAARC02', 'SAARC04', 'SAARC06', 'SAARC07', 'SACHGF', 'SALG01', 'SAMU', 'SATA01', 'SATA03', 'SATA05', 'SATA11', 'SC', 'SCC0104', 'SCC0105', 'SCC0106', 'SCORES', 'SCOREX', 'SHARMAJI', 'SHASFUN', 'SHINAPP', 'SHISTR', 'SHUFFLE2', 'SHUTTLE', 'SIDPRIME', 'SIDSTR', 'SILK', 'SIMKRY', 'SLADDERS', 'SLX04', 'SMCD3', 'SMCD5', 'SMHTE', 'SMPLSUM', 'SNAKE', 'SNAKENUM', 'SNCHT2', 'SNON07', 'SNON08', 'SNOWLIST', 'SNOWPRIM', 'SOPC02', 'SOPC05', 'SOPC1501', 'SOPC1504', 'SOPC1506', 'SORT', 'SORT4', 'SP01', 'SP03', 'SPIDY', 'SPIDY2', 'SPIRAL', 'SPIT04', 'SPIT1', 'SPIT3', 'SPRLNMS', 'SQUE1', 'SREENI', 'SSEQ', 'SSORT', 'SSWAP', 'ST202', 'STANDUP', 'STATSHW', 'STATUES', 'STCKS', 'STIKGAME', 'STKENC', 'STR_FUNC', 'STRGM', 'STRMCH', 'STRONG', 'SUBBXOR', 'SUBSGCD', 'SUBSTR', 'SUMMATH', 'SURF', 'SWAPMATR', 'SWEET', 'SYBANK', 'SYNBRIG', 'SYNCRYPT', 'T01', 'TAZOS', 'TCFST04', 'TCFST05', 'TCFST07', 'TCFST09', 'TDIV', 'TEAMUP', 'TECH02', 'TECH04', 'TECH05', 'TECH06', 'TECH07', 'TECH08', 'TECH09', 'TECH10', 'TECH13', 'TEMPQUE', 'TENNCLUM', 'TESTTT5', 'TF01', 'TF03', 'TF04', 'TGPA01', 'TGPA02', 'THIEF', 'TIC02', 'TIC04', 'TIDRICE', 'TIME', 'TOFFEES', 'TOMJER', 'TOS03', 'TOS04', 'TOYSGAME', 'TR001', 'TR003', 'TR004', 'TRIANGCL', 'TRIDIM', 'TRINT', 'TRSUM', 'TRYOUT', 'TSX01', 'TSX02', 'TTEACH', 'TUX03', 'TWOFRNDS', 'UNIVMT', 'VCAKE', 'VERMIN', 'VIRAT', 'VITC01', 'VLD', 'VOTE', 'VSQ3', 'WATSY', 'WAY004', 'WGHTLIF', 'WICQ4', 'WICQ5', 'WKIMAAL', 'WMIS', 'WOLVXR', 'WORDCNT', 'WOWPRO', 'WYSIWYG3', 'WYSIWYG4', 'XORSACK', 'XORSN', 'YJUMP', 'ZEROES']

	already_scraped = []

	for ndx, n in enumerate(all_names_before[0][1]):
		if n not in already_scraped:
			all_names_p.append(n)

	print "all_names"
	#print all_names_p
	print len(all_names_p)
	"""

	#all_names = [["external", all_names_p[start:end]]]





	for ndx, n in enumerate(all_names):
		category = all_names[ndx][0]
		problem_list = all_names[ndx][1]
		#descriptions, left_out, failed_to_download_d = get_descriptions(problem_list)

		language = ["python", "c++"]

		#root_dir = 'codechef_data'


		for idx, i in enumerate(problem_list):
		#for idx, i in enumerate(['ACDEMY']):
			#descriptions, left_out, failed_to_download_d = get_description(i)
			#descriptions, left_out, failed_to_download_d = get_solution_ids(i)
			#print descriptions
			#print left_out
			#if i not in left_out:

			if not os.path.exists(root_dir):
			    os.makedirs(root_dir)

			cat_dir = root_dir + "/" + category

			if not os.path.exists(cat_dir):
			    os.makedirs(cat_dir)

			#save_dir = cat_dir + "/" + i
			save_dir = cat_dir

			if not os.path.exists(save_dir):
				os.makedirs(save_dir)

			#'''
			ids_l = []
			for l in language:
				ids = get_solution_ids(i, l)
				problem2_id_pts = {}
				#problem2_id_pts[str(i) + '_' + str(l)] = ids
				problem2_id_pts[i + '/' + 'solutions_' + l] = ids

				print problem2_id_pts
				#print len(problem2_id_pts)
				print len(ids)

				#ids_l.append(ids)

				#'''
				#for jdx, j in enumerate(solutions):
				#solution_file_path = save_dir + "/" + ids[jdx] + ".txt"
				s_file_path = 'tags' + '_' + category
				#solution_file = open(solution_file_path, 'w')
				#solution_file = open(s_file_path, 'a')
				if len(ids) != 0:
					solution_file = open(s_file_path, 'a')
					#solution_file.write(i + '\n' + l + '\n' + str(problem2_id_pts) + '\n')
					solution_file.write(str(problem2_id_pts) + '\n')
					#'''

				'''
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
				    '''
			'''
			#remove problems with zero solutions
			if len(ids_l[0]) == 0 and len(ids_l[1]) == 0:
				shutil.rmtree(save_dir)
				'''

			print problem2_id_pts

parser = argparse.ArgumentParser()
parser.add_argument('--index', type=str, default="index", help='')
args = parser.parse_args()

index_n = args.index

#get_solution_ids('codechef_problem_names.txt', index_n)



#download_descriptions_solutions('codechef_problem_names_easy.txt')
#download_descriptions_solutions('codechef_problem_names.txt', index_n)
#download_descriptions_solutions('codechef_problem_names_left.txt', index_n)
download_descriptions_solutions('codechef_problem_names.txt', index_n)
#download_descriptions_solutions('codechef_problem_names_easy_short.txt')






