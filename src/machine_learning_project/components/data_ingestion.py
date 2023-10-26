import os
import zipfile
import urllib.request as request
from pathlib import Path
from machine_learning_project import logger
from machine_learning_project.utils.common import get_size
from machine_learning_project.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config : DataIngestionConfig):
        self.config = config

    
    def download_file(self):

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(

                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f'{filename} download! with the following info \n{headers}')

        else:
            logger.info(f'File already exists of size : {get_size(Path(self.config.local_data_file))}')

    def extract_zipfile(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)