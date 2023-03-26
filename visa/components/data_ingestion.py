from visa.constant import *
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import *
from visa.utils.utils import read_yaml_file
from visa.entity.artifact_entity import  DataIngestionArtifact
from visa.entity.config_entity import DataIngestionConfig
from visa.config.configuration import Configuration
from datetime import datetime
from six.moves import urllib
from sklearn.model_selection import train_test_split

import sys,os
import pandas as pd
import numpy as np




class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info("-------------------------------Data Ingestion Logging Started-------------------")
            self.data_ingestion_config = data_ingestion_config
        except  Exception as e:
            raise CustomException(e,sys) from e


    def download_data(self)-> str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(raw_data_dir, exist_ok=True)
            visa_file_name = os.path.basename(download_url)
            raw_file_path = os.path.join(raw_data_dir,visa_file_name)

            logging.info(f"Downloading file from:[{download_url}]   into :[{raw_file_path}] ")

            urllib.request.urlretrieve(download_url, raw_file_path)

            logging.info(f"File :[{raw_file_path}] has been downloaded successfully.")

            return raw_file_path
        
        except  Exception as e:
            raise CustomException(e,sys) from e
        
    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion.raw_data_dir
            file_name =os.listdir(raw_data_dir)[0]
            visa_file_name = os.path.join(raw_data_dir,file_name)
            today_date = date.today()
            current_year = today_date.year

            visa_df = pd.read_csv(visa_file_name)
            visa_df[COLUMN_COMPANY_AGE]=  current_year - visa_df[COLUMN_YEAR_ESTB]
            visa_df.drop([COLUMN_ID,COLUMN_YEAR_ESTB], axis=1, inplace=True)
            visa_df[COLUMN_CASE_STATUS] = np.where(visa_df[COLUMN_CASE_STATUS] == "Denied", 1,0)

            logging.info(f"Splitting data into train and test data")

            train_set = None
            test_set = None

            train_set ,test_set = train_test_split(visa_df,test_size= 0.2, random_state=42)
            
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

# ****************************************************************************************************************

            if train_set is not None :
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(f"Exporting training dataset to file:[{train_file_path}]")
                train_set.to_csv(train_file_path, index = False)

            if test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok= True)
                logging.info(f"Exporting test dataset to file:[{test_file_path}]")
                test_set.to_csv(test_file_path, index =False)
            

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path= train_file_path,
                test_file_path= test_file_path,
                is_ingestd= True,
                message= f"Data ingestion Completed Successfully"
            )

            logging.info(f"Data ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact       

        except  Exception as e:
            raise CustomException(e,sys) from e
        

    def intiate_data_ingestion(self):
        try:
            raw_file_path = self.download_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise CustomException(e,sys) from e
        