On June, 7th, 2022 first model edition 3 (further simply the first model) of machine learning was deployed into heroku server. The first model presents a ordinary Decision Tree Regressor model and its application was based on FastAPI library for Python.
The first model isn’t very accuracy, because it will be upgraded soon.

The fist model gets POST request as JSON style {"user_id": X, "mean_score": Y}, where X - is user_id (integer) and Y - float number from 0 to 1,0 (indicates mean score of completed current exam result of some user) to link https://km-model-03.herokuapp.com/predict.

The first model answers by JSON style {"user_id": X,   "prediction": P}, where P - is BOLIAN number: 0 - fail, 1 - pass.
