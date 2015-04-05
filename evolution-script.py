#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

class EvolutionScript(object):
    def __init__(self, f=""):
        self.setup()
        
        if type(f) == "file":
            print "You gave me a file!"
        elif type(f) == "string":
            print "You gave me a string!"
        elif type(f) == list:
            print "You gave me a list!"
            self.interpretLines(f)
        else:
            print "You gave me a %s!" % type(f)
    
    def setup(self):
        self.variables = {}
    
    def interpretLines(self, lines):
        for l in lines:
            self.interpretLine(l)
    
    def interpretLine(self, line):
        print "INTERPRETING LINE %s" % line
        words = self.parseLine(line)
    
    def parseLine(self, line):
        words = []
        punctuation = ["^", "+", "-", "*", "/", "[", "{", "]", "}", ";", "|", "&", "!", "\"", "'", "$", "=", ".", ":", " "]
        
        # Parse line.
        currentWord = ""
        for i in range(0, len(line)):
            if line[i] in punctuation:
                print "Adding word '%s' to word list with separator '%s'" % (
                    currentWord, line[i])
                words.append(line[i])
                words.append(currentWord)
                currentWord = ""
            else:
                currentWord = currentWord + line[i]
        
        words.append(currentWord) # Add the last word to the list.
        print "Finished parsing line! Output:", words
        return words

if (__name__ == '__main__'):
    e = EvolutionScript([
        "X = HELLO WORLD",
        "X"
    ])