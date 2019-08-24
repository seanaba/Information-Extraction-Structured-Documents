"""
Basic information extraction (structured documents)
1- Collect template/test documents
2- Align test documents with the template
3- Extract information
"""
import os
from extract import ExtractDoc


if __name__ == "__main__":
    """
    Data path 
    Classification model path 
    Train classification model
    """
    code_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname(code_path)
    data_path = os.path.join(base_path, 'data')
    config_path = os.path.join(base_path, 'config')
    try:
        info_extract_obj = ExtractDoc(data_path, config_path)
        info_extract_obj.extract_info()
    finally:
        del info_extract_obj
