from src.paths import PARENT_DIR
from dotenv import load_dotenv
import os
load_dotenv(PARENT_DIR / '.env')

HOPSWORKS_PROJECT_NAME = 'TaxiDemandPredictorNYC'
try:
    # HOPSWORKS_PROJECT_NAME = os.environ['HOPSWORKS_PROJECT_NAME']
    HOPSWORKS_API_KEY = os.environ['HOPSWORKS_API_KEY']
except:
    raise Exception(
        'Create an .env file on the project root with the HOPSWORKS_API_KEY')
FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 3
