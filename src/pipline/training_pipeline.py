import os
import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion ##Data ingestion component
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig #Data ingestion configuration 
from src.entity.artifact_entity import DataIngestionArtifact  ##Data ingestion artifact 

from src.components.data_validation import DataValidation
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifact

from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact

from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifact_entity import ModelTrainerArtifact

from src.components.model_evaluation import ModelEvaluation
from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import ModelEvaluationArtifact

from src.components.model_pusher import ModelPusher
from src.entity.config_entity import ModelPusherConfig
from src.entity.artifact_entity import ModelPusherArtifact



class TrainPipeline:
    def __init__(self):
        """initialise the Data ingestion configuration because it has 
        required information about the data, it's naming and its location even it's artifacts name and folder"""
        self.data_ingestion_config=DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()
        self.data_transformation_config=DataTransformationConfig()
        self.model_trainer_config=ModelTrainerConfig()
        self.model_evaluation_config=ModelEvaluationConfig()
        self.model_puhser_config=ModelPusherConfig()

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
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            """data_ingestion_artifact: For reading the ingestion data (train and test).
               data_validation_config: Expects the location where it can save its validation report file.
            """
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact
        except Exception as e:
            raise MyException(e, sys) from e
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_ingestion_artifact=data_ingestion_artifact,
                                                     data_transformation_config=self.data_transformation_config,
                                                     data_validation_artifact=data_validation_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise MyException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        """
        This method of TrainPipeline class is responsible for starting model training
        """
        try:
            model_trainer=ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                       model_trainer_config=self.model_trainer_config)
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise MyException(e,sys)
        
    def start_model_evaluation(self,data_ingestion_artifact=DataIngestionArtifact,
                               model_trainer_artifact=ModelTrainerArtifact)->ModelEvaluationArtifact:
        """
        This method of TrainPipeline class is responsible for starting modle evaluation
        """
        try:
            model_evaluation=ModelEvaluation(model_eval_config=self.model_evaluation_config,
                                            data_ingestion_artifact=data_ingestion_artifact,
                                             model_trainer_artifact=model_trainer_artifact)
            model_evaluation_artifact=model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact
        except Exception as e:
            raise MyException(e,sys)
    
    def start_model_pusher(self, model_evaluation_artifact=ModelEvaluationArtifact)->ModelPusherArtifact:
        """
        This method of TrainPipeline class is responsible for starting model pushing
        """
        try:
            model_pusher=ModelPusher(model_pusher_config=self.model_puhser_config,
                                     model_evaluation_artifact=model_evaluation_artifact)
            model_pusher_artifact=model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise MyException(e,sys)
        
    def run_pipeline(self,)-> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                                                        data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_evaluation_artifact=self.start_model_evaluation(data_ingestion_artifact=data_ingestion_artifact,
                                                                  model_trainer_artifact=model_trainer_artifact)
            if not model_evaluation_artifact.is_model_accepted:
                logging.info(f"Model not accepted.")
                return None 
            model_pusher_artifact=self.start_model_pusher(model_evaluation_artifact=model_evaluation_artifact)
        except Exception as e:
            raise MyException(e, sys)
        


        

