
import base64
import sys
import json
from urllib.parse import unquote

from pyfasttext import FastText

from itertools import permutations

import hashlib

import datetime
from multiprocessing.connection import Listener
from array import array


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
#     return hashed_dic

def get_hash(word):
    encoded_word = word.encode('utf-8')
    hash_object = hashlib.sha512(encoded_word)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def hashing_tagged_copus():
    filepath = "/var/www/html/morphy/fasttext/hashed_dic"
    a = {}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = int(x[1])
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


def split_check(words,word):
    first_word =[]
    last_word = []
    space_suggestion = []
    for i in words:
        if i[0] != '' and word != '' and i[0][0] != '' and i[0][0] == word[0] and i[0] in word:
            first_word.append(i[0])
        if i[0] != '' and word != '' and i[0][-1] != '' and i[0][-1] == word[-1] and i[0] in word:
            last_word.append(i[0])
    for i in first_word:
        for j in last_word:
            if i+j==word:
                s = i + ' '+ j
                space_suggestion.append((s,0))
    return space_suggestion


def get_modified_input_word(word):
    new_sin_word = word
    if 'ජ්යා' in word:
        new_sin_word = new_sin_word.replace('ජ්යා', 'ජ්‍යා')
    if 'බ්රිී' in word:
        new_sin_word = new_sin_word.replace('බ්රිී', 'බ්‍රි')
    if 'ද්යා' in word:
        new_sin_word = new_sin_word.replace('ද්යා', 'ද්‍යා')

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
    all = ['න', 'ණ', 'ල', 'ළ', 'ශ', 'ෂ', 'ත', 'ථ', 'බ', 'භ', 'ද', 'ධ', 'ග', 'ඳු', 'දු', 'ු', 'ූ', 'ට', 'ඨ', 'ච', 'ඡ', 'ජ']
    # simple = ['න', 'ල', 'ශ', 'ත', 'බ', 'ද']
    # capital = ['ණ', 'ළ', 'ෂ', 'ථ', 'භ', 'ධ']
    # indices = []
    # word_lst = []
    permutated_words = [word]
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
            Dhaword = False
            if word_lst[i[j]] == 'න':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ණ'

            if word_lst[i[j]] == 'ණ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'න'

            if word_lst[i[j]] == 'ල':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ළ'

            if word_lst[i[j]] == 'ළ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ල'

            if word_lst[i[j]] == 'ශ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ෂ'

            if word_lst[i[j]] == 'ෂ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'

            if word_lst[i[j]] == 'ත':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ථ'

            if word_lst[i[j]] == 'ථ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ත'

            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'භ'

            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'බ'

            if word_lst[i[j]] == 'ද':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ධ'
                per_word2[i[j]] = 'ඳ'
                Dhaword = True
            if word_lst[i[j]] == 'ධ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ද'

            if word_lst[i[j]] == 'ග':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඟ'

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

            if word_lst[i[j]] == 'ු':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ූ'

            if word_lst[i[j]] == 'ූ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ු'

            if word_lst[i[j]] == 'ට':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඨ'

            if word_lst[i[j]] == 'ඨ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ට'

            if word_lst[i[j]] == 'ඡ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ච'
                per_word2[i[j]] = 'ජ'
                Dhaword = True
            if word_lst[i[j]] == 'ච':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'

            if word_lst[i[j]] == 'ජ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'

        concat = ''
        for k in per_word:
            concat += k
        if Dhaword:
            concat2 = ''
            for k in per_word2:
                concat2 += k

            hash_dig = get_hash(concat2)
            if hash_dig in hashed_dic:
                permutated_words.append(concat2)
        hash_dig = get_hash(concat)
        if hash_dig in hashed_dic:
            permutated_words.append(concat)
    #print(permutated_words)
    #print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
    return permutated_words




