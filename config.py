import os, logging
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT', '8080'))
logging.basicConfig(
    filename=f'{os.path.dirname(__file__)}/logs/app.log',
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)
