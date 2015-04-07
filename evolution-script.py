#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

class EvolutionScript(object):
    def __init__(self, f=""):
        self.setup()
        
        if type(f) == file:
            print "You gave me a file!"
        elif type(f) == str:
            print "You gave me a string!"
            self.interpretLines(f.split("\n"))
        elif type(f) == list:
            print "You gave me a list!"
            self.interpretLines(f)
        else:
            print "You gave me a %s!" % type(f)
    
    def setup(self):
        self.variables = {} # Variables are stored in an dictionary.
    
    def interpretLines(self, lines):
        for l in lines:
            # Run line
            out = self.interpretLine(l.strip())
            # Output
            if out is not None: print "=>", out
    
    def interpretLine(self, line):
        words = self.parseLine(line)[0]
        punc = self.parseLine(line)[1]
        testing = True
        if testing == True: # to help with visualisation
            print words
            print punc
            print "Interpreting line: '%s'" % line
        # Commands!
        if (len(words) > 1):
            if (punc[1] == "="):
                #print "Found set-variable command!"
                #print "Setting variable '%s' to '%s'." % (words[1], words[1:])
                print len(words), words
                value = filter(lambda x: x != "", words[1:])[0] + "'"
                self.variables[words[0]] = value
            elif words[0] == "@":
                return None
            elif words[0] == "BIN" and punc[1] == ")":
                if words[1].isdigit():
                    return bin(int(words[1]))
                else:
                    if words[1] in self.variables:
                        return bin(int(self.variables[words[1]]))
                    else:
                        return "ERROR: NO VARIABLE OF THAT NAME IS DEFINED."
            elif words[0] == "HEX" and punc[1] == ")":
                return hex(int(words[1])) 
            elif words[0] == "OCT" and punc[1] == ")":
                return oct(int(words[1]))
            elif words[0] == "DO" and punc[len(words)-2] == ")":
                return eval(line[2:]) # Is the problem here?
            else:
                return "ERROR: COMMAND NOT FOUND"
        elif (len(words) == 1):
            if False: # Put 1 line commands after line 49
                pass
            else:
                if words[0] in self.variables:
                    return self.variables[words[0]][1:]
                else:
                    return "ERROR: METHOD OR VARIABLE NOT DEFINED."
        elif len(words) == 0 or words == ['']:
            return None
    
    def parseLine(self, line):
        line = line.strip().replace("\n", "")
        #print "<", line
        
        words = []
        puncOut = []
        punctuation = ["(", ")", "^", "+", "-", "*", "/", "[", "{", "]", "}", ";", "|", "&", "!", "\"", "'", "$", "=", ".", ":", " "] # added ()
        
        # Parse line.
        if (line is not None and line is not "\n"):
            currentWord = ""
            inString = False
            for i in range(0, len(line)):
                if (line[i] == "\"" or line[i] == "'"): # Detect string
                    inString = not inString
                
                if (line[i] in punctuation and inString is False):
                    puncOut.append(line[i])
                    words.append(currentWord)
                    currentWord = ""
                else:
                    currentWord = currentWord + line[i]
    
            
            words.append(currentWord) # Add the last word to the list.
        return (words, puncOut)

if (__name__ == '__main__'):
    new = EvolutionScript("""
        Y = 'THIS USES A MULTI-LINE STRING!'
        Y 
        X = 2
        @ THIS IS A COMMENT BY MRSHERLOCKHOLMES
        BIN(43)
        HEX(90)
        OCT(72) 
        DO(2*9*5/15)
""")
    