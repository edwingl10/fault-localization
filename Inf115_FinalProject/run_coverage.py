import subprocess
import multiprocessing

relevant_tests_path = "/Users/Bone17/Desktop/RelevantTestMethods.txt"


def CoverageReport(line):
    '''This runs the required commands in terminal to get the coverage
        report of every test method.
        line is the line from the file in the format path::method
    '''
    #calls the coverage command 
    subprocess.call("defects4j coverage -t "+line, shell=True)
    #Using for getting specific information from coverage report
    #also used to name each file differently
    subprocess.call('cat coverage.xml|grep "line number" > PassingXML_Closure_96/{}'.format(line.split("::")[1]), shell=True)

    subprocess.call("> coverage.xml", shell=True)




if __name__ == "__main__":
    
    file = open(relevant_tests_path,"r")
    

    #loops through everyline of the file that contains each test method
    for line in file.readlines():
        
        CoverageReport(line)
