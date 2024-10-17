from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('sk-OQMGQQNQbM9GzES5NiYJ6CpjULgY4-F6nHzW9dtNWXT3BlbkFJgTryoDAV5zhvJ3o8LCavYWUr1AoxLTBsIsFIkNcCYA')

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    data = request.json
    crop = data['crop']
    symptoms = data['symptoms']
    weather = data['weather']
    soil = data['soil']
    fertilizer = data['fertilizer']

    # Call your OpenAI API or any disease prediction logic here
    # For this example, let's assume a placeholder prediction
    prediction = f"Based on your input, {crop} might be affected by XYZ disease."

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
