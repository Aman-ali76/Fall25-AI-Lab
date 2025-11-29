import pickle
import os
from flask import Flask, render_template, request
import pickle
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model_svc.pkl')

app = Flask(__name__)


model_svc = pickle.load(open(model_path, 'rb'))


street_options = [1502, 3858, 2265, 4219]
city_options = [36, 35, 18, 3]
statezip_options = [62, 58, 26, 7]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
    
        try:
            input_data = {
                'bedrooms': [int(request.form['bedrooms'])],
                'bathrooms': [int(request.form['bathrooms'])],
                'sqft_living': [int(request.form['sqft_living'])],
                'sqft_lot': [int(request.form['sqft_lot'])],
                'floors': [float(request.form['floors'])],
                'waterfront': [int(request.form['waterfront'])],
                'view': [int(request.form['view'])],
                'condition': [int(request.form['condition'])],
                'sqft_above': [int(request.form['sqft_above'])],
                'sqft_basement': [int(request.form['sqft_basement'])],
                'yr_built': [int(request.form['yr_built'])],
                'yr_renovated': [int(request.form['yr_renovated'])],
                'street': [int(request.form['street'])],
                'city': [int(request.form['city'])],
                'statezip': [int(request.form['statezip'])]
            }

        
            df = pd.DataFrame(input_data)

        
            prediction = model_svc.predict(df)[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html',
                           prediction=prediction,
                           street_options=street_options,
                           city_options=city_options,
                           statezip_options=statezip_options)

if __name__ == "__main__":
    app.run(debug=True)
