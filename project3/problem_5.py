#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:55:28 2020

@author: Sharonvy
"""

from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        #initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
        
    def insert(self, char):
        #add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

        
    def suffixes(self, suffix = ''):
        #recursive function that collects the suffix for all complete words below this point
        
        if not isinstance(suffix, str):
            print("Invalid input suffix type")
            return None
        
        if len(self.children) == 0:
            return []
        
        results = []
        
        for char, child in self.children.items():
            if child.is_word:
                results.append(suffix + char)
            results += child.suffixes(suffix + char)
        
        return results


class Trie(object):
    def __init__(self):
        # initialize this trie (add a root node)
        self.root = TrieNode()
        
    def insert(self, word):
        # add a word to the trie
        if not isinstance(word, str):
            print("Invalid input word type")
            return
        
        node = self.root
        
        for char in word:
            node.insert(char)
            node = node.children[char]
        
        node.is_word = True
    
    def find(self, prefix):
        #find the trie node that represents this prefix
        if not isinstance(prefix, str):
            print("Invalid input prefix type")
            return None
        
        node = self.root
        
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        
        return node
    
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    

#test functionality and edge cases
print("Pass" if type(MyTrie.find('a')) is TrieNode else "Fail")     #should print pass
print("Pass" if MyTrie.find('b') is None else "Fail")       #should print pass

MyTrie.insert(['antique']) #should print "Invalid input word type"
MyTrie.find(['a']) #should print Invalid input prefix type
node = MyTrie.find('a')
node.suffixes([]) #should print "Invalid input suffix type"

#test suffix
node = MyTrie.find('a')
suffixes = ["nt", "nthology", "ntagonist", "ntonym"]    
print("Pass" if node.suffixes() == suffixes else "Fail")        #should print pass

node = MyTrie.find('')
print("Pass" if node.suffixes() == wordList else "Fail")        #should print pass

node = MyTrie.find('trig')
suffixes = ['ger', 'onometry']
print("Pass" if node.suffixes() == suffixes else "Fail")        #should print pass
