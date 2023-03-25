import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}"


CURRECT_TIME_STAMP = get_current_time_stamp
ROOT_DIR= os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

#data ingestion related parameters

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"


# training pipeline related parameters

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = 'pipeline'

#Company variables
COLUMN_COMPANY_AGE = "company_age"
COLUMN_YEAR_ESTB = "yr_of_estab"
COLUMN_ID = "case_id"
COLUMN_CASE_STATUS = "case_status"
# Data Validation related parameters


# Data Transformation related parameters


# model Training related parameters


# model Evaluation related parameters


# Model Pusher related parameters



