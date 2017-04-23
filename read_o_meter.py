#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:53:31 2017

@author: afrin
"""


class ReadPost:
    
    def __init__(self, post):
        self.post = post
        
    def count_words(self):
        words = self.post.split(" ")
        return len(words)
    
    def wpm(self):
        time = (self.count_words()*60)/200
        return int(time)
    
    
