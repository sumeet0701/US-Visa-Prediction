# namedtuple is mutable whereas the tuple is immutable
from collections import namedtuple

DataIngestionConfig = namedtuple('DataIngestionConfig',[
    "dataset_download_url",
    "raw_data_dir",
    "ingested_train_dir",
    "ingested_test_dir",])


TrainingPipelineConfig = namedtuple('TrainingPipelineConfig',[
    "artifact_dir" ])

                                     
DataValidationConfig =   namedtuple("DataValidationConfig",
                                 ["schema_file_dir"])

DataTransformationConfig = namedtuple("DataTransformationConfig",[
    "transformed_train_dir",
    "transformed_test_dir",
    "preprocessed_object_file_path",
    "feature_engineering_object_file_path"])

