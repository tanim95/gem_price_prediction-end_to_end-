# Student Math Score Prediction Web App

This web application is built using Flask and allows users to predict a student's math score based on their reading score, writing score, gender, ethnicity, and lunch type.

## Prerequisites

- Python 3.8.10
- Flask
- scikit-learn
- pickle

## Installation

1. Clone the repository: https://github.com/tanim95/endtoend_mlproject.git

2. Run virtual environment: venv/Scripts/activate

[NOTE: if venv do not run then firtst try 'Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass ',then run the code command again 'venv/Scripts/activate']

3. Activate the virtual environment:

- For Windows:

  ```
  venv\Scripts\activate
  ```

- For macOS/Linux:

  ```
  source venv/bin/activate
  ```

4. Install the dependencies:

pip install -r requirements.txt

5. Run the application: python application.py

6. Open a web browser and navigate to `http://localhost:5000` to access the web app.

## Usage

- On the home page, fill in the required details such as gender, ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score.
- Click the "Predict your Math Score" button to submit the form.
- The predicted math score will be displayed on the page.

## Directory Structure

- `app.py`: The main Flask application file.
- `src`: The main folder contain main modules.
- `artifact`: Contains necessary pickle file.
- `templates/`: Contains HTML templates for the web app.
- `static/`: Contains static files such as CSS stylesheets and JavaScript files.
- `model.pkl`: The trained machine learning model serialized using pickle.

## Acknowledgements

- I made this project with the help of YouTuber 'KRISH NAIK'.

- Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
- The data consists of 8 column and 1000 rows.

## License
