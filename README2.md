# Gem Price Prediction

This project aims to predict gem prices based on various features such as cut, color, clarity, depth, table, and dimensions (x, y, z).It is implemented in Python 3.8.10 within a virtual environment named 'venom'.

## Directory Structure

- `app.py`: The main Flask application file.
- `src`: The main folder contain main modules.
- `artifact`: Contains necessary pickle file.
- `templates/`: Contains HTML templates for the web app.
- `static/`: Contains static files such as CSS stylesheets and JavaScript files.
- `model.pkl`: The trained machine learning model serialized using pickle.

## Installation

1. Clone the repository:
   https://github.com/tanim95/end_to_end_gemprice.git

2. Create virtual environment:
   python -m venv venom
3. Activate the virtual environment:

- For Windows:

  ```
  venv\Scripts\activate
  ```

- For macOS/Linux:

  ```
  source venv/bin/activate
  [NOTE: if venv do not run then firtst try 'Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass ',then run the code command again 'venv/Scripts/activate']
  ```

## Dependencies

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- catboost
- xgboost
- dill
- flask

3. Install the required dependencies:
   pip install -r requirements.txt
   or,

   pip install pandas numpy seaborn matplotlib scikit-learn catboost xgboost dill flask
   or ,
   python -m pip install pandas numpy seaborn matplotlib scikit-learn catboost xgboost dill flask

## Data Source

https://www.kaggle.com/competitions/playground-series-s3e8/data

## How to Run

Just run the application.py file after installing all the dependency and creating virtual environment.

## License

This project is licensed under the MIT License
