import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper(AbstractContextManager, ABC):
    def __init__(self):
        self._cnx = None

    def __enter__(self):
        """Wird ausgeführt, sobald die Klasse mit dem "with" Befehl aufgerufen wird"""

        if os.getenv('GAE_ENV', '').startswith('standard'):
            """
            Landen wir in diesem Zweig, so haben wir festgestellt, dass der Code in der Cloud abläuft.
            Die App befindet sich somit im **Production Mode** und zwar im *Standard Environment*.
            Hierbei handelt es sich also um die Verbindung zwischen Google App Engine und Cloud SQL."""
            self._cnx = connector.connect(user='root', password='Sopragruppe12!',
                                          unix_socket='/cloudsql/learned-surge-353408:europe-west3:zeiterfassung-db',
                                          database='Zeiterfassung')
        else:
            """Es soll eine Verbindung zur Datenbank erstellt werden"""
            self._cnx = connector.connect(user='root', password='Sopragruppe12!',
                                  host='127.0.0.1',
                                  database='Zeiterfassung', auth_plugin='mysql_native_password')

        return self

    def __exit__(self,  exc_type, exc_val, exc_tb):
        """Wird ausgeführt, sobald die Befehle, die mit "with" ausgeführt werden, beendet werden"""

        """ Wir trennen die Datenbankverbindung"""
        self._cnx.close()

    """ @abstractmethod -> Wir möchten die erbenden Klassen zwingen, die folgenden Methoden zu besitzen!"""
    @abstractmethod
    def find_all(self):
        pass

    #@abstractmethod
    def insert(self, value):
        pass

    #@abstractmethod
    def delete(self, value):
        pass