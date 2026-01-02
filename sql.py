import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "banco_oficial.db")

def conectar():
    return sqlite3.connect(DB_PATH)
