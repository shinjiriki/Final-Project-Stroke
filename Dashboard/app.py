from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        input = request.form

        df = pd.DataFrame(
            {
                'gender' : [input['gender']],
                'age' : [input['age']],
                'hypertension' : [input['blood pressure']],
                'heart_disease' : [input['heart disease']],
                'ever_married' : [input['married']],
                'work_type' : [input['type of work']],
                'Residence_type' : [input['residence type']],
                'avg_glucose_level' : [input['average glucose level']],
                'bmi' : [input['bmi']],
                'smoking_status' : [input['smoking status']],
            }
        )

        prediksi = model.predict_proba(df)[0][1]

        if prediksi > 0.5:
            stroke = 'Sorry to say but you are prone to Stroke'
        else:
            stroke = 'Congrats, you are healthy'

        return render_template('index.html', data = input, pred = stroke, prob = prediksi)
    return render_template('index.html')


@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df = pd.DataFrame(
            {
                'gender' : [input['gender']],
                'age' : [input['age']],
                'hypertension' : [input['blood pressure']],
                'heart_disease' : [input['heart disease']],
                'ever_married' : [input['married']],
                'work_type' : [input['type of work']],
                'Residence_type' : [input['residence type']],
                'avg_glucose_level' : [input['average glucose level']],
                'bmi' : [input['bmi']],
                'smoking_status' : [input['smoking status']],
            }
        )

        prediksi = model.predict_proba(df)[0][1]

        if prediksi > 0.5:
            stroke = 'Sorry to say but you are prone to Stroke'
        else:
            stroke = 'Congrats, you are healthy'

        return render_template('result.html', data = input, pred = stroke, prob = prediksi)

if __name__ == '__main__':
    
    filename = 'Model Final.sav'
    model = pickle.load(open(filename,'rb'))
    app.run(debug=True)