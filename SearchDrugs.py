import os
import sys
import re
import numpy as np
import pandas as pd
import io
import requests
import csv

class SD:
    def search(self, str):
        csv = open("/Users/shilpa/Desktop/Appa/homeopathwebapp/csvF_Head.csv", 'r')
        csvF = csv.readlines()
        #csvF = pd.read_csv(csv)

        #print("1.Hello")
        #url = "https://raw.githubusercontent.com/ShilpaMuralidhar/homeopathwebapp/master/csvF_Head.csv"
        #print("1-1.Hello")
        #s = requests.get(url).content
        #csvF = pd.read_csv(io.StringIO(s.decode('utf-8')))
        #csvA = pd.read_csv(url)
        #csvF = csvA
        #print("2.Hello")
        #print(csvF.iloc[0,:])
        #csvF.to_csv('csvF_Head_1.csv', encoding='utf-8')
        num_lines = len(csvF)
        #csv.close

        #str = "Nose,Water"
        # print("Enter the search string")
        #str = input("Enter the symptom string here = ")
        str = re.sub("\s", ",", str)
        str = re.sub(",+", ",", str)
        

        # print("Looking for = ", str)
        rank = np.zeros([num_lines])
        #print(rank)

        str = str.lower()
        #print(str)
        symptoms = re.split(",", str)
        #print(symptoms)
        rank_symp = {}
        #print(rank_symp)
        match_symp = {}
        #print(match_symp)
        top3 = {}
        top2 = {}
        top = {}
    

        for symp in symptoms:
            rank_symp[symp] = 0
            #print('symp:',symp, 'rank_symp:',rank_symp)

        for line in range (1, num_lines):
        #for line in csvF:
            match_symp[line] = ""
            #print(csvF.iloc[0,0])
            #print(match_symp)
            for symp in symptoms:
                r1 = re.findall(symp, csvF[line].lower()) 
                #print('r1:',r1)
                if (r1 != []):
                     rank[line] = rank[line] + 1
                     rank_symp[symp] = rank_symp[symp] + 1
                     print(rank[line],rank_symp[symp])
                     if (match_symp[line] == ""):
                        match_symp[line] = symp
                     else:
                        match_symp[line] = symp + "," + match_symp[line]
                     top3[symp] = line
        idx = int(np.argmax(rank))
        arr = rank.argsort()[-3:][::-1]
        print("Symptoms found = ", rank_symp)
        print ("Found ", len(arr), "possible suggestions")
        # print(arr)
        # print(rank)
        if (rank[arr[2]] == rank[arr[1]] == rank[arr[0]]):
            print("Entered symptom is found in three possible cases")
            print("Try entering more specific symptoms")
        elif (rank[arr[2]] == rank[arr [1]]) or (rank[arr[1]] == rank[arr[0]]):
            print("Entererd symptom is found in two possible cases")
            print("Try entering more specific symptoms")
        else:
            print("Entered symptom is a unique possible case")
        # print(idx, arr)
        print(rank[arr[0]], rank[arr[1]], rank[arr[2]])

        if (idx < 2):
            print("No matching medicine found")
        else:
            ind = 1
            for i in arr:
                if (rank[i] > 0) and (ind > 0):
                    print(ind, ". Suggestion Medicine = ", re.split(",", csvF[arr[ind-1]])[1], sep='')
                    print("   Matching symptoms are", match_symp[arr[ind-1]])
                    otherSymps = re.split(",", csvF[arr[ind-1]])
                    max = 0
                    for x in range (1, len(otherSymps)):
                        if (otherSymps[x] != ""):
                            if (max <= 3):
                                print("   Other possibly associated symptoms are", otherSymps[x])
                                max = max + 1
                            else:
                                break
                    ind = ind + 1
        #ret
        retVal = re.split(",", csvF[arr[0]])[1] + "\n" + re.split(",", csvF[arr[1]])[1]+ "\n" + re.split(",", csvF[arr[2]])[1]
        return(retVal)



