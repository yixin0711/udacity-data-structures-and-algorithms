#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:18:26 2020

@author: Sharonvy
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        node = self.root
        
        for word in path:
            node.insert(word)
            node = node.children[word]
            
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        
        for word in path:
            if word not in node.children:
                return None
            node = node.children[word]
        
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, word):
        # Insert the node as before
        if word not in self.children:
            self.children[word] = RouteTrieNode()

        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, non_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if not isinstance(path, str):
            print("Invalid path type")
            return
        
        path_list = self.split_path(path)
        self.router.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not isinstance(path, str):
            print("Invalid path type")
            return 
        
        path_list = self.split_path(path)
        
        if len(path_list) == 0:
            return self.router.handler
        
        res = self.router.find(path_list)
        if res is None:
            return self.non_found_handler
        else:
            return res

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split(sep = '/')
        res_list = [i for i in path_list if i != '']
        return res_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

#test edge cases
router.add_handler(["/home/about"], "about handler")    #should print "Invalid path type"
router.lookup(["/"])             # should print "Invalid path type"
print(router.lookup("/"))       # should print 'root handler'

# some lookups with the expected output
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one