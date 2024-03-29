# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import Counter
import numpy as np
import pandas as pd

absolute_path = os.path.dirname(__file__)
relative_path = "shakespeare.txt"
full_path = os.path.join(absolute_path, relative_path)
print(full_path)


def process_data(file_name):
    """
    Input:
        A file_name which is found in your current directory. You just have to read it in.
    Output:
        words: a list containing all the words in the corpus (text file you read) in lower case.
    """
    with open(file_name) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+', file_name_data)

    return words

word_l = process_data(full_path)
vocab = set(word_l)  # this will be your new vocabulary
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")


# A function that calculates the number of times " \
# a word appear in the corpus.
def get_count(word_l):
    '''
    Input:
        word_l: a set of words representing the corpus.
    Output:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    '''
    word_count_dict = {}
    for w in word_l:
        if w not in word_count_dict:
            word_count_dict[w] = 1
        else:
            word_count_dict[w] += 1
    return word_count_dict

word_count_dict = get_count(word_l)
print(f"There are {len(word_count_dict)} key values pairs")
print(f"The count for the word 'thee' is {word_count_dict.get('thee', 0)}")


def get_probs(word_count_dict):
    '''
    Input:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    Output:
        probs: A dictionary where keys are the words and the values are the probability that a word will occur.
    '''
    probs = {}
    for k, v in word_count_dict.items():
        prob = {}
        prob[k] = v / sum(word_count_dict.values())
        probs.update(prob)

    return probs

probs = get_probs(word_count_dict)
print(f"Length of probs is {len(probs)}")
print(f"P('thee') is {probs['thee']:.4f}")


def get_probs(word_count_dict):
    '''
    Input:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    Output:
        probs: A dictionary where keys are the words and the values are the probability that a word will occur.
    '''
    probs = {}  # return this variable correctly
    for k, v in word_count_dict.items():
        prob = {}
        prob[k] = v / sum(word_count_dict.values())
        probs.update(prob)

    return probs

probs = get_probs(word_count_dict)
print(f"Length of probs is {len(probs)}")
print(f"P('thee') is {probs['thee']:.4f}")


def delete_letter(word, verbose=False):
    '''
    Input:
        word: the string/word for which you will generate all possible words
                in the vocabulary which have 1 missing character
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    delete_l = [L + R[1:] for L, R in split_l if R]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l

delete_word_l = delete_letter(word="cans",
                              verbose=True)
print(f"Number of outputs of delete_letter('at') is {len(delete_letter('at'))}")


def switch_letter(word, verbose=False):
    '''
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    '''
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    switch_l = [L[:-1] + R[0] + L[-1] + R[1:] for L, R in split_l if L if R]

    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")

    return switch_l

switch_word_l = switch_letter(word="eta",
                              verbose=True)
print(switch_word_l)


def replace_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word
    Output:
        replaces: a list of all possible strings where we replaced one letter from the original word.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    split_l = [w for w in split_l if w != word]
    replace_l = set([L + R.replace((L + R)[i], l) for L, R in split_l for l in letters
                     for i in range(len(L + R))])
    replace_l.discard(word)

    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")

    return sorted(list(replace_l))


replace_l = replace_letter(word='can',
                           verbose=True)
print(replace_l)
print(len(replace_l))


def insert_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word
    Output:
        inserts: a set of all possible strings with one new letter inserted at every offset
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'

    split_l = [(word[:i] + l, word[i:]) for i in range(len(word) + 1) for l in letters]
    insert_l = [L + R for L, R in split_l]

    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")

    return insert_l


insert_l = insert_letter('at', True)
print(f"Number of strings output by insert_letter('at') is {len(insert_l)}")

expected_output = ['aat', 'bat', 'cat', 'dat', 'eat', 'fat', 'gat', 'hat', 'iat', 'jat', 'kat', 'lat', 'mat', 'nat',
                   'oat', 'pat', 'qat', 'rat', 'sat', 'tat', 'uat', 'vat', 'wat', 'xat', 'yat', 'zat', 'aat', 'abt',
                   'act', 'adt', 'aet', 'aft', 'agt', 'aht', 'ait', 'ajt', 'akt', 'alt', 'amt', 'ant', 'aot', 'apt',
                   'aqt', 'art', 'ast', 'att', 'aut', 'avt', 'awt', 'axt', 'ayt', 'azt', 'ata', 'atb', 'atc', 'atd',
                   'ate', 'atf', 'atg', 'ath', 'ati', 'atj', 'atk', 'atl', 'atm', 'atn', 'ato', 'atp', 'atq', 'atr',
                   'ats', 'att', 'atu', 'atv', 'atw', 'atx', 'aty', 'atz']

print(insert_l == expected_output)


# UNQ_C8 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: edit_one_letter
def edit_one_letter(word, allow_switches=True):
    """
    Input:
        word: the string/word for which we will generate all possible words
        that are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit.
        Please return a set. and not a list.
    """

    edit_one_set = set()

    ### START CODE HERE ###
    all_edits = delete_letter(word) + replace_letter(word) + insert_letter(word)
    if allow_switches:
        all_edits = all_edits + switch_letter(word)
    for edit in all_edits:
        edit_one_set.add(edit)
    ### END CODE HERE ###

    return edit_one_set


tmp_word = "at"
tmp_edit_one_set = edit_one_letter(tmp_word)
# turn this into a list to sort it, in order to view it
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
print(f"Number of outputs from edit_one_letter('at') is {len(edit_one_letter('at'))}")


# UNQ_C9 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: edit_two_letters
def edit_two_letters(word, allow_switches=True):
    '''
    Input:
        word: the input string/word
    Output:
        edit_two_set: a set of strings with all possible two edits
    '''

    edit_two_set = set()

    ### START CODE HERE ###
    one_edits = edit_one_letter(word, allow_switches)
    for edit in one_edits:
        edit_of_edit = edit_one_letter(edit, allow_switches)
        if edit_of_edit is not None:
            edit_two_set = edit_two_set.union(edit_of_edit)

    ### END CODE HERE ###

    return edit_two_set


tmp_edit_two_set = edit_two_letters("a")
tmp_edit_two_l = sorted(list(tmp_edit_two_set))
print(f"Number of strings with edit distance of two: {len(tmp_edit_two_l)}")
print(f"First 10 strings {tmp_edit_two_l[:10]}")
print(f"Last 10 strings {tmp_edit_two_l[-10:]}")
print(f"The data type of the returned object should be a set {type(tmp_edit_two_set)}")
print(f"Number of strings that are 2 edit distances from 'at' is {len(edit_two_letters('at'))}")

# example of logical operation on lists or sets
print([] and ["a", "b"])
print([] or ["a", "b"])
# example of Short circuit behavior
val1 = ["Most", "Likely"] or ["Less", "so"] or ["least", "of", "all"]  # selects first, does not evalute remainder
print(val1)
val2 = [] or [] or ["least", "of", "all"]  # continues evaluation until there is a non-empty list
print(val2)


def get_corrections(word, probs, vocab, n=2, verbose=False):
    '''
    Input:
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output:
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    suggestions1 = edit_one_letter(word)
    suggestions2 = edit_two_letters(word)

    suggestions = suggestions1.intersection(suggestions2)
    prob_suggestions2 = []
    for el in suggestions:
        if el in probs:
            prob_suggestions2.append((el, probs[el]))

    n_best = sorted(prob_suggestions2[:n], key=lambda x: x[1], reverse=True)

    suggestions = set(el[0] for el in prob_suggestions2)

    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best

