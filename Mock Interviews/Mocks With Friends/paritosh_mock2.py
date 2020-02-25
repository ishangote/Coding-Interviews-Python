"""
Design a spell checker.

What is the API/contract/function signature?
Is it offline/online? Is it offline desktop application or is it a web-service?
Should we also add auto-correct?

How many words are there in the dictionary?
Are all words made up of 26 characters? Like no punctuations or symbols?
Are they case in-sensitive?
Discuss pros and cons of using hashmap vs trie.

Define API/contract for the problem:
API:
public boolean SpellCheck(string word)

Dictionary Trie:
            root
        a        b
      N            a
    T   D            T
                       H

----------------------------------------------
constraints:
1. all chars must be alpha

name: spell_checker
input: string
output: True/False

spell_checker:
  func is_correct_spell(input_word) -> True/False


				-
			a		g
        p 		       o
      p   e          d 	  o	
    l     	                 d
   e

Why use Trie instead of hash_set/dictionary:

Worst case time complexity for array: O(number of words in the dictionary)
Worst case time complexity is fixed for trie -> O(depth of trie)
Worst case time complexity for hash set/map -> O(length of input word) because internally for hash function

TESTING:
1. ""	-> False
2. god	->	True
     ^
     
3. gta -> False
	  ^
	ROOT
		g  <
    	o
		o    d
	d
  
  curr = gnode			{o:onode}


"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_end = False

class Trie:
    def __init__(self): self.root = TrieNode('ROOT')
  
    def insert_word(self, word):	
        if not word: return 
        curr = self.root
    
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
    
        curr.word_end = True
  	
    def check_word(self, word):
        curr = self.root
        for ch in word:
            if not ch in curr.children: return False
            curr = curr.children[ch]
    
        return curr.word_end
  	
class SpellCheck:
    def __init__(self, trie):
        self.trie = trie
    
    def is_correct_word(self, word):
        return self.trie.check_word(word)

import unittest
class TestSpellCheck(unittest.TestCase):
    dictionary = Trie()
    
    dictionary.insert_word("apple")
    dictionary.insert_word("orange")
    dictionary.insert_word("pear")
    dictionary.insert_word("watermelon")
    dictionary.insert_word("avocado")
    dictionary.insert_word("ape")
    dictionary.insert_word("ball")
    dictionary.insert_word("bag")

    spell_check_obj = SpellCheck(dictionary)

    def test_generic(self):
        self.assertEqual(self.spell_check_obj.is_correct_word("apple"), True)
        self.assertEqual(self.spell_check_obj.is_correct_word("pear"), True)
        self.assertEqual(self.spell_check_obj.is_correct_word("ape"), True)

        self.assertEqual(self.spell_check_obj.is_correct_word("apples"), False)
        self.assertEqual(self.spell_check_obj.is_correct_word("bear"), False)
        self.assertEqual(self.spell_check_obj.is_correct_word("baller"), False)

    def test_edge(self):
        self.assertEqual(self.spell_check_obj.is_correct_word(""), False)

if __name__  == "__main__": unittest.main()

"""
Feedback:
  
research assitant, teaching assitant -->poor intro, no mention of what you want or are looking for	

Document or word?
Not taking examples quickly instead of asking questions in air --> Red flag

assuming without asking ---> BIG red flag

quick followup, hasty requirement gathering 

so ok ok, instead of "Ah, ..."

What would the API/contract look like?
A> First we need some datastructure... going into implementation before defining input/outputs ---> Red Flag

What is API?
It is a service --> not really

It'll output, "sorry" --> 

Went with some preprocessing logic without consulting the interviewer -> wasted time

correctly-spelled words -> call it dictionary

No brute force solution explained -> direclty went into data structures

Lot of silence instead of speaking out

Very poor understanding of basic data strucutres like sets and tries

Don't use the word contract too much: say "function signature" for functions

Can you tell me about software deve process?

respononsible
"""