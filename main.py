from IRIS_MLops import logger

from IRIS_MLops.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from IRIS_MLops.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from IRIS_MLops.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from IRIS_MLops.pipeline.stage04_model_training import ModelTrainingPipeline
from IRIS_MLops.pipeline.stage05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Training stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e