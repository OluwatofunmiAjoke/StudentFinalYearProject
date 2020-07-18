from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class PredictConfig(AppConfig):
    # create path to models
    path = os.path.join(settings.MODELS, 'finalized_prediction_model.sav')
 
    # load models into separate variables
    # these will be accessible via this class
    # with open(path, 'rb') as pickled:
    #    data = pickle.load(pickled)
    # regressor = data['regressor']

    with open('predict/model/finalized_prediction_model.sav' ,'rb') as f:
    	loaded_model = pickle.load(f)
    