# Test implementation
my_word = 'dys'
tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=True)  # keep verbose=True
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")

# CODE REVIEW COMMENT: using "tmp_corrections" insteads of "cors". "cors" is not defined
print(f"data type of corrections {type(tmp_corrections)}")


def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    '''
    Input:
        source: a string corresponding to the string you are starting with
        target: a string corresponding to the string you want to end with
        ins_cost: an integer setting the insert cost
        del_cost: an integer setting the delete cost
        rep_cost: an integer setting the replace cost
    Output:
        D: a matrix of len(source)+1 by len(target)+1 containing minimum edit distances
        med: the minimum edit distance (med) required to convert the source string to the target
    '''
    # use deletion and insert cost as  1
    m = len(source)
    n = len(target)
    # initialize cost matrix with zeros and dimensions (m+1,n+1)
    D = np.zeros((m + 1, n + 1), dtype=int)

    # Fill in column 0, from row 1 to row m, both inclusive
    for row in range(1, m + 1):  # Replace None with the proper range
        D[row, 0] = D[row - 1, 0] + ins_cost

    # Fill in row 0, for all columns from 1 to n, both inclusive
    for col in range(1, n + 1):
        D[0, col] = D[0, col - 1] + ins_cost

    # Loop through row 1 to row m, both inclusive
    for row in range(1, m + 1):

        # Loop through column 1 to column n, both inclusive
        for col in range(1, n + 1):

            # Initialize r_cost to the 'replace' cost that is passed into this function
            r_cost = rep_cost

            # Check to see if source character at the previous row
            # matches the target character at the previous column,
            if source[row - 1] == target[col - 1]:
                # Update the replacement cost to 0 if source and target are the same
                r_cost = 0

            # Update the cost at row, col based on previous entries in the cost matrix
            # Refer to the equation calculate for D[i,j] (the minimum of three calculated costs)
            D[row, col] = min(D[row - 1, col] + del_cost,
                              D[row, col - 1] + ins_cost,
                              D[row - 1, col - 1] + r_cost)

    # Set the minimum edit distance with the cost found at row m, column n
    med = D[len(source), len(target)]

    return D, med

# testing implementation
source = 'play'
target = 'stay'
matrix, min_edits = min_edit_distance(source, target)
print("minimum edits: ", min_edits, "\n")
idx = list('#' + source)
cols = list('#' + target)
df = pd.DataFrame(matrix, index=idx, columns=cols)
print(df)

#DO NOT MODIFY THIS CELL
# testing your implementation
source =  'play'
target = 'stay'
matrix, min_edits = min_edit_distance(source, target)
print("minimum edits: ",min_edits, "\n")
idx = list('#' + source)
cols = list('#' + target)
df = pd.DataFrame(matrix, index=idx, columns= cols)
print(df)


#DO NOT MODIFY THIS CELL
# testing your implementation
source =  'eer'
target = 'near'
matrix, min_edits = min_edit_distance(source, target)
print("minimum edits: ",min_edits, "\n")
idx = list(source)
idx.insert(0, '#')
cols = list(target)
cols.insert(0, '#')
df = pd.DataFrame(matrix, index=idx, columns= cols)
print(df)

source = "eer"
targets = edit_one_letter(source,
                          allow_switches=False)  # disable switches since min_edit_distance does not include them
for t in targets:
    _, min_edits = min_edit_distance(source, t, 1, 1, 1)  # set ins, del, sub costs all to one
    if min_edits != 1: print(source, t, min_edits)

source = "eer"
targets = edit_two_letters(source,
                           allow_switches=False)  # disable switches since min_edit_distance does not include them
for t in targets:
    _, min_edits = min_edit_distance(source, t, 1, 1, 1)  # set ins, del, sub costs all to one
    if min_edits != 2 and min_edits != 1: print(source, t, min_edits)
