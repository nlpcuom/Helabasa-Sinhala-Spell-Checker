# Python3 program for a word cleaner
# ver 1.0
import requests
import codecs
import operator
from collections import *
import re


def reverse_ucleaner(word):
	rules = [
	 ['REPLACE','ේ',['ෙ','්']],
	 ['REPLACE','ෛ',['ෙ','ෙ']],
	 ['REPLACE','ො',['ෙ','ා']],
	 ['REPLACE','ෝ',['ෙ','ා','්']],
	 ['REPLACE','ෝ',['ො','්']],
	 ['REPLACE','ෞ',['ෙ','ෟ']],
	 ['REPLACE','ෲ',['ෘ','ෘ']]
	 ]
	word_char_list = list(word)
	is_changed =0
	for x in range(len(rules)):
		
		if rules[x][0] =="REPLACE":
			
			wordtemp =""
			for y in range(len(word_char_list)):
				
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
			word_char_list = list(wordtemp)
	return [''.join(word_char_list),is_changed] 

def get_charsixteen(chari):
	uchar = chari.encode('unicode_escape').decode('utf-8')
	CharList = list(uchar)
	counti =0
	if 6 == len(CharList) & 6 == len(CharList):
		str_char_count = CharList[2] + CharList[3] + CharList[4] + CharList[5]
		counti = int(str_char_count, 16)
	return counti
	 
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
def clean_wordlist(wordlist):
	clean_list = []
	for word in wordlist:
		# update symbols string if there are any other unwanted symbols
		symbols = '!@#$%^&*()-+={[}]|\;:"<>?/., '
		new_word = ''
		for i in word:
			if i not in symbols:
				new_word += i
		if len(new_word) > 0:
			clean_list.append(new_word)
	return clean_list


# Driver code
if __name__ == '__main__':
    input_file = "dataset.txt"
    output_file = "output.txt"
    error_file = "error.txt"

    # Sinhala Unicode Range
    pax_min = 3456
    pax_max = 3583
    word_less_list =[]
    word_less_list_error =[]
    wordlist = []
    errorwordlist = []
    
    
    with open(input_file, "r", encoding="utf-8") as fi:
        for line in fi:
            words = line.lower().split()
            for each_word in words:
                x = list(each_word)

                minX = min(x)
                maxX = max(x)

                maxChar = maxX.encode('unicode_escape').decode('utf-8')
                maxCharList = list(maxChar)

                minChar = minX.encode('unicode_escape').decode('utf-8')
                minCharList = list(minChar)

                if 6 == len(maxCharList) & 6 == len(minCharList):

                    str_char_max = maxCharList[2] + maxCharList[3] + maxCharList[4] + maxCharList[5]
                    str_char_min = minCharList[2] + minCharList[3] + minCharList[4] + minCharList[5]

                    maxCharCount = int(str_char_max, 16)
                    minCharCount = int(str_char_min, 16)

                    if (pax_min <= minCharCount) & ((pax_max >= maxCharCount) | (maxCharCount == 8205) | (maxCharCount == 65279)):
                        wordist =clean_unicode(each_word,0)
                       
                        wordlist.append(wordist[0])
                        word_less_list.append(each_word)
                    else:
                        wordist =clean_unicode(each_word,0)
                        errorwordlist.append(wordist[0])
                        word_less_list_error.append(each_word)
                        
     
    wordlist = clean_wordlist(wordlist)
    errorwordlist = clean_wordlist(errorwordlist)
    word_less_list = clean_wordlist(word_less_list)
    word_less_list_error = clean_wordlist(word_less_list_error)
     

    print(len(wordlist))
    print(len(errorwordlist))

    f = open(output_file, 'w', encoding="utf-8")
    for x in range(len(wordlist)):
        f.write(wordlist[x])
        f.write( "\n")
    f.close()


	

