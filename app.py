from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

data_pasien = [
    {'name': 'John', 'age': 30, 'blood_pressure': '120/80', 'disease': 'Hipertensi', 'medication': 'Lisinopril', 'doctor': 'Dr. Smith', 'address': 'Jalan Utama 123'},
    {'name': 'Alice', 'age': 25, 'blood_pressure': '110/70', 'disease': 'Migrain', 'medication': 'Sumatriptan', 'doctor': 'Dr. Garcia', 'address': 'Jalan Elm 456'},
    {'name': 'Bob', 'age': 40, 'blood_pressure': '130/90', 'disease': 'Diabetes', 'medication': 'Insulin', 'doctor': 'Dr. Johnson', 'address': 'Jalan Oak 789'},
    {'name': 'Mary', 'age': 35, 'blood_pressure': '115/75', 'disease': 'Alergi', 'medication': 'Loratadine', 'doctor': 'Dr. Lee', 'address': 'Jalan Pine 321'},
    {'name': 'David', 'age': 45, 'blood_pressure': '140/95', 'disease': 'Asma', 'medication': 'Albuterol', 'doctor': 'Dr. White', 'address': 'Jalan Birch 987'},
    {'name': 'Emily', 'age': 28, 'blood_pressure': '118/78', 'disease': 'Flu', 'medication': 'Oseltamivir', 'doctor': 'Dr. Martinez', 'address': 'Jalan Maple 654'},
    {'name': 'Michael', 'age': 50, 'blood_pressure': '135/85', 'disease': 'Artritis', 'medication': 'Ibuprofen', 'doctor': 'Dr. Brown', 'address': 'Jalan Cedar 246'},
    {'name': 'Sophia', 'age': 22, 'blood_pressure': '105/65', 'disease': 'Demam', 'medication': 'Paracetamol', 'doctor': 'Dr. Wilson', 'address': 'Jalan Willow 753'},
    {'name': 'William', 'age': 38, 'blood_pressure': '125/82', 'disease': 'Kolesterol', 'medication': 'Atorvastatin', 'doctor': 'Dr. Taylor', 'address': 'Jalan Fir 159'},
    {'name': 'Olivia', 'age': 32, 'blood_pressure': '112/72', 'disease': 'Sakit Kepala', 'medication': 'Acetaminophen', 'doctor': 'Dr. Anderson', 'address': 'Jalan Spruce 852'},
    {'name': 'James', 'age': 55, 'blood_pressure': '145/88', 'disease': 'Gangguan Pencernaan', 'medication': 'Omeprazole', 'doctor': 'Dr. Harris', 'address': 'Jalan Aspen 468'},
    {'name': 'Emma', 'age': 27, 'blood_pressure': '117/77', 'disease': 'Infeksi Saluran Kemih', 'medication': 'Ciprofloxacin', 'doctor': 'Dr. Thomas', 'address': 'Jalan Cherry 357'},
    {'name': 'Alexander', 'age': 42, 'blood_pressure': '128/84', 'disease': 'Pendarahan Lambung', 'medication': 'Pantoprazole', 'doctor': 'Dr. Evans', 'address': 'Jalan Holly 246'},
    {'name': 'Ava', 'age': 29, 'blood_pressure': '120/80', 'disease': 'Gigi Sensitif', 'medication': 'Fluoride', 'doctor': 'Dr. Moore', 'address': 'Jalan Laurel 951'},
    {'name': 'Benjamin', 'age': 48, 'blood_pressure': '132/87', 'disease': 'Obesitas', 'medication': 'Orlistat', 'doctor': 'Dr. Garcia', 'address': 'Jalan Birch 753'},
    {'name': 'Isabella', 'age': 31, 'blood_pressure': '114/76', 'disease': 'Pusing', 'medication': 'Diazepam', 'doctor': 'Dr. King', 'address': 'Jalan Pine 951'},
    {'name': 'Daniel', 'age': 37, 'blood_pressure': '123/79', 'disease': 'Stres', 'medication': 'Alprazolam', 'doctor': 'Dr. Martinez', 'address': 'Jalan Elm 357'},
    {'name': 'Mia', 'age': 26, 'blood_pressure': '108/68', 'disease': 'Gangguan Kecemasan', 'medication': 'Sertraline', 'doctor': 'Dr. Lee', 'address': 'Jalan Oak 753'},
    {'name': 'Ethan', 'age': 33, 'blood_pressure': '118/74', 'disease': 'Depresi', 'medication': 'Escitalopram', 'doctor': 'Dr. Smith', 'address': 'Jalan Cedar 159'},
    {'name': 'Charlotte', 'age': 34, 'blood_pressure': '119/76', 'disease': 'Insomnia', 'medication': 'Zolpidem', 'doctor': 'Dr. Brown', 'address': 'Jalan Pine 357'}
]


# Route to serve HTML file for displaying health data
@app.route('/datapasien')
def serve_datapasien_html():
    return render_template('index.html', data=data_pasien)

# Route to return health data as JSON
@app.route('/healthdata')
def get_health_data():
    return jsonify(data_pasien)

# Route to serve detail_pasien.html
@app.route('/detail_pasien.html')
def serve_detail_pasien_html():
    name = request.args.get('name')
    patient = next((patient for patient in data_pasien if patient['name'] == name), None)
    if patient:
        return render_template('detail_pasien.html', patient=patient)
    else:
        return 'Data pasien tidak ditemukan', 404

if __name__ == '__main__':
    app.run(debug=True)
