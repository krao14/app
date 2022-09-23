from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    age = int(request.form['age'])
    currentSmoker= int(request.form['currentSmoker'])
    cigsPerDay = int(request.form['cigsPerDay'])
    BPMeds = int(request.form['BPMeds'])
    prevalentStroke=int(request.form['prevalentStroke'])
    diabetes=int(request.form['diabetes'])
    prediction=model.predict([[1, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, 0, diabetes, 200, 1, 1, 0, 0, 0]])
    if str(prediction[0]) == '0':
        prediction_text = f'SAFE:No heart disease predicted'
    else:
        prediction_text=f'ALERT:Heart disease predicted'
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')
