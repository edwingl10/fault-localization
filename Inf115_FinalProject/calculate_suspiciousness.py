import re
from collections import defaultdict
import os


passing_files_path = "/Users/Bone17/Desktop/Inf115_FinalProject/PassingXML_Closure_96"
failing_files_path = "/Users/Bone17/Desktop/Inf115_FinalProject/FailingXML_Closure_96"
total_passing_tests = 4067
total_failing_tests = 3

#used to store info in following format
# filenum: {passedCoverage: num, failedCoverage: num}
score_dict = defaultdict(lambda: defaultdict(int))



def scoreOnPassed(path:str):
    ''' calculates how many passing tests cover each line using hit numbers
        from coverage report files in PassingXML_Closure_96 folder.
        if hits >1 then I just count it as 1. 
        stores it in score_dict[line number] under "passedCoverage".
    '''
    
    #loops through the directory of passed test reports
    for subdir, dirs, files in os.walk(path):
        #loops through the files within directory
        for file in files:           
            
            try:
                file = open(path+"/"+file,"r")
            
            
                for lines in file.readlines():
                    
                    line = lines.split('"')

                    #stores the hit number of each line
                    hit_num = int(line[3])
                    #had to do to not include duplicates within coverage file
                    tab_count = line[0].count("\t")
                    
                    if hit_num >=1 and tab_count == 8:
                        #add 1 to number of tests that passed and covered line
                        score_dict[line[1]]["passedCoverage"] += 1
                
            except:
                pass
                



def scoreOnFailed(path:str):
    ''' calculates how many failing tests cover each line using hit numbers
        from coverage reports files in FailingXML_Closure_96 folder.
        if hits >1 then i just count it as 1.
        stores it in score_dict[line number] under "failedCoverage".
    '''
    
    #loops through directory of failed test reports
    for subdir, dirs, files in os.walk(path):
        #loops through the files within directory
        for file in files:
            try:
                file = open(path+"/"+file, "r")
                for lines in file.readlines():
                    
                    line = lines.split('"')

                    #stores the hit number of each line
                    hit_num = int(line[3])
                    #had to do to not include duplicates within coverage file
                    tab_count = line[0].count("\t")
                    
                    if hit_num >=1 and tab_count == 8:
                        #add 1 to number of tests that failed and covered line
                        score_dict[line[1]]["failedCoverage"] += 1

            except:
                pass



def writeCsvFile(filename:str):
    '''calculates the suspicioussness score of each line.
        when done, writes it to csv file.
    '''
    
    file = open(filename,"w+")
    #writes the headers for the CSV file
    file.write("Project,Bug ID,Line Number, Suspiciousness Score\n")

    #goes through every file number 
    for i in range(1720):
        #calculates failed(e)/ total failed
        failed_score = score_dict[str(i+1)]["failedCoverage"]/total_failing_tests
        #calculates passed(e)/ total passed
        passed_score = score_dict[str(i+1)]["passedCoverage"]/total_passing_tests
        
        try:
            #calculates suspiciousness score using the formula
            suspiciousness = failed_score/(passed_score+failed_score)
        except ZeroDivisionError:
            suspiciousness = 0

        #formats it for csv file 
        to_write = "Closure,96,{},{:.4f}\n".format(i+1, float(suspiciousness))
        
        file.write(to_write)


        

if __name__ == "__main__":
    
    
    scoreOnPassed(passing_files_path)
    scoreOnFailed(failing_files_path)
    writeCsvFile("SuspiciousnessScore.csv")
    



