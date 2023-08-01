import json
from sensor.exception import CustomException
from sensor.logger import logging
import os,sys

from config import mongo_client
import pandas as pd
import logging
def dump_csv_file_to_mongo_connection(file_path:str,database_name:str,collection_name:str)->None:
    try:
        df = pd.read_csv(file_path)
        logging.info(f'Rows and Columns {df.shape}')


        df.reset_index(drop = True,inplace = True)
        json_record = list(json.loads(df.T.to_json()).values())

        mongo_client[database_name][collection_name].insert_many(json_record)

    except Exception as e:
        raise e

def export_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        if '_id' in df.columns.to_list():
            df.drop('_id',axis = 1)
        return df
    except Exception as e:
        raise CustomException(e, sys)
