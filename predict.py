import pandas as pd
from sklearn.pipeline import Pipeline
import pickle
import matplotlib.pyplot as plt
from fpdf import FPDF

def predict_home_price(details: dict, model: Pipeline, features: list) -> float:
    """
    Predicts the home price based on user input.

    Parameters:
    details (dict): Dictionary with home details.
    model (Pipeline): Trained model.
    features (list): List of feature names.

    Returns:
    float: Predicted price.
    """
    user_input_df = pd.DataFrame([details], columns=features)
    estimated_price = model.predict(user_input_df)

    return estimated_price[0]

with open('trained_model_new.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']
user_details = {}

for feature in features:
    value = float(input(f"Enter value for {feature}: "))
    user_details[feature] = value

estimated_price = predict_home_price(user_details, loaded_model, features)

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
pdf.output("Prediction_Report.pdf")

print(f"\nThe estimated price of the home is: ${estimated_price:.2f}")
print("Prediction report saved as 'Prediction_Report.pdf'")
