from lambda_function import lambda_handler

observations = [
    ['2021-04-20', 97.4],
    ['2021-04-27', 96.7],
    ['2021-05-11', 96.0],
    ['2021-05-18', 94.2],
    ['2021-05-25', 93.7],
    ['2021-06-01', 94.3],
]

class_args = {
    'daily_seasonality': False,
    'weekly_seasonality': False,
    'yearly_seasonality': False,
}

make_future_dataframe_args = {
    'periods': 50,
    'freq': 'w',
}

event = {
    'data': observations,
    'class_args': class_args,
    'make_future_dataframe_args': make_future_dataframe_args,
}

result = lambda_handler(event)

print(result)
