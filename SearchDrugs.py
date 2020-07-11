import os
import sys
import re
import numpy as np
import pandas as pd
import io
#import requests
import csv

class SD:
    def search(self, str):
        url = "https://raw.githubusercontent.com/ShilpaMuralidhar/homeopathwebapp/master/csvF_Head.csv"
        #csv_url = requests.get(url)
        csvF_df = pd.read_csv(url, encoding='utf-8')

        #csvF_df = pd.read_csv(io.StringIO(csv_url.text), encoding='utf-8')
        csvF_df= csvF_df.reset_index(drop=True)
        #csvF_df = csvF_df.drop(columns=["Unnamed: 0"])

        #csvF_df = csvF_df.drop(columns=["Unnamed: 0", "Unnamed: 5", "Unnamed: 7", "Unnamed: 19", "Unnamed: 21", "Unnamed: 31", "Unnamed: 36", "Unnamed: 37"])
        #csvF_df= csvF_df.set_index('Unnamed:0')

        

        print(type(csvF_df))


        csvF = csvF_df.to_csv(index=False).strip('\n').split('\n')
        #csvF = csvF_df.to_csv(index=False).strip('\n')

        #csvF = csvF_df.to_csv()

        print(csvF)

        num_lines = len(csvF)
        num_lines

        #str = input("Enter the symptom string here = ")
        str = re.sub("\s", ",", str)
        print("str:", str)
        str = re.sub(",+", ",", str)
        print("str:", str)
        rank = np.zeros([num_lines])
        str = str.lower()
    
        #print(str)
        symptoms = re.split(",", str)
        print("Symptoms:",symptoms)
        rank_symp = {}
        print(rank_symp)
        match_symp = {}
        print(match_symp)
        top3 = {}
        top2 = {}
        top = {}


        for symp in symptoms:
            rank_symp[symp] = 0
            print("RS", rank_symp)

            for line in range (1, num_lines):
                match_symp[line] = ""
                for symp in symptoms:
                    r1 = re.findall(symp, csvF[line].lower())
                    #print('r1:', r1, csvF[line])
                    if (r1 != []):
                        rank[line] = rank[line] + 1
                        print("RL:", rank[line])
                        #rank_symp[symp] = rank_symp[symp] + 1 (Commenting this line makes the entire code work!!!)

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
                    print(ind, ". Suggestion Medicine = ", re.split(",", csvF[arr[ind-1]])[0], sep='')
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

        #retVal = re.split(",", csvF[arr[0]])[1] + "\n" + re.split(",", csvF[arr[1]])[1]+ "\n" + re.split(",", csvF[arr[2]])[1]
        retVal = re.split(",", csvF[arr[0]])[0] + "\n" + re.split(",", csvF[arr[1]])[0]+ "\n" + re.split(",", csvF[arr[2]])[0]

        print(retVal)
        return(retVal)
