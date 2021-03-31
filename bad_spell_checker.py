"""
Write a (bad) spell checker

The Product department needs a quick and dirty spell-checker. And they need it yesterday!

Should return a correctly spelled word if found, otherwise return None.

1. A correctly spelled word is defined as one that appears in the list
2. A matching input word would have
    a. The same combination of characters as the valid word
    b. The same number of total characters as the valid word
    OR
    c. Beginning of partial word. ie, like '%word' search in sql
"""
valid_words = ['cat', 'bat']
def spell_checker(word):
    for word_check in valid_words:
        if len(word) < len(word_check) and word_check[:len(word)] == word:        
            return word_check
        elif len(word) == len(word_check):
            word_list = list(word)
            word_check_list = list(word_check)
            word_list.sort()
            word_check_list.sort()
            if word_list == word_check_list:
                return word_check
    return None


assert spell_checker('cat') == 'cat'
assert spell_checker('act') == 'cat'
assert spell_checker('tac') == 'cat'
assert spell_checker('atc') == 'cat'
assert spell_checker('ca') == 'cat'
assert spell_checker('ba') == 'bat'
assert spell_checker('acct') == None
assert spell_checker('batty') == None
assert spell_checker('bats') == None
assert spell_checker('at') == None
