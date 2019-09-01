import re
from collections import defaultdict

file_path = "/Users/Bone17/Desktop/AllPassingTests.txt"
relevant_tests_path = "/Users/Bone17/Desktop/AllRelevantTests.txt"


def StoreTests(Rawfile:str):
    '''creates and stores a dictionary that is used for finding all the
        test methods within the relevant tests.
        Rawfile is the name of the file that contains all the passing tests.
    '''
    # the dictionary that stores test:list of methods
    testMethods = defaultdict(list)
    
    #opens the raw file
    file = open(Rawfile,"r")

    
    for lines in file.readlines():
        
        #splits the lines by parenthesis
        line = re.split("[(]|[)]",lines)
        testMethods[line[1]].append(line[0])
        
        
    file.close()
    return testMethods


def WriteRelevantTests(Rawfile:str, ParsedFile:str, test_dict:dict):
    ''' Writes all the relevant test methods to a file in the format:
        path::method
        Rwafile is the the file that contains all the relevant tests.
        ParsedFile is the name of the file that we are writing to.
        test_dict is the dictionary that contains all the test methods.
    '''
    
    file = open(Rawfile,"r")
    outFile = open(ParsedFile,"w+")

    for line in file.readlines():
        #indexs and loops through the list of methods 
        for methods in test_dict[line.strip()]:
            #formats the file content
            toWrite = "{}::{}\n".format(line.strip(), methods)
            outFile.write(toWrite)
            

    file.close()
    outFile.close()
        
    


testMethods = StoreTests(file_path)
WriteRelevantTests(relevant_tests_path, "RelevantTestMethods.txt",testMethods)

