import flask
import pickle
import pandas as pd

import SearchDrugs as SD
SeaDrugs = SD.SD()
#import pickle

with open(f"SD.pkl", "wb") as file:
	pickle.dump(SeaDrugs,file) 


 #Use pickle to load in the pre-trained model.
with open(f'SD.pkl', 'rb') as f:
    loaded_object = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
       # Extract the input
        Symptoms = flask.request.form['Symptoms']

    # Make DataFrame for the model
    #input_variables = pd.DataFrame([['Symptoms']],
    #columns=['Symptoms'],dtype=object,
    #index=['input'])
    
    # Get the model's prediction
        prediction = loaded_object.search(Symptoms)

    # Render the form again, but add in the prediction and remind the user
    # of the values they input before
        return flask.render_template('main.html',
                                original_input={'Symptoms': Symptoms},
                                                result=prediction)   
    #else:
        #return render_template('main.html')

if __name__ == '__main__':
    app.run()