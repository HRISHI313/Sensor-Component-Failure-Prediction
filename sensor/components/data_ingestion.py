from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.config_entity import DataIngestionConfig
from sensor.exception import CustomException
from sensor.logger import logging
from sensor.utils import export_collection_as_dataframe
import os,sys
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:



    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try: 
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)
    def initiate_data_ingestion()->DataIngestionArtifact:
        try:
            logging.info('Exporting collection as dataframe')
            df = export_collection_as_dataframe(database_name = self.data_ingestion_config.database_name, 
            collection_name = self.data_ingestion_config.collection_name)

            logging.info('Replacing na with NAN')
            df.replace({'na':np.NAN},inplace = True)

            logging.info('Splitting dataframe into train and test')
            train_df,test_df = train_test_split(df,test_size = self.data_ingestion_config.test_size)

            logging.info('creating dataset as  directory')
            os.makedirs(self.data_ingestion_config.dataset_dir,exist_ok = True)

            logging.info('Saving train and test file')
            train_df.to_csv(self.data_ingestion_config.train_file_path,index = False,header = True)
            test_df.to_csv(self.data_ingestion_config.test_file_path,index = False,header = True)

            logging.info('Preparing data ingestion artifact')
            data_ingestion_artifact = DataIngestionArtifact(train_file_path = data_ingestion_config.train_file_path,
             test_file_path = data_ingestion_config.test_file_path)

            logging.info(f'Data ingestion artifact: {data_ingestion_artifact}')
            return





        
        
        
        except Exception as e:
            raise CustomException(e, sys)



