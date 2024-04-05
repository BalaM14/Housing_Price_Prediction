from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
import warnings
warnings.filterwarnings('ignore')

def main():
    try:
        pipeline=Pipeline()
        pipeline.start()
        logging.info(f"Main function execution completed successfully")
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
