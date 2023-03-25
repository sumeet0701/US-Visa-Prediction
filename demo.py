from visa.logger import logging
from visa.exception import CustomException
from visa.config.configuration import Configuration
from visa.pipeline.pipeline import Pipeline
from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact

import os
import sys

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        raise CustomException(e,sys) from e
    

if __name__ == "__main__":
    main()
    