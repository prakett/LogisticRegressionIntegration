import pickle
import logging
import numpy as np
import sys
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the path to the model folder
MODEL_PATH = "C:\\Users\\ASUS\\IdeaProjects\\LogisticRegressionIntegration\\src\\main\\resources\\model"

# Load the trained model, vectorizer, and scaler
try:
    logger.info("Loading model, vectorizer, and scaler...")
    with open(os.path.join(MODEL_PATH, 'logistic_regression_model.pkl'), 'rb') as model_file:
        model = pickle.load(model_file)
    with open(os.path.join(MODEL_PATH, 'tfidf_vectorizer.pkl'), 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    with open(os.path.join(MODEL_PATH, 'scaler.pkl'), 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    logger.info("Model, vectorizer, and scaler loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model, vectorizer, or scaler: {e}")
    sys.exit(1)

def predict(url):
    try:
        print(f"Received URL: {url}")
        # Transform the URL using the loaded vectorizer
        url_tfidf = vectorizer.transform([url])

        # Check if there are additional numerical features
        num_features = 48  # Adjust this to match the actual number of features your model expects
        if url_tfidf.shape[1] < num_features:
            # Dummy numerical features (zeros or some default value)
            numerical_features = np.zeros((1, num_features - url_tfidf.shape[1]))
        else:
            numerical_features = np.zeros((1, 0))

        # Scale the numerical features
        if numerical_features.shape[1] > 0:
            scaled_numerical_features = scaler.transform(numerical_features)
            combined_features = np.hstack((url_tfidf.toarray(), scaled_numerical_features))
        else:
            combined_features = url_tfidf.toarray()

        # Ensure combined_features has the correct number of features
        expected_features = 63121  # Replace with the number of features your model expects
        print(f"Combined features shape: {combined_features.shape}")
        if combined_features.shape[1] != expected_features:
            raise ValueError(f"Feature dimension mismatch: expected {expected_features} but got {combined_features.shape[1]}")

        # Make a prediction
        print("Making prediction...")
        prediction = model.predict(combined_features)
        prediction_proba = model.predict_proba(combined_features)[:, 1]

        # Interpret the prediction
        result = "Phishing" if prediction[0] == 1 else "Not Phishing"
        confidence = prediction_proba[0] * 100  # Convert to percentage

        print(f"Prediction: {result}")
        print(f"Confidence: {confidence:.2f}%")

        return result, confidence
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        sys.exit(1)

def main():
    # Get the URL input from the user (if applicable)
    url = sys.argv[1].strip()

    if not url:
        print("No URL provided. Exiting...")
        sys.exit(1)

    # Predict and display the result
    result, confidence = predict(url)

    if result is not None:
        print(f"Prediction: {result}")
        print(f"Confidence: {confidence:.2f}%")
    else:
        print("Error during prediction.")

if __name__ == '__main__':
    main()
