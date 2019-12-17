import codecs
import requests
import base64
import operator
from collections import *
import re
import sys
import json
from urllib.parse import unquote

from pyfasttext import FastText

from itertools import permutations

import hashlib

import datetime
from multiprocessing.connection import Listener
from array import array

import math

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
	
#
# def hashing_tagged_copus():  # hash tagging function for all the unique words in the tagged corpus
#     filepath = "tagged.txt"
#     a = {}
#     with open(filepath) as fp:
#         for line in fp:
#             x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
#             if (len(x) == 2):
#                 if x[0] not in a:
#                     a[x[0]] = 0
#                 else:
#                     a[x[0]] += 1
#     hashed_dic = {}
#
#     for i in a:
#         encoded_word = i.encode('utf-8')
#         hash_object = hashlib.sha512(encoded_word)  # hash each word in the dictionary
#         hex_dig = hash_object.hexdigest()
#         if type(a[i]) is int:
#             hashed_dic[hex_dig] = a[i]
#         else:
#             hashed_dic[hex_dig] = 0
#
#     return hashed_dic/home/kalana

def get_hash(word):
#    encoded_word = word.encode('utf-8')
#    hash_object = hashlib.sha512(encoded_word)
#    hex_dig = hash_object.hexdigest()
#    return hex_dig
    return word


def get_hash_md5(word):
    encoded_word = word.encode('utf-8')
    hash_object = hashlib.md5(encoded_word)
    hex_dig = hash_object.hexdigest()
    return hex_dig
    

def hashing_tagged_copus():
#    filepath = "/var/www/html/morphy/fasttext/hashed_dic"
    filepath = "/var/www/html/morphy/fasttext/unique_word_frequency"
    a={}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = int(x[1])
    return a
    
    
def hashing_spell_checking_dic():
    filepath = "/var/www/html/morphy/fasttext/word_dms_hash"
    a = {}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = int(x[1])
    return a
    
    
def reading_other_file():
    filepath = "/var/www/html/morphy/fasttext/other.txt"
    a = {}
    with open(filepath,"r",encoding="utf-8") as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = 1
    return a

def is_papili_missing_word(word1, word2):
    array = []
    for i in word2:
        array.append(i)
    for i in word1:
        if i in array:
            array.remove(i)

    if len(array) > 0:
        if array[0] == 'ු' or array[0] == 'ූ' or array[0] == '්' or array[0] == 'ා' or array[0] == 'ි' or array[0] == 'ී' or array[0] == 'ී' or array[0] == 'ෑ' or array[0] == 'ැ':
            return True
        else:
            return False
    else:
        return False


def is_joiner_missing_word(word1, word2):
    array = []
    for i in word2:
        array.append(i)
    for i in word1:
        if i in array:
            array.remove(i)

    if len(array) > 0:
        if array[0] == '\u200d':
            return True
        else:
            return False
    else:
        return False


def split_check(words, word):
    first_word =[]
    last_word = []
    space_suggestion = {}
#    for i in words:
#       if i[0] != '' and word != '' and i[0][0] != '' and i[0][0] == word[0] and i[0] in word:
#           if get_hash(i[0]) in hashed_dic and get_hash_md5(i[0]) in spell_checking_dic:
#               first_word.append(i[0])
#       if i[0] != '' and word != '' and i[0][-1] != '' and i[0][-1] == word[-1] and i[0] in word:
#           if get_hash(i[0]) in hashed_dic and get_hash_md5(i[0]) in spell_checking_dic:
#               last_word.append(i[0])
                
#   for i in first_word:
#       for j in last_word:
#           if i+j == word:
#               s = i + ' ### ' + j
#               space_suggestion[s]=1
    dic_words = {}
    for i in words:
        dic_words[i[0]] = 0
    
                
    for i in range(1,len(word)):
        if get_hash_md5(word[:i]) in spell_checking_dic and get_hash_md5(word[i:]) in spell_checking_dic:
            if word[:i] in dic_words and word[i:] in dic_words:
                space_suggestion[word[:i] + ' ' + word[i:]] = 1
