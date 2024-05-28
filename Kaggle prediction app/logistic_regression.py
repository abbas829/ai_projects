import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Function to load data
def load_data(file):
    return pd.read_csv(file)

# Function for data preprocessing
def preprocess_data(train_df, test_df, target_column):
    # Combine train and test data for consistent preprocessing
    combined = pd.concat([train_df.drop(target_column, axis=1), test_df], axis=0)
    
    # Encode categorical variables
    le = LabelEncoder()
    for col in combined.select_dtypes(include=['object']).columns:
        combined[col] = le.fit_transform(combined[col].astype(str))

    # Separate the combined data back into train and test sets
    X_train = combined.iloc[:len(train_df), :]
    X_test = combined.iloc[len(train_df):, :]

    y_train = train_df[target_column]

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, y_train, X_test_scaled

# Function to train and evaluate the model
def train_and_evaluate_model(X, y, model):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)

    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted')
    recall = recall_score(y_val, y_pred, average='weighted')
    f1 = f1_score(y_val, y_pred, average='weighted')

    return model, accuracy, precision, recall, f1

# Function to make predictions on the test data
def make_predictions(model, test_data):
    return model.predict(test_data)

# Streamlit app
def main():
    st.title("Kaggle Competition Prediction App")

    st.markdown("""
        This app allows you to upload your train, test, and sample submission files to train a model and make predictions.
        - `train.csv`: Training data with features and the target column.
        - `test.csv`: Test data with features (without the target column).
        - `sample_submission.csv`: Sample submission file with the required format for predictions.

        **Target Column**: The column in your training data that contains the labels you want to predict.
    """)

    # File uploaders
    train_file = st.file_uploader("Upload train.csv", type="csv")
    test_file = st.file_uploader("Upload test.csv", type="csv")
    sample_submission_file = st.file_uploader("Upload sample_submission.csv", type="csv")

    target_column = st.text_input("Enter the target column name")
    id_column = st.text_input("Enter the ID column name")

    if train_file is not None and test_file is not None and sample_submission_file is not None and target_column and id_column:
        train_data = load_data(train_file)
        test_data = load_data(test_file)
        sample_submission = load_data(sample_submission_file)

        if target_column not in train_data.columns:
            st.error(f"Target column '{target_column}' not found in the training data.")
            return

        if id_column not in test_data.columns or id_column not in sample_submission.columns:
            st.error(f"ID column '{id_column}' not found in the test data or sample submission file.")
            return

        X_train, y_train, X_test = preprocess_data(train_data, test_data, target_column)

        model_choice = st.selectbox("Choose a model", ["Logistic Regression", "Random Forest", "SVM", "Hist Gradient Boosting"])

        if model_choice == "Logistic Regression":
            model = LogisticRegression()
        elif model_choice == "Random Forest":
            model = RandomForestClassifier()
        elif model_choice == "SVM":
            model = SVC()
        elif model_choice == "Hist Gradient Boosting":
            model = HistGradientBoostingClassifier()

        model, accuracy, precision, recall, f1 = train_and_evaluate_model(X_train, y_train, model)
        st.write(f"Model: {model_choice}")
        st.write(f"Accuracy: {accuracy}")
        st.write(f"Precision: {precision}")
        st.write(f"Recall: {recall}")
        st.write(f"F1 Score: {f1}")

        predictions = make_predictions(model, X_test)
        sample_submission[target_column] = predictions

        st.subheader("Predicted Output")
        st.write(sample_submission)

        csv = sample_submission.to_csv(index=False).encode()
        st.download_button(
            label="Download Predictions as CSV",
            data=csv,
            file_name='predictions.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()
