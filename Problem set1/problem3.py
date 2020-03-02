# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 02:19:04 2020

@author: Mostafa Atalla
"""

"""
Pseudocode for the problem:
    1 - start using the first letter of the word
    2 - Check if the following letter has higher index:
        if yes, accumulate this letter to the first and continue
        if not, start the loop again with the following letter
        store the accumulated words in a list
    
    3- check the word with the most number of letters 
        return it
          

"""
s = 'abcdefghijklmnopqrstuvwxyz'

alphabet='abcdefghijklmnopqrstuvwxyz'


def alphabet_index(alphabet_letter):
    index=alphabet.index(alphabet_letter)
    return index


sub_string_list=[]
sub_string=s[0]
idx=0
for idx in range(len(s)-1):
    first_char_idx = alphabet_index(s[idx])
    second_char_idx = alphabet_index(s[idx+1])
    if second_char_idx >= first_char_idx:
        sub_string+=s[idx+1]
    else:
        sub_string_list.append(sub_string)
        sub_string=s[idx+1]
sub_string_list.append(sub_string)


longest_string=sub_string_list[0]
for string in sub_string_list:
    if len(string) > len(longest_string):
        longest_string = string

print("Longest substring in alphabetical order is: "+str(longest_string))
    