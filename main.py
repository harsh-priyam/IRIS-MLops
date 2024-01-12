from IRIS_MLops import logger

from IRIS_MLops.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from IRIS_MLops.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from IRIS_MLops.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline


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