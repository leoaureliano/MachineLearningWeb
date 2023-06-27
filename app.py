from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    # Retrieve input data from the form
    input_data = [float(request.form['feature1']), float(request.form['feature2']), ...]

    # Convert input data to a pandas DataFrame
    data = pd.DataFrame([input_data], columns=['feature1', 'feature2', ...])

    # Append the new data to an existing dataset or create a new dataset
    existing_data = pd.read_csv('user_data.csv')  # Load existing data if available
    updated_data = existing_data.append(data, ignore_index=True)

    # Save the updated data to a CSV file
    updated_data.to_csv('user_data.csv', index=False)

    # Display a success message to the user
    message = "Data saved successfully!"
    return render_template('index.html', message=message)

@app.route('/plot_data')
def plot_data():
    # Load the user-generated data
    data = pd.read_csv('user_data.csv')

    # Extract the features and target variable
    x = data['feature1']
    y = data['feature2']

    # Create a scatter plot
    plt.scatter(x, y)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('User-generated Data')

    # Save the plot as an image
    plt.savefig('static/data_plot.png')

    # Display the plot image on the result page
    return render_template('result.html', plot_image='data_plot.png')

app.run(host='0.0.0.0', port=81, debug = True)
