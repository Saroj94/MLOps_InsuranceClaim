import os
import sys
from src.exception import MyException
from src.logger import logging
from src.components.data_ingestion import DataIngestion ##Data ingestion component
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig #Data ingestion configuration 
from src.entity.artifact_entity import DataIngestionArtifact  ##Data ingestion artifact 


class TrainPipeline:
    def __init__(self):
        """initialise the Data ingestion configuration because it has 
        required information about the data, it's naming and its location even it's artifacts name and folder"""
        self.data_ingestion_config=DataIngestionConfig()

    #data ingestion method
    def start_data_ingestion(self) ->DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e
        
    def run_pipeline(self,)-> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise MyException(e, sys)


        