#            elif word[:i] in dic_words:
#                space_suggestion[word[:i] + ' 2' + word[i:]] = 2
#            elif word[i:] in dic_words:
#                space_suggestion[word[:i] + '3 ' + word[i:]] = 3
#            else:
#                space_suggestion[word[:i] + ' 4' + word[i:]] = 4

        if word[-i:] in other_file and get_hash_md5(word[:-i]) in spell_checking_dic:
            space_suggestion[word[:-i] + ' ' + word[-i:]] = 5  
                         
                
    return space_suggestion


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
    
    
def get_modified_input_word(word):
    new_sin_word = word
    symbols = ['ු', 'ැ' , 'ි', '්', 'ං','ෙ' ]
    if word[0] in symbols:
        new_sin_word = swap(word,0,1)
    if '්යා' in word and 'ර්යා' not in word:
        new_sin_word = new_sin_word.replace('්යා', '්‍යා')
    if '්ය' in word and 'ර්ය' not in word:
        new_sin_word = new_sin_word.replace('්ය', '්‍ය')

    if 'බ්රිී' in word:
        new_sin_word = new_sin_word.replace('බ්රිී', 'බ්‍රි')
    if 'ක්රි' in word:
        new_sin_word = new_sin_word.replace('ක්රි', 'ක්‍රි')
    if 'ප්රි' in word:
        new_sin_word = new_sin_word.replace('ප්රි', 'ප්‍රි')
    if 'ග්රි' in word:
        new_sin_word = new_sin_word.replace('ග්රි', 'ග්‍රි')
    if 'ද්රි' in word:
        new_sin_word = new_sin_word.replace('ද්රි', 'ද්‍රි')

    if 'බ්රී' in word:
        new_sin_word = new_sin_word.replace('බ්රී', 'බ්‍රී')
    if 'ක්රී' in word:
        new_sin_word = new_sin_word.replace('ක්රී', 'ක්‍රී')
    if 'ප්රී' in word:
        new_sin_word = new_sin_word.replace('ප්රී', 'ප්‍රී')
    if 'ග්රී' in word:
        new_sin_word = new_sin_word.replace('ග්රී', 'ග්‍රී')
    if 'ද්රී' in word:
        new_sin_word = new_sin_word.replace('ද්රී', 'ද්‍රී')

    if 'බ්ර' in word:
        new_sin_word = new_sin_word.replace('බ්ර', 'බ්‍ර')
    if 'ප්ර' in word:
        new_sin_word = new_sin_word.replace('ප්ර', 'ප්‍ර')
    if 'ක්ර' in word:
        new_sin_word = new_sin_word.replace('ක්ර', 'ක්‍ර')
    if 'ග්ර' in word:
        new_sin_word = new_sin_word.replace('ග්ර', 'ග්‍ර')
    if 'ද්ර' in word:
        new_sin_word = new_sin_word.replace('ද්ර', 'ද්‍ර')

    return new_sin_word


def show_entry_fields():  # Display box function

    #print(suggestion_generator(e1.get()))
    msg = messagebox.showinfo("Hello_Python", suggestion_generator(e1.get()))


def call_counter(func):  # Part of the levenshtein minimum edit distance algorithm
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__
    return helper


def memoize(func):
    mem = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]

    return memoizer


@call_counter
@memoize
def levenshtein(s, t):  # Minimum edit distance algorithm
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])
    return res


# #print(levenshtein("ළකුණ", "ලකුණු"))
# #print("The function was called " + str(levenshtein.calls) + " times!")

def get_permutations(word, changed_letters):
    all = changed_letters
    indices = []
    word_lst = []
    for i in word:  # put all the letters in the word to a list
        word_lst.append(i)
    for i in range(len(word_lst)):
        if word_lst[i] in all:  # get the index numbers of the Nana Lala letters of that particular word
            indices.append(i)
    final = []
    for i in range(1, len(indices) + 1):

        perm = permutations(indices, i)  # Generate the permutations

        # Print the obtained permutations
        for i in list(perm):
            lst = []
            for j in i:
                lst.append(j)
            lst.sort()
            if lst not in final:
                final.append(lst)
    return word_lst, final


def get_Bindu_words(word):
    all = ['න', 'ං']
    permutated_words = []
    word_lst, final = get_permutations(word, all)
    #print(word_lst)
    #print(final)
    for i in final:
        per_word = ['']
        inside_once = False
        for j in range(len(i)):
            #print(i[j])
            #print(len(word_lst))
            if word_lst[i[j]] == 'න' and i[j] < len(word_lst)-2 and word_lst[i[j]+1] == '්':
                if inside_once == False:
                    per_word = word_lst.copy()
                    inside_once = True
                #print("LLLMMMM")
                per_word[i[j]] = 'ං'
                per_word[i[j]+1] = ''

        concat = ''
        for k in per_word:
            concat += k
        hash_dig = get_hash(concat)
        if (hash_dig in hashed_dic) and (concat not in permutated_words):
            permutated_words.append(concat)
    return permutated_words
            # if word_lst[i[j]] == 'ං':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #     per_word[i[j]] = 'න'
            #     per_word[i[j] + 1] = '්'


