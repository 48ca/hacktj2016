from flask.ext.sqlalchemy import SQLAlchemy
import os
import getpass

username = input("Enter admin username: ")
print("Enter admin password: ")
password = getpass.getpass()

