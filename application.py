from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity'),
            carat=request.form.get(
                'carat'),
            depth=request.form.get('depth'),
            table=request.form.get(
                'table'),
            x=request.form.get('x'),
            y=request.form.get('y'),
            z=request.form.get('z'),

        )
        pred_df = data.get_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])


if __name__ == '__main__':
    app.run(port=8000)
