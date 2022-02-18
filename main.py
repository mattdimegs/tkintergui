from login import *
from config import *

if __name__ == '__main__':
    mainPage = Gui()

db = mysql.connector.connect(
    host=hostAddress,
    user=username,
    passwd=password,
    database=dbName
)

