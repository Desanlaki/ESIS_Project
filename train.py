import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import pickle

# ... [all the imports]

# Load dataset
df = pd.read_csv('data.csv')

# Handle missing values
df = df.fillna(0)

# Select relevant features and target
features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']
target = 'price'
X = df[features]
y = df[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a pipeline with a scaler and the model
model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
model.fit(X_train, y_train)

# Save the trained model as a pickle string.
with open('trained_model_new.pkl', 'wb') as file:
    pickle.dump(model, file)
