# Python3 program for a word cleaner
# ver 1.0
import requests
import codecs
import operator
from collections import *
import re
import json
from urllib.parse import unquote
import sys


def clean_unicode(word,is_reverse =0):
	rules = [
	 ['REPLACE','ේ',['ෙ','්']],
	 ['REPLACE','ෛ',['ෙ','ෙ']],
	 ['REPLACE','ො',['ෙ','ා']],
	 ['REPLACE','ෝ',['ෙ','ා','්']],
	 ['REPLACE','ෝ',['ො','්']],
	 ['REPLACE','ෞ',['ෙ','ෟ']],
	 ['REPLACE','ෲ',['ෘ','ෘ']]
	 ]
	 
	delete_rules = [
	 ['IGNORE','\u200d',['්','*','ය']],
	 ['IGNORE','\u200d',['්','*','ර']]
	 ]
	 
	add_rules = [
	 ['IGNORE','\u200d',['ක','්','*','ය']],
	 ['IGNORE','\u200d',['බ','්','*','ය']],
	 ['IGNORE','\u200d',['ග','්','*','ය']],
	 ['IGNORE','\u200d',['ච','්','*','ය']],
	 ['IGNORE','\u200d',['ජ','්','*','ය']],
	 ['IGNORE','\u200d',['ට','්','*','ය']],
	 ['IGNORE','\u200d',['ඪ','්','*','ය']],
	 ['IGNORE','\u200d',['ණ','්','*','ය']],
	 ['IGNORE','\u200d',['ත','්','*','ය']],
	 ['IGNORE','\u200d',['ථ','්','*','ය']],
	 ['IGNORE','\u200d',['ද','්','*','ය']],
	 ['IGNORE','\u200d',['ධ','්','*','ය']],
	 ['IGNORE','\u200d',['න','්','*','ය']],
	 ['IGNORE','\u200d',['ප','්','*','ය']],
	 ['IGNORE','\u200d',['භ','්','*','ය']],
	 ['IGNORE','\u200d',['ම','්','*','ය']],
	 ['IGNORE','\u200d',['ය','්','*','ය']],
	 ['IGNORE','\u200d',['ල','්','*','ය']],
	 ['IGNORE','\u200d',['ව','්','*','ය']],
	 ['IGNORE','\u200d',['ශ','්','*','ය']],
	 ['IGNORE','\u200d',['ෂ','්','*','ය']],
	 ['IGNORE','\u200d',['ස','්','*','ය']],
	 ['IGNORE','\u200d',['හ','්','*','ය']],
	 ['IGNORE','\u200d',['ක','්','*','ර']],
	 ['IGNORE','\u200d',['ග','්','*','ර']],
	 ['IGNORE','\u200d',['ඝ','්','*','ර']],
	 ['IGNORE','\u200d',['ජ','්','*','ර']],
	 ['IGNORE','\u200d',['ත','්','*','ර']],
	 ['IGNORE','\u200d',['ද','්','*','ර']],
	 ['IGNORE','\u200d',['ප','්','*','ර']],
	 ['IGNORE','\u200d',['බ','්','*','ර']],
	 ['IGNORE','\u200d',['භ','්','*','ර']],
	 ['IGNORE','\u200d',['ම','්','*','ර']],
	 ['IGNORE','\u200d',['ව','්','*','ර']],
	 ['IGNORE','\u200d',['ශ','්','*','ර']],
	 ['IGNORE','\u200d',['ස','්','*','ර']],
	 ['IGNORE','\u200d',['හ','්','*','ර']]
	 ] 
	 
	word_char_list = list(word)
	is_changed =0
	
	 
	if(is_reverse ==1): 
		for x in range(len(rules)):
		
			if rules[x][0] =="REPLACE":
				
				wordtemp =""
				for y in range(len(word_char_list)):
					if len(rules[x][2])==2:
						if word_char_list[y] ==rules[x][2][0]:
							
							if y<len(word_char_list)-1:
								if word_char_list[y+1] ==rules[x][2][1]:
									wordtemp=wordtemp+rules[x][1]
									word_char_list[y+1] =""
									word_char_list[y] =""
									is_changed = 1
								else:
									wordtemp=wordtemp+word_char_list[y]
							else:
								wordtemp=wordtemp+word_char_list[y]
						else:
							wordtemp=wordtemp+word_char_list[y]
					if 	len(rules[x][2])==3:
						if word_char_list[y] ==rules[x][2][0]:
							
							if y<len(word_char_list)-2:
								if word_char_list[y+1] ==rules[x][2][1] and word_char_list[y+2] ==rules[x][2][2] :
									wordtemp=wordtemp+rules[x][1]
									word_char_list[y+1] =""
									word_char_list[y+2] =""
									word_char_list[y] =""
									is_changed = 1
								else:
									wordtemp=wordtemp+word_char_list[y]
							else:
								wordtemp=wordtemp+word_char_list[y]
						else:
							wordtemp=wordtemp+word_char_list[y]
				word_char_list = list(wordtemp)
	else:
		for x in range(len(rules)):
	
			if rules[x][0] =="REPLACE":
				
				wordtemp =""
				for y in range(len(word_char_list)):
					
					if word_char_list[y] ==rules[x][1]:
						for i in range(len(rules[x][2])):
							
							wordtemp=wordtemp+rules[x][2][i]
						is_changed = 1
					else:
						wordtemp=wordtemp+word_char_list[y]
				word_char_list = list(wordtemp)
	
	rule_lenth = len(delete_rules)
	for p in range(len(word_char_list)):

		wordtemp =""
		
		if word_char_list[p] =='\u200d':
			is_detected =0
			for q in range(rule_lenth):
				if delete_rules[q][0] =="IGNORE":
					x_location =-1
					ar_length = len(delete_rules[q][2])
					for px in range(ar_length):
						x_location =x_location+1
						if delete_rules[q][2][px] =="*":
							break
					no_char_before = x_location
					no_char_after = ar_length-x_location-1
					
					if p>=no_char_before and p<len(word_char_list)-no_char_after:
						if x_location==1:
							if word_char_list[p-1] == delete_rules[q][2][0] and word_char_list[p+1] == delete_rules[q][2][2]:
								is_detected=2
						if x_location==2:
							if word_char_list[p-2] == delete_rules[q][2][0] and word_char_list[p-1] == delete_rules[q][2][1] and word_char_list[p+1] == delete_rules[q][2][3]:
								is_detected=2
			if is_detected ==0:
				word_char_list[p]=""
				is_changed=2




	
	return [''.join(word_char_list),is_changed]
	# Function removes any unwanted symbols
	
	
if __name__ == '__main__':
	word=sys.argv[1].encode('unicode_escape').decode('utf-8')
	word = json.loads(r'"'+word+'"')

	word=unquote(word)
	
	word =clean_unicode(word,0)
	
	print(word[0])
	