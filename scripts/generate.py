

###################
#
#			README
#
#		An extension to this would be a bash wrapper to the convert to pdf and merge into one file
#
#		Blueskies:
#
#			1) Create a GUI for creating new models and tests
#
#			2) An executable short cut on desktop
###################

import secretary
import json
import random
import sys
import inflect


p = inflect.engine()


copies = int(sys.argv[1])
numQuestions = int(sys.argv[2])

def makeCopy(num):
    dictionary = {}
    f = open("./questions/test.json", "r")
    questions = json.load(f)
    f.close()
    
    r = random.sample(list(questions.values()), numQuestions)
    counter = 1
    while len(dictionary) < numQuestions:
        dictionary[str(p.number_to_words((counter)))] = r[int(counter-1)]
        counter += 1
        #print(str(p.number_to_words((counter))))
    #print(dictionary)
    engine = secretary.Renderer()
    result = engine.render("/home/rr/Development/AntiCheat_format/models/new.odt", **dictionary)
    output = open("/home/rr/Development/AntiCheat_format/tests/{}.odt".format(num), 'wb')
    output.write(result)



for a in range(0, copies):
    makeCopy(a)