def suggestion_generator(sinhala_word):
    # model = FastText('sinhala_all2.bin')
    a = datetime.datetime.now()
    #    #print(model.similarity('බල්ල', 'බල්ලා'))
    user_sin_word = sinhala_word
    sin_word = get_modified_input_word(sinhala_word)

    permutated_nana_lala_sin_word = nana_lala(sin_word)
    permutated_bindu_sin_word = get_Bindu_words(sin_word)

    permutated_sin_word = permutated_nana_lala_sin_word + permutated_bindu_sin_word
    #print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
    #print(permutated_sin_word)
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
    space_suggestion = split_check(words,sin_word)
    for i in words:
       
        punc = [',','.','/','?']
        punctuation_free_word = ''
        for k in i[0]:
            if k not in punc:
                punctuation_free_word += k

        minimum_edit_distance = levenshtein(punctuation_free_word, sin_word)
        # if get_hash(punctuation_free_word) in hashed_dic and minimum_edit_distance < min:
        #     #print(minimum_edit_distance)
        #     min = minimum_edit_distance
        #     max_frequency = hashed_dic[get_hash(punctuation_free_word)]
        #     minnnnn[punctuation_free_word] = max_frequency
        if get_hash(punctuation_free_word) in hashed_dic and minimum_edit_distance <= min:
            # #print(minimum_edit_distance)
            min = minimum_edit_distance
            max_frequency = hashed_dic[get_hash(punctuation_free_word)]
            if min == 1:
                min1[punctuation_free_word] = max_frequency
            elif min == 2:
                min2[punctuation_free_word] = max_frequency
            elif min == 3:
                min3[punctuation_free_word] = max_frequency
            else:            #methna tradeoff ekk tyno minimum_edit_distance eka dadnawada max_frequency ddanawadda kiyla
                min_other[punctuation_free_word] = max_frequency
            # #print("K")
            # #print(max_frequency)
        if minimum_edit_distance <= 1 or (get_hash(punctuation_free_word) in hashed_dic and minimum_edit_distance == 2 and hashed_dic[get_hash(punctuation_free_word)] > 1400):
            # copy_suggested_words.remove(i)
            suggested_words.append(punctuation_free_word)
        if 'ං' in punctuation_free_word and minimum_edit_distance <= 3 and get_hash(punctuation_free_word) in hashed_dic and hashed_dic[get_hash(punctuation_free_word)] > 1000:
            suggested_words.append(punctuation_free_word)
        if 'ද්‍ර' in punctuation_free_word and minimum_edit_distance <= 2 and get_hash(punctuation_free_word) in hashed_dic and hashed_dic[get_hash(punctuation_free_word)] > 100:
            suggested_words.append(punctuation_free_word)
        if 'බ්‍රි' in punctuation_free_word and minimum_edit_distance <= 2 and get_hash(punctuation_free_word) in hashed_dic and hashed_dic[get_hash(punctuation_free_word)] > 100:
            suggested_words.append(punctuation_free_word)
    sorted_min1 = sorted(min1.items(), key=lambda kv: kv[1])[::-1]
    sorted_min2 = sorted(min2.items(), key=lambda kv: kv[1])[::-1]
    sorted_min3 = sorted(min3.items(), key=lambda kv: kv[1])[::-1]
    sorted_min_other = sorted(min_other.items(), key=lambda kv: kv[1])[::-1]
    minnnnn = sorted_min1 + sorted_min2 + sorted_min3 + sorted_min_other
    # #print(minnnnn)
    #print("KKKKKKKKKKKKKKKKKKKKKKK")
    #print(suggested_words)
    copy_suggested_words = suggested_words.copy()
    priority_suggested_words = {}
    for i in suggested_words:
        if i in permutated_sin_word:
            hex_dig = get_hash(i)
            if hex_dig not in hashed_dic:
                copy_suggested_words.remove(i)
            else:
                copy_suggested_words.remove(i)
                priority_suggested_words[i] = hashed_dic[hex_dig]  # Nana Lala error word are in the priority words list
    #print("HHHHHHHHHHHHHHHHHHHHHHh")
    #print(priority_suggested_words)
    #print(suggested_words)
    frequency_dic = {}
    for i in copy_suggested_words:
        hex_dig = get_hash(i)
        if hex_dig not in hashed_dic:
            copy_suggested_words.remove(i)
        else:
            frequency_dic[i] = hashed_dic[hex_dig]

    sorted_frequency_dic = sorted(frequency_dic.items(), key=lambda kv: kv[1])
    v1 = sorted_frequency_dic[::-1]
    v1_copy = v1.copy()
    # convertWordToArray = []
    # #print(sin_word)
    # #print(sinhala_word)
    # for i in sin_word:
    #     convertWordToArray.append(i)
    # #print(convertWordToArray)
    ispiliWords = {}
    for i in v1_copy:
        if is_papili_missing_word(sin_word, i[0]):
            #print(i[0])
            ispiliWords[i[0]] = i[1]/10**levenshtein(i[0], sin_word)
            v1.remove(i)

    v3 = sorted(ispiliWords.items(), key=lambda kv: kv[1])

    for i in v3:
        v1.insert(0, i)
    # #print(v1)

    sorted_frequency_dic = sorted(priority_suggested_words.items(), key=lambda kv: kv[1])
    v2 = sorted_frequency_dic[::-1]

    max = 0
    max_word = ''
    #print(permutated_sin_word)
    for i in permutated_sin_word:
        hex_dig = get_hash(i)
        if hex_dig in hashed_dic:
            if hashed_dic[hex_dig] > max:
                max = hashed_dic[hex_dig]
                max_word = i
    # #print(max)

    # #print(v2)
    if '්ය්‍ය' in user_sin_word:
        new_sin_word = user_sin_word.replace('්ය්‍ය', '්‍ය')
        if get_hash(new_sin_word) in hashed_dic:
            if (new_sin_word, hashed_dic[get_hash(new_sin_word)]) in v2:
                v2.remove((new_sin_word, hashed_dic[get_hash(new_sin_word)]))
            if (new_sin_word, hashed_dic[get_hash(new_sin_word)]) in v1:
                v1.remove((new_sin_word, hashed_dic[get_hash(new_sin_word)]))
                #print(v2)
            v2.insert(0, (new_sin_word, hashed_dic[get_hash(new_sin_word)]))
            #print(v2)
    if 'ද්යා' in user_sin_word:
        new_sin_word = user_sin_word.replace('ද්යා', 'ද්‍යා')
        if get_hash(new_sin_word) in hashed_dic:
            #print(hashed_dic[get_hash(new_sin_word)])

            if (new_sin_word, hashed_dic[get_hash(new_sin_word)]) in v2:
                v2.remove((new_sin_word, hashed_dic[get_hash(new_sin_word)]))
            if (new_sin_word, hashed_dic[get_hash(new_sin_word)]) in v1:
                v1.remove((new_sin_word, hashed_dic[get_hash(new_sin_word)]))
                #print(v2)
            v2.insert(0, (new_sin_word, hashed_dic[get_hash(new_sin_word)]))
            #print(v2)

    if len(permutated_sin_word) == 1:
        if len(v2) > 1 and v2[0][1] <= max:
            v2.insert(0, max_word)
    elif len(permutated_sin_word) > 1 and max != 0:
        if (max_word, max) not in v2 and (max_word, max) not in v1:
           v2.insert(0, (max_word, max))

    v = v2 + v1

    #print(v)
    if len(v) == 0:
        v = v + minnnnn[:5]

    if len(space_suggestion):
        v = space_suggestion + v
    # if get_hash(user_sin_word) in hashed_dic:
    #     if (user_sin_word, hashed_dic[get_hash(user_sin_word)]) not in v:
    #         v.insert(0, (user_sin_word, hashed_dic[get_hash(user_sin_word)]))
    #         #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs")

    # f = open('test', 'w')
    # for x in v:
    #   f.write(x[0]+"\n")
    # f.close()
    b = datetime.datetime.now()
    #print(b - a)
    #print(v[:5])
    return v[:5]


# #print(suggestion_generator('කකුළ'))
# a1 = datetime.datetime.now()
# filepath2 = "extracted_misspelled_official"
# #print("FFFFFFF")
# b = {}
# with open(filepath2) as fp:
#     for line in fp:
#         x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
#         b[x[0]] = suggestion_generator(x[0])
# #print(b)
#
# f = open('suggested_words_official', 'w')
# for x in b:
#     f.write(x+" : "+str(b[x])+"\n")
# f.close()
#
# b1 = datetime.datetime.now()
# #print(b1 - a1)

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
    d2=sync_time()
    address = ('localhost', 25035)     
	
	
    while(1):
        with Listener(address, authkey=b'123@kbs') as listener:
            with listener.accept() as conn:

                data = conn.recv()
                foutput = suggestion_generator(data)
                conn.send(json.dumps(foutput))
		
	

