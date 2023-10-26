from machine_learning_project import logger
from machine_learning_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from machine_learning_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from machine_learning_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from machine_learning_project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

logger.info("Welcome to my first mlops project")

STAGE_NAME = "Data Ingestion stage"

try:
   
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
   logger.exception(e)
   raise e

STAGE_NAME = "Model Trainer stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


