import SearchDrugs as SD
SeaDrugs = SD.SD()
import pickle

with open(f"SD.pkl", "wb") as file:
	pickle.dump(SeaDrugs,file) 
