import logging
import os
from datetime import datetime
from settings import ROOT_WORKING_DIRECTORY, LOGS_FOLDER


def create_logs():
    """
    Function that creates logs on ROOT_WORKING_DIRECTORY\output\logs
    """
    results_path = f"{ROOT_WORKING_DIRECTORY}/output/{LOGS_FOLDER}"
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    return results_path


create_logs()
logg = logging.getLogger()  # param '__name__' in need
logg.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
file_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S.log")

file_handler = logging.FileHandler(f"{ROOT_WORKING_DIRECTORY}/output/{LOGS_FOLDER}/{file_name}",
                                   encoding='utf-8')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logg.addHandler(file_handler)
logg.addHandler(stream_handler)
