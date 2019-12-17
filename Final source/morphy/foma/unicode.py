import base64
import sys
import json
from urllib.parse import unquote
import morfessor


import hashlib

import datetime
from multiprocessing.connection import Listener
from array import array

def clean_unicode(word,is_reverse =0):
	word_map={}
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
	is_detected =0
	is_unicode =0 
	
	 
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
	
	for qg in range(len(word_char_list)):
		map_body = {"char":"","type":"","color":""}
		if word_char_list[qg] =='\u200c':
			
			is_unicode =2
			map_body["char"]=word_char_list[qg]
			map_body["type"]="2"
			map_body["color"]="#9e54ff"
			
			word_char_list[qg]=''
			
			
			word_map[str(qg)] = map_body
		else:
			map_body["char"]=word_char_list[qg]
			map_body["type"]="0"
			map_body["color"]="#adadad"
			word_map[str(qg)] = map_body
			
	for p in range(len(word_char_list)):

		wordtemp =""
		
		if word_char_list[p] =='\u200d':
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
								is_detected=1
						if x_location==2:
							if word_char_list[p-2] == delete_rules[q][2][0] and word_char_list[p-1] == delete_rules[q][2][1] and word_char_list[p+1] == delete_rules[q][2][3]:
								is_detected=1
			if is_detected ==0:
				map_body = {"char":"","type":"","color":""}
			
				
				map_body["char"]=word_char_list[p]
				map_body["type"]="1"
				map_body["color"]="#9e54ff"
			
				word_map[str(p)] = map_body
				word_char_list[p]=""
				is_unicode =2



	return_dic = {"cword":"","word":"","error":"","word_map":{}}
	return_dic["cword"]="".join(word_char_list)
	return_dic["word"]=word
	return_dic["error"]=str(is_unicode)
	return_dic["word_map"]=word_map
	
	
	return return_dic
	
if __name__ == "__main__":
	
	word_arr=clean_unicode(sys.argv[1])
	
	print(word_arr)
	

