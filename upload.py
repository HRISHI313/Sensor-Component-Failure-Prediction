from sensor.utils import dump_csv_file_to_mongo_connection
from sensor.exception import CustomException
from sensor.logger import logging
import os,sys


def storing_data_in_mongo():
    try:
        file_path = '/config/workspace/aps_failure_training_set1.csv'
        database_name = 'Sensor_Data'
        collection_name = 'aps_sensor_reading'
        dump_csv_file_to_mongo_connection(file_path,database_name,collection_name)
    except Exception as e:
        raise e


if __name__=="__main__":
    storing_data_in_mongo()