def nana_lala(word):  # function which generates permutations of a given word
    # Get all permutations of length 2
    # and length 2
    all = ['න', 'ණ', 'ල', 'ළ', 'ස', 'ශ', 'ෂ', 'ත', 'ථ', 'බ', 'භ', 'ද', 'ඳ', 'ධ', 'ග', 'ට', 'ඨ', 'ච', 'ඡ', 'ජ', 'ක', 'ඛ', 'ග', 'ඝ', 'ජ', 'ඣ', 'ප', 'ඵ', 'ඩ', 'ඪ']
    # simple = ['න', 'ල', 'ශ', 'ත', 'බ', 'ද']
    # capital = ['ණ', 'ළ', 'ෂ', 'ථ', 'භ', 'ධ']
    # indices = []
    # word_lst = []
    permutated_words = []
    # for i in word:  # put all the letters in the word to a list
    #     word_lst.append(i)
    # for i in range(len(word_lst)):
    #     if word_lst[i] in all:  # get the index numbers of the Nana Lala letters of that particular word
    #         indices.append(i)
    # final = []
    # for i in range(1, len(indices) + 1):
    #
    #     perm = permutations(indices, i)  # Generate the permutations
    #
    #     # Print the obtained permutations
    #     for i in list(perm):
    #         lst = []
    #         for j in i:
    #             lst.append(j)
    #         lst.sort()
    #         if lst not in final:
    #             final.append(lst)
    word_lst, final = get_permutations(word, all)
    for i in final:
        per_word = ['']
        for j in range(len(i)):
            dha_word = False
            if word_lst[i[j]] == 'න':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ණ'
                per_word2[i[j]] = 'ණ'

            if word_lst[i[j]] == 'ණ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'න'
                per_word2[i[j]] = 'න'

            if word_lst[i[j]] == 'ල':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ළ'
                per_word2[i[j]] = 'ළ'

            if word_lst[i[j]] == 'ළ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ල'
                per_word2[i[j]] = 'ල'

            if word_lst[i[j]] == 'ශ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ෂ'
                per_word2[i[j]] = 'ස'
                dha_word = True

            if word_lst[i[j]] == 'ෂ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'
                per_word2[i[j]] = 'ස'
                dha_word = True

            if word_lst[i[j]] == 'ස':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'
                per_word2[i[j]] = 'ෂ'
                dha_word = True

            if word_lst[i[j]] == 'ත':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ථ'
                per_word2[i[j]] = 'ථ'

            if word_lst[i[j]] == 'ථ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ත'
                per_word2[i[j]] = 'ත'

            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'භ'
                per_word2[i[j]] = 'භ'

            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'බ'
                per_word2[i[j]] = 'බ'

            if word_lst[i[j]] == 'ද':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ධ'
                per_word2[i[j]] = 'ඳ'
                dha_word = True

            if word_lst[i[j]] == 'ධ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ද'
                per_word2[i[j]] = 'ඳ'
                dha_word = True
                
            if word_lst[i[j]] == 'ඳ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ද'
                per_word2[i[j]] = 'ධ'
                dha_word = True

            if word_lst[i[j]] == 'ග':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඟ'
                per_word2[i[j]] = 'ඟ'

            # if word_lst[i[j]] == 'දු':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #         per_word2 = word_lst.copy()
            #     per_word[i[j]] = 'ඳු'
            #
            # if word_lst[i[j]] == 'ඳු':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #         per_word2 = word_lst.copy()
            #     per_word[i[j]] = 'දු'

            #if word_lst[i[j]] == 'ු':
            #   if j <= 0:
            #       per_word = word_lst.copy()
            #       per_word2 = word_lst.copy()
            #   per_word[i[j]] = 'ූ'
            #   per_word2[i[j]] = 'ූ'

            #if word_lst[i[j]] == 'ූ':
            #   if j <= 0:
            #       per_word = word_lst.copy()
            #       per_word2 = word_lst.copy()
            #   per_word[i[j]] = 'ු'
            #   per_word2[i[j]] = 'ු'

            if word_lst[i[j]] == 'ට':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඨ'
                per_word2[i[j]] = 'ඨ'

            if word_lst[i[j]] == 'ඨ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ට'
                per_word2[i[j]] = 'ට'

            if word_lst[i[j]] == 'ඡ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ච'
                per_word2[i[j]] = 'ජ'
                dha_word = True

            if word_lst[i[j]] == 'ච':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'
                per_word2[i[j]] = 'ඡ'

            if word_lst[i[j]] == 'ජ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'
                per_word2[i[j]] = 'ඡ'
                
            if word_lst[i[j]] == 'ක':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඛ'
                per_word2[i[j]] = 'ඛ'

            if word_lst[i[j]] == 'ඛ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ක'
                per_word2[i[j]] = 'ක'
                
            if word_lst[i[j]] == 'ග':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඝ'
                per_word2[i[j]] = 'ඝ'

            if word_lst[i[j]] == 'ඝ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ග'
                per_word2[i[j]] = 'ග'
                
            if word_lst[i[j]] == 'ජ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඣ'
                per_word2[i[j]] = 'ඣ'

            if word_lst[i[j]] == 'ඣ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ජ'
                per_word2[i[j]] = 'ජ'
                
            if word_lst[i[j]] == 'ප':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඵ'
                per_word2[i[j]] = 'ඵ'

            if word_lst[i[j]] == 'ඵ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ප'
                per_word2[i[j]] = 'ප'
                
            if word_lst[i[j]] == 'ඩ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඪ'
                per_word2[i[j]] = 'ඪ'

            if word_lst[i[j]] == 'ඪ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඩ'
                per_word2[i[j]] = 'ඩ'

        concat = ''
        for k in per_word:
            concat += k
        hash_dig = get_hash(concat)
        md5_hash_dig = get_hash_md5(concat)
        if hash_dig in hashed_dic and md5_hash_dig in spell_checking_dic:
            permutated_words.append(concat)
        modified_concat = get_modified_input_word(concat)
        hash_dig = get_hash(modified_concat)
        md5_hash_dig = get_hash_md5(modified_concat)
        if hash_dig in hashed_dic and md5_hash_dig in spell_checking_dic:
            permutated_words.append(modified_concat)
        if dha_word:
            concat2 = ''
            for k in per_word2:
                concat2 += k

            hash_dig = get_hash(concat2)
            md5_hash_dig = get_hash_md5(concat2)
            if hash_dig in hashed_dic and md5_hash_dig in spell_checking_dic:
                permutated_words.append(concat2)
            modified_concat2 = get_modified_input_word(concat2)
            hash_dig = get_hash(modified_concat2)
            md5_hash_dig = get_hash_md5(md5_hash_dig)
            if hash_dig in hashed_dic and md5_hash_dig in spell_checking_dic:
                permutated_words.append(modified_concat2)

    return permutated_words
    
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1]
    str1=''
    for i in list:
        str1+=i

    return str1
    
