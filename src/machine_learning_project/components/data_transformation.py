import os
import pandas as pd
from machine_learning_project import logger
from sklearn.model_selection import train_test_split
from machine_learning_project.config.configuration import DataTranformationConfig

class DataTransformation:

    def __init__(self, config : DataTranformationConfig):
        self.config = config

    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        logger.info("Spliting data into train and test set")
        train, test = train_test_split(data)

        logger.info("Saving train and test set to train.csv, test.csv")
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info("Spliting completed>>>>>>>>")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
