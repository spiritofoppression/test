# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 00:30:04 2021

@author: spirit of oppression
"""

from collections import Counter

#ввод слова
#word = input().lower()
#print(word)
checked_word = "Ростелеком"

list_of_checked_word_letters = []

#перевод букв слова в нижний регистр
for i in range(len(checked_word)):
    list_of_checked_word_letters.append(checked_word.lower()[i])

counter_of_checked_word_letters = Counter(list_of_checked_word_letters)

word_list = []

#считывание данных из файла
with open('word_rus.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word_list.append(line.strip())
    
number_of_words = 0
    
#проверяет, можно ли составить из слова из списка наше слово
for i in range(len(word_list)):
    if (counter_of_checked_word_letters | Counter(word_list[i].lower())) == counter_of_checked_word_letters:
        number_of_words += 1
        
print(number_of_words)