from utils import dump_csv_file_to_mongo_connection

if __name__=="__main__":
    file_path = 'aps_failure_training_set1.csv'
    database_name = 'Sensor_Data'
    collection_name = 'aps_sensor_reading'
    dump_csv_file_to_mongo_connection(file_path,database_name,collection_name)
