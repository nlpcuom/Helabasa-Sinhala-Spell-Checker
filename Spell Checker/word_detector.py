import base64
import sys
import json
from urllib.parse import unquote
import morfessor


import hashlib

import datetime
from multiprocessing.connection import Listener
from array import array


def evaluate_model(sin_eng_main,sin_eng_sub,word_list,model,hashed_dic,affix_arra):

	
	
	for word in word_list:
		t = model.viterbi_segment(word[1])
	
		
		rword = convert_word(sin_eng_main,sin_eng_sub,word[0],2)
		
		if(len(t) >1):
			cnt=0
			for fi in t:
				cnt+=1
				
				if(cnt ==1):
			
					if(len(fi)>1):
						if (len(fi)==2):
							for i in range(len(fi)):
								if(i == 0):
									word_to_check = rword[0:len(fi[i])]
									affix_to_check = rword[len(fi[i]):]
								
									if(word_check_morfessor(word_to_check,hashed_dic)):
										if affix_to_check in affix_arra:
											return -1
										else:
											return 0
									else:
										return 0
						else:
							return 0
					else:
						return 0
				

	

def convert_word(sin_eng_main,sin_eng_sub,word,mode):
	if(len(word)>0):
		converted_word=""
		for ch in word:
			if(mode==1):
				if(ch in sin_eng_main):
					converted_word = converted_word+sin_eng_main[ch]
				elif(ch in sin_eng_sub):
					converted_word = converted_word+sin_eng_sub[ch].replace("α","")
					
				else:
					s =u''+ch+''
					
						
					if(s=='\u200d'):
						converted_word = converted_word+"¤"
					elif(s=='\n' or s=='\u200c'):
						converted_word = converted_word
					else:
						converted_word=""
						break
			elif(mode==2):
				if(ch in sin_eng_main):
					converted_word = converted_word+ch
				elif(ch in sin_eng_sub):
					converted_word = converted_word+ch
					
				else:
					s =u''+ch+''
					
						
					if(s=='\u200d'):
						converted_word = converted_word+ch
					elif(s=='\n' or s=='\u200c'):
						converted_word = converted_word
					else:
						converted_word=""
						break
				
		return converted_word 		
		
	else:
		return ""
		
		
def convert_word_alpha(sin_eng_main,sin_eng_sub,word):
	if(len(word)>0):
		converted_word_alpha =""
		for ch in word:
			if(ch in sin_eng_main):
				converted_word_alpha = converted_word_alpha+sin_eng_main[ch]
			elif(ch in sin_eng_sub):
				converted_word_alpha = converted_word_alpha+sin_eng_sub[ch]
			else:
				s =u''+ch+''
				
				if(s=='\u200d'):
					converted_word_alpha = converted_word_alpha+"¤"
				elif(s=='\n' or s=='\u200c'):
					converted_word_alpha = converted_word_alpha
				else:
					converted_word_alpha=""
					break
		return converted_word_alpha 		
		
	else:
		return ""

def develop_training_set(sin_eng_main,sin_eng_sub,wordlist_file):
	fword = open("converted_word.txt","a", encoding="utf-8")
	fword_a = open("converted_word_alpha.txt","a", encoding="utf-8")
	
	
	incorrect_char ={}
	with open(wordlist_file,"r", encoding="utf-8-sig") as fa:  
		line = "start"
		cnt = 1
		
		
		
		while line:
			arraix=[]
			if(cnt !=1):
				line = fa.readline()
				single_word_arr = line.split(" ")
				if(single_word_arr):
					if(len(single_word_arr) ==2):
						word = single_word_arr[1]
						frequency = single_word_arr[0]
						converted_word = ""
						converted_word_alpha =""
						
						for ch in word:
							if(ch in sin_eng_main):
								converted_word = converted_word+sin_eng_main[ch]
								converted_word_alpha = converted_word_alpha+sin_eng_main[ch]
							elif(ch in sin_eng_sub):
								converted_word = converted_word+sin_eng_sub[ch].replace("α","")
								converted_word_alpha = converted_word_alpha+sin_eng_sub[ch]
							else:
								s =u''+ch+''
								if(s not in incorrect_char):
									incorrect_char[s]=1
								else:
									incorrect_char[s]=incorrect_char[s]+1
									
								if(s=='\u200d'):
									converted_word = converted_word+"¤"
									converted_word_alpha = converted_word_alpha+"¤"
								elif(s=='\n' or s=='\u200c'):
									converted_word = converted_word
									converted_word_alpha = converted_word_alpha
								else:
									converted_word=""
									converted_word_alpha=""
									break
						if(converted_word !="" and converted_word_alpha !=""):
							fword.write(frequency+" "+converted_word+"\n");
							fword_a.write(frequency+" "+converted_word_alpha+"\n");
						
						
			cnt += 1

	fword.close()
	fword_a.close()

def construct_test_array(test_file):
	word_array =[]
	with open(test_file,"r", encoding="utf-8-sig") as fa:  
		line = "start"
		cnt = 1
		while line:
			arraix=[]
			if(cnt !=1):
				line = fa.readline().strip()
				if(len(line)>1):
					word_array.append(line)		
			cnt += 1
	return word_array

# Driver code 

