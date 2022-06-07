# Importing Necessary modules
#import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import pickle as pkl
import numpy as np


# Loading predict model
predict_model = pkl.load(open("model/saved_model_01.pkl","rb"))


# Declaring our FastAPI instance
app_model_01 = FastAPI()

# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    user_id : int
    mean_score : float



# Creating an Endpoint to receive the data to make prediction on.
@app_model_01.post('/predict')
def predict(data: request_body):
    # Making the data in a form suitable for prediction
    test_data_a = [[
            data.user_id,
            data.mean_score
    ]]
    
    # user_idx = test_data_a[0]
    test_data_b = np.array(test_data_a).reshape(-1, 1)
    # Predicting the Class
    class_idx = predict_model.predict(test_data_b)[1]
    # Return the Result
    return {'user_id': data.user_id, 'prediction': class_idx}    


#uvicorn.run(app_model_01)
