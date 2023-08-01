from sensor.pipeline.training_pipeline import TrainingPipeline
from sensor.pipeline.training_pipeline import TrainingPipeline
from sensor.entity.config_entity import TrainingPipeLineConfig
from sensor.exception import CustomException
from sensor.logger import logging

if __name__=='__main__':
    try: 
        training_pipeline_config = training_pipeline.TrainingPipeLineConfig()

        training_pipeline = TrainingPipeline(training_pipeline_config = training_pipeline_config)

        training_pipeline.start()

    except Exception as e:
        logging.info(e)
        print(e)
        

