import SearchDrugs as SD
SeaDrugs = SD.SD()
import pickle

with open("/Users/shilpa/Desktop/Appa/homeopathwebapp/SD.pkl", "wb") as file:
	pickle.dump(SeaDrugs,file) 