def get_swapped_words(word):
    lst = []
    stuff1 = list(word)
    stuff2 = stuff1.copy()
    if '්' in stuff1:
        pos = word.index('්')
        str1=''
        str2=''
        if len(word)-2>=pos:
            str1 = swapPositions(stuff1, pos, pos+1)
        if pos>0:
            str2 = swapPositions(stuff2, pos, pos-1)
        if get_hash(str1) in hashed_dic and get_hash_md5(str1) in spell_checking_dic:
            lst.append(str1)
        if get_hash(str2) in hashed_dic and get_hash_md5(str2) in spell_checking_dic:
            lst.append(str2)
        
    return lst


def get_RU_replaced_words(word):
    lst=[]
    if 'රැ' in word:
        w1= word.replace('රැ','රු')
        if get_hash(w1) in hashed_dic and get_hash_md5(w1) in spell_checking_dic:
            lst.append(w1)
    if 'රු' in word:
        w2= word.replace('රු','රැ')
        if get_hash(w2) in hashed_dic and get_hash_md5(w2) in spell_checking_dic:
            lst.append(w2)
    if 'රෑ' in word:
        w3= word.replace('රෑ','රූ')
        if get_hash(w3) in hashed_dic and get_hash_md5(w3) in spell_checking_dic:
            lst.append(w3)
    if 'රූ' in word:
        w4= word.replace('රූ','රෑ')
        if get_hash(w4) in hashed_dic and get_hash_md5(w4) in spell_checking_dic:
            lst.append(w4)
            
    return lst
    
    
