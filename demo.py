##local package
## -e . is helpful on this cases when we have to load our locally created packages in working environment
from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# #----------------------------------------
# # # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try: ##try to the block of code
#     a = 1+'Z'
# except Exception as e: ##if any exception occurs then enter into the except block
#     # Log the error message
#     logging.info(e)
#     raise MyException(e, sys) from e ##raise the exception
#----------------------------------------

from src.pipline.training_pipeline import TrainPipeline
##create an object of TrainPipeline class
pipeline=TrainPipeline()
##Call one of the method of TrainPipeline class to run entire pipeline that i build so far
pipeline.run_pipeline() 
# -------------------
# import os
# from datetime import date
# from dotenv import load_dotenv
# load_dotenv()

# # For MongoDB connection
# MONGODB_URL_KEY = os.getenv("MONGODB_URL")

# if MONGODB_URL_KEY is None:
# 	raise ValueError("MONGODB_URL is not set in the .env file or the .env file is missing.")

# print(MONGODB_URL_KEY)