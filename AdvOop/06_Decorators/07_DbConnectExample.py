
from functools import wraps
from multiprocessing.sharedctypes import Value
from time import sleep
import psycopg2

def retryConnection(retryCount, delayTime):
    def retryDecorator(func):
        wraps(func)
        def functionWrapper(*args, **kwargs):
            result = None
            lastExecption = []

            for i in range(retryCount):
                try:
                    result = func(*args, **kwargs)
                    if result:
                        return result
                    else:
                        raise ValueError()

                except Exception as e:
                    lastExecption.append(e)

                sleep(delayTime)
            
            if lastExecption:
                for e in lastExecption:
                    print(e)

        return functionWrapper

    return retryDecorator


class DbHandler:
    def __init__(self, dbName, dbUser, dbPassword, dbHost) -> None:
        self.dbUser = dbUser
        self.dbPassword = dbPassword
        self.dbName = dbName
        self.dbHost = dbHost

    @retryConnection(retryCount=5, delayTime=1)
    def getConnection(self):
        conn = psycopg2.connect(
                host = self.dbHost,
                database = self.dbName,
                user = self.dbUser,
                password = self.dbPassword)

        return conn