def construct_affix_array(test_file):
	word_array ={}
	with open(test_file,"r", encoding="utf-8") as fa:  
		line = "start"
		cnt = 1
		while line:
			if(cnt !=1):
				line = fa.readline().strip()
				affix_arr = line.split(" ")
				if(affix_arr[0] =="0"):
					if affix_arr[1] in word_array:
						word_array[affix_arr[1]] =word_array[affix_arr[1]]+1
					else:
						word_array[affix_arr[1]] =1
			cnt += 1
	return word_array

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
		if word_char_list[qg] =='\u200c':
			word_char_list[qg]=''
			is_unicode =2
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
				word_char_list[p]=""
				is_unicode =2




	
	return [''.join(word_char_list),is_unicode]
	# Function removes any unwanted symbols
	





def get_hash(word):
    #encoded_word = word.encode('utf-8')
    #hash_object = hashlib.md5(encoded_word)
    #hex_dig = hash_object.hexdigest()
    #return hex_dig
    return word


def hashing_tagged_copus():
    filepath = "/var/www/html/morphy/foma/word_dms_hashx"
    a = {}
    with open(filepath, "r") as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] =1
    return a

def word_check_morfessor(word, hashed_dic):
    if get_hash(word) in hashed_dic:
        return 1
    else:
        return 0


def word_check(word, hashed_dic,sin_eng_main,sin_eng_sub,model,affix_arra,cleaning_state):
    if get_hash(word) in hashed_dic:
        if cleaning_state == 2:
            return -2
        else:
            return 1
    else:
        wordr= convert_word(sin_eng_main,sin_eng_sub,word,1)
        test_converted_words =[]
        test_converted_words.append([word,wordr])		
        spell_word = evaluate_model(sin_eng_main,sin_eng_sub,test_converted_words,model,hashed_dic,affix_arra)
        return spell_word
if __name__ == "__main__":
    io = morfessor.MorfessorIO()
    model = io.read_binary_model_file('/var/www/html/morphy/foma/model1.bin')
    sin_eng_main ={
	"අ":"a",
	"ආ":"A",
	"ඇ":"æ",
	"ඈ":"Æ",
	"ඉ":"i",
	"ඊ":"I",
	"උ":"u",
	"ඌ":"U",
	"ඍ":"R",
	"ඎ":"H",
	"ඏ":"î",
	"ඐ":"Î",
	"එ":"e",
	"ඒ":"E",
	"ඓ":"X",
	"ඔ":"o",
	"ඕ":"O",
	"ඖ":"Y",
	"ක":"k",
	"ඛ":"K",
	"ග":"g",
	"ඝ":"G",
	"ඞ":"F",
	"ඟ":"ß",
	"ච":"c",
	"ඡ":"C",
	"ජ":"j",
	"ඣ":"J",
	"ඤ":"ñ",
	"ඥ":"Ñ",
	"ඦ":"ç",
	"ට":"t",
	"ඨ":"T",
	"ඩ":"d",
	"ඪ":"D",
	"ණ":"N",
	"ඬ":"W",
	"ත":"q",
	"ථ":"Q",
	"ද":"v",
	"ධ":"V",
	"න":"n",
	"ඳ":"µ",
	"ප":"p",
	"ඵ":"P",
	"බ":"b",
	"භ":"B",
	"ම":"m",
	"ඹ":"M",
	"ය":"y",
	"ර":"r",
	"ල":"l",
	"ව":"w",
	"ශ":"S",
	"ෂ":"x",
	"ස":"s",
	"හ":"h",
	"ළ":"L",
	"ෆ":"f"
	}
    eng_sin_main = dict([(value, key) for key, value in sin_eng_main.items()]) 
	
    sin_eng_sub ={
	"ං":"αz",
	"ඃ":"αZ",
	"්":"αø",
	"ා":"αA",
	"ැ":"αæ",
	"ෑ":"αÆ",
	"ි":"αi",
	"ී":"αI",
	"ු":"αu",
	"ූ":"αU",
	"ෘ":"αR",
	"ෲ":"αH",
	"ෟ":"αî",
	"ෳ":"αÎ",
	"ෙ":"αe",
	"ේ":"αE",
	"ෛ":"αX",
	"ො":"αo",
	"ෝ":"αO",
	"ෞ":"αY"
	}
    eng_sin_sub = dict([(value, key) for key, value in sin_eng_sub.items()]) 
	

   
    wordlist_file="unique_word.txt"
    
    hashed_dic = hashing_tagged_copus()
    address = ('localhost', 34232) 
    affix_arra = construct_affix_array("/var/www/html/morphy/foma/uniqueaff.txt")
	
    while(1):
        with Listener(address, authkey=b'123@kbs') as listener:
            with listener.accept() as conn:

                data = conn.recv()
                data_arr = json.loads(data)
                wh_arr = []
                for i in data_arr:
                    wi_arr =[]
                    wi_arr.append(i[0])					
                    wi_arr.append(i[1])
                    clenuin=clean_unicode(i[1],0)
                    cleaning_state = clenuin[1]
                    clean_word = clenuin[0]					
                    wi_arr.append(word_check(clean_word,hashed_dic,sin_eng_main,sin_eng_sub,model,affix_arra,cleaning_state))
                    wh_arr.append(wi_arr)
                conn.send(json.dumps(wh_arr))





