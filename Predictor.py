import pickle
import pandas as pd

def predict (data, model_path): 
    

    model = pickle.load(open(model_path, 'rb')) #Please enter path to the model in this
    CSV = pd.read_json("path to CSV FILE") #Please enter path to the CSV here
    with open(SelectedFeatures.txt) as file: #Please make sure that the text filenamed SelectedFeatures is in the same path as this script or change manually
    while (sf := file.readline().rstrip()): #This opens the file and saves it as a list

    CSV = CSV[sf] #Slicing the csv to keep only the features that our model can work on
    prediction = model.predict(CSV)  
    return prediction
