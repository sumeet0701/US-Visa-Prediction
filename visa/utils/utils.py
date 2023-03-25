import os, sys
import yaml
from visa.exception import CustomException


def write_ymal_file(file_path:str,data:dict=None):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as f:
            if data is not None:
                return yaml.dump(data,f)
    except Exception as e:
        raise CustomException(e,sys) from e
    
def read_ymal_file(file_path:str)-> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    
    try:
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise CustomException(e,sys) from e