import os
import sys
import re
import numpy as np

class SD:
    def search(self, str):
        csv = open("/Users/shilpa/Desktop/Appa/homeopath-webapp/untitled folder/HEAD_SHEET.csv", "r")
        csvF = csv.readlines()
        num_lines = len(csvF)
        csv.close

        #str = "Nose,Water"
        # print("Enter the search string")
        #str = input("Enter the symptom string here = ")
        str = re.sub("\s", ",", str)
        str = re.sub(",+", ",", str)

        # print("Looking for = ", str)
        rank = np.zeros([num_lines])

        str = str.lower()
        symptoms = re.split(",", str)
        rank_symp = {}
        match_symp = {}
        top3 = {}
        top2 = {}
        top = {}

        for symp in symptoms:
            rank_symp[symp] = 0

        for line in range (1, num_lines):
            match_symp[line] = ""
            for symp in symptoms:
                r1 = re.findall(symp, csvF[line].lower())
                if (r1 != []):
                    rank[line] = rank[line] + 1
                    rank_symp[symp] = rank_symp[symp] + 1
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
        retVal = re.split(",", csvF[arr[0]])[0] + "\n" + re.split(",", csvF[arr[1]])[0]+ "\n" + re.split(",", csvF[arr[2]])[0]
        return(retVal)



