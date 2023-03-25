from collections import namedtuple


#Data Ingestion Arifacts
DataIngestionArtifact = namedtuple("DataIngestionArtifact", 
                                     ["train_file_path", "test_file_path", "is_ingestd","message"])