def suggestion_generator(sinhala_word):
    # model = FastText('sinhala_all2.bin')
    a = datetime.datetime.now()
    #    #print(model.similarity('බල්ල', 'බල්ලා'))
    user_sin_word = sinhala_word
    sin_word = get_modified_input_word(sinhala_word)

    permutated_nana_lala_sin_word = nana_lala(sin_word)
    permutated_bindu_sin_word = get_Bindu_words(sin_word)

    permutated_sin_word = permutated_nana_lala_sin_word + permutated_bindu_sin_word
    words = model.nearest_neighbors(sin_word, k=2000)
    minnnnn = []
    min1 = {}
    min2 = {}
    min3 = {}
    min_other = {}
    min = 1000000000
    max_frequency = 0
    # #print(words)
    suggested_words = []
    space_suggestion = split_check(words, sin_word)
    swapped_words = get_swapped_words(sin_word)
    for i in swapped_words:
        words.append((i,1000))
        
    RU_replaced_words = get_RU_replaced_words(sin_word)
    for i in RU_replaced_words:
        words.append((i,1000))
        
    final_dic = {}
    for i in words:
        punc = [',','.','/','?']
        punctuation_free_word = ''
        for k in i[0]:
            if k not in punc:
                punctuation_free_word += k


        if get_hash(punctuation_free_word) in hashed_dic and get_hash_md5(punctuation_free_word) in spell_checking_dic:
        #if get_hash(punctuation_free_word) in hashed_dic:
            minimum_edit_distance = levenshtein(punctuation_free_word, sin_word)
            final_dic[punctuation_free_word] = math.log((hashed_dic[get_hash(punctuation_free_word)]+1)) #add or remove the log

            if punctuation_free_word in permutated_sin_word:
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] *= 10**1.35
                final_dic[punctuation_free_word] *= 1.35

            if is_papili_missing_word(sin_word, punctuation_free_word) and minimum_edit_distance<=1:
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] *= 10**1.3
                final_dic[punctuation_free_word] *= 1.3

            if is_joiner_missing_word(sin_word, punctuation_free_word):
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] *= 10**1.12
                final_dic[punctuation_free_word] *= 1.12

            #minimum_edit_distance = levenshtein(punctuation_free_word, sin_word)

            if punctuation_free_word in permutated_sin_word:
                ##print(final_dic[punctuation_free_word])
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] /= 10*minimum_edit_distance
                final_dic[punctuation_free_word] /= minimum_edit_distance
                ##print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
                ##print(punctuation_free_word)
                ##print(hashed_dic[get_hash('ළඟයි')])
            elif minimum_edit_distance<3:
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] /= 10**minimum_edit_distance
                final_dic[punctuation_free_word] /= minimum_edit_distance**2
            else:
                #final_dic[punctuation_free_word+str(hashed_dic[get_hash(punctuation_free_word)])] /= 100**minimum_edit_distance
                final_dic[punctuation_free_word] /= minimum_edit_distance**3


    sorted_final_dic2 = sorted(final_dic.items(), key=lambda kv: kv[1])[::-1]
    sorted_final_dic = []
    
    for i in sorted_final_dic2:
        sorted_final_dic.append((i[0],i[1]))


    max_frequency = 0
    max_word = ''
    #print(permutated_sin_word)
    for i in permutated_sin_word:
        hex_dig = get_hash(i)
        if hex_dig in hashed_dic:
            if hashed_dic[hex_dig] / 10 ** levenshtein(i, sin_word) > max_frequency:
                max_frequency = hashed_dic[hex_dig] / 10 ** levenshtein(i, sin_word)
                max_word = i

    if max_word != '' and max_word not in final_dic:
        sorted_final_dic.insert(0, (max_word, max_frequency))
    elif max_word != '' and max_word in final_dic and (max_word, final_dic[max_word]) not in sorted_final_dic[:5]:
        sorted_final_dic.insert(0, (max_word, max_frequency))
        
    if sin_word != '' and get_hash_md5(sin_word) in spell_checking_dic and get_hash(sin_word) in hashed_dic and (sin_word, hashed_dic[get_hash(sin_word)]) not in sorted_final_dic[:5]:
        sorted_final_dic.insert(0, (sin_word, max_frequency))
        
    sorted_final_dic = sorted(space_suggestion.items(), key=lambda kv: kv[1]) + sorted_final_dic        
    
    
    return sorted_final_dic[:5]
	

def sync_time():
    a1 = datetime.datetime.now()
    return a1



if __name__ == "__main__":
    
    m1 =sync_time()
    model = FastText('/var/www/html/morphy/fasttext/sinhala_all2.bin')
    m2 =sync_time()
    # model = FastText('result/fil9.bin')
    d1=sync_time()
    hashed_dic = hashing_tagged_copus()
    spell_checking_dic = hashing_spell_checking_dic()
    other_file = reading_other_file()
    d2=sync_time()
    address = ('localhost', 25035)     
	
	
    while(1):
        with Listener(address, authkey=b'123@kbs') as listener:
            with listener.accept() as conn:
				
				
                data = conn.recv()
                data = clean_unicode(data,0)[0]
                foutput = suggestion_generator(data)
                conn.send(json.dumps(foutput))
		
	

