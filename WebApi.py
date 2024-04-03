from flask import Flask, request, jsonify
import csv

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            blood_group = request.form['blood_group']
            if (blood_group == "ABP"):
                rh = ("AB +ve")
            elif (blood_group == "AP"):
                rh = ("A +ve")
            elif (blood_group == "BP"):
                rh = ("B +ve")
            elif (blood_group == "ABN"):
                rh = ("AB -ve")
            elif (blood_group == "AN"):
                rh = ("A -ve")
            elif (blood_group == "BN"):
                rh = ("B -ve")
            else:
                rh = "-"

            age = request.form['age']
            medical_condition = request.form['medical_condition']
            if (medical_condition == "diabetes"):
                condition = ("Diabetes")
            elif (medical_condition == "arthritis"):
                condition = ("Arthritis")
            elif (medical_condition == "asthama"):
                condition = ("Asthama")
            elif (medical_condition == "obesity"):
                condition = ("Obesity")
            elif (medical_condition == "cancer"):
                condition = ("Cancer")
            elif (medical_condition == "hypertension"):
                condition = ("Hypertension")
            else:
                condition = "-"
            # Add data to CSV file
            with open('patient_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, rh, age, condition])

            return jsonify({'message': 'Data received and saved'})
        except Exception as e:
            return jsonify({'error': e})


if __name__ == '__main__':
    app.run(debug=True)
