from flask import Flask, request, jsonify, send_file
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd
import matplotlib
import numpy as np

matplotlib.use('Agg')  # Use the Agg backend for Matplotlib
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def predict_home_price(details: dict, model: Pipeline, features: list) -> float:
    # Your prediction function remains the same
    user_input_df = pd.DataFrame([details], columns=features)
    estimated_price = model.predict(user_input_df)
    return estimated_price[0]


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price_api():
    try:
        # Load the trained model
        with open('trained_model_new.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        # Define the list of features
        features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']

        # Get user input as JSON
        user_details = request.json

        # Call the prediction function
        estimated_price = predict_home_price(user_details, loaded_model, features)

        # Create a PDF report
        plt.figure(figsize=(10, 6))
        plt.bar(features, user_details.values(), color='skyblue')
        plt.title(f'Estimated Home Price: ${estimated_price:.2f}')
        plt.ylabel('Values')
        plt.xlabel('Features')
        plt.tight_layout()
        image_path = 'temp_report_image.png'
        plt.savefig(image_path)
        plt.close()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Home Price Prediction Report", ln=True, align='C')
        pdf.ln(10)

        # Add details in numbers to the report
        pdf.cell(200, 10, txt=f"Estimated Home Price: ${estimated_price:.2f}", ln=True)
        pdf.ln(10)

        for feature, value in user_details.items():
            pdf.cell(200, 10, txt=f"{feature.capitalize()}: {value}", ln=True)
            pdf.ln(10)

        pdf.image(image_path, x=10, y=pdf.get_y(), w=190)

        pdf_file_path = 'Prediction_Report.pdf'

        # Check if the file exists before attempting to delete it
        if os.path.exists(pdf_file_path):
            try:
                # Delete the file
                os.remove(pdf_file_path)
            except OSError as e:
                print(f"Error deleting file '{pdf_file_path}': {e}")

        pdf.output(pdf_file_path)

        # Clean up temporary image file
        os.remove(image_path)

        estimated_price = np.float64(estimated_price)
        formatted_price = "{:.2f}".format(estimated_price)

        # Include the feature names in the API response
        response_data = {
            "estimated_price": formatted_price,
            "directory:": os.getcwd() + "/" + pdf_file_path,
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
