import itertools
import collections
import ast
import astor

import time

from CodeAnalysis import *
from Data_Match import *



class file:
    def __init__(self,filename):
        file = open(filename,"r").read()
        data = CodeAnalysis(file)
        data.show_fragments()
        data.show_instances()
        fragment_data = data.fragment_io()
        matches = Data_Match(fragment_data).matches
        print(matches)
        for match in matches:
            for node in match[0].nodes:
                print(node.body)
            print("=======")
            print(match[1])
            print("\n\n\n")

#
#class console:
#    def __init__(self)



file('test/pa_'+str(input())+'.py')
