from collections import namedtuple


#Data Ingestion Arifacts
DataIngestionArtifact = namedtuple("DataIngestionArtifact", 
                                     ["train_file_path", 
                                      "test_file_path", 
                                      "is_ingestd",
                                      "message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",[
    "schema_file_path",
    "is_validated",
    "message"
])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",[
    "is_transformed",
    "message",
    "transformed_train_file_path",
    "transformed_test_file_path",
    "preprocessed_object_file_path",
    "feature_engineering_object_file_path"])

