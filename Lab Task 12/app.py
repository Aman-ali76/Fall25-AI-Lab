import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request


try:
    
    model = pickle.load(open('model.pkl', 'rb'))
    print("Model loaded successfully: model.pkl")
except FileNotFoundError:
    print("WARNING: model.pkl not found. Prediction will use a dummy value.")
    
    class DummyModel:
        def predict(self, X):
            
            return np.array([2.5])
    model = DummyModel()
except Exception as e:
    print(f"Error loading model: {e}")
    
    class DummyModel:
        def predict(self, X):
            return np.array([2.5])
    model = DummyModel()


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the main prediction form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the form submission and returns the prediction."""
    try:
        
        data = {
            'StudentID': int(request.form['StudentID']),
            'Gender': int(request.form['Gender']),
            'Age': int(request.form['Age']),
            'StudyHoursPerWeek': float(request.form['StudyHoursPerWeek']),
            'AttendanceRate': float(request.form['AttendanceRate']),
            'Major': int(request.form['Major']),
            'PartTimeJob': int(request.form['PartTimeJob']),
            'ExtraCurricularActivities': int(request.form['ExtraCurricularActivities'])
        }

        
        
        feature_vector = np.array([
            data['StudentID'], data['Gender'], data['Age'], data['StudyHoursPerWeek'],
            data['AttendanceRate'], data['Major'], data['PartTimeJob'], data['ExtraCurricularActivities']
        ]).reshape(1, -1)

        
        prediction = model.predict(feature_vector)[0]
        
        
        predicted_gpa = f"{prediction:.2f}"

        return render_template(
            'index.html', 
            prediction_text=f'Predicted GPA: {predicted_gpa}',
            
            input_data=data
        )

    except ValueError:
        return render_template('index.html', prediction_text='Error: Please enter valid numerical inputs for all fields.', input_data=request.form)
    except Exception as e:
        return render_template('index.html', prediction_text=f'An error occurred: {e}', input_data=request.form)

if __name__ == '__main__':
    
    app.run(debug=True)