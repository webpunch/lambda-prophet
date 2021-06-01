import pandas as pd
from prophet import Prophet

def lambda_handler(event):
    # invocation
    data = event['data']
    class_args = event.get('class_args', {})
    make_future_dataframe_args = event.get('make_future_dataframe_args', {})

    df = pd.DataFrame(data, columns=['ds', 'y'])
    model = Prophet(**class_args)
    model.fit(df)
    future = model.make_future_dataframe(**make_future_dataframe_args)
    forecast = model.predict(future)
    return forecast.to_json(orient='records')
