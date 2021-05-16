import json
import numpy as np
import os
import pickle
import joblib

def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It's the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION).
    # For multiple models, it points to the folder containing all deployed models (./azureml-models).
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'clf.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    data = np.array(json.loads(raw_data)['data'])
    # Make prediction.
    
    x = np.array([1 if data[0] == "female" else 0 , data[1] ])
    x = x.reshape(1 , -1)

    y_hat = model.predict_proba(x)
    # You can return any data type as long as it's JSON-serializable.
    
    
    return json.dumps({"survival_probability" : y_hat[0][1]})
    

