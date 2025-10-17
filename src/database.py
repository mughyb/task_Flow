import sqlite3
from .modelos import Tarea, Proyecto
import os

DATABASE_NAME= 'tareas.db'


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def crear_tarea(self, tarea: Tarea) -> Tarea:
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(""""
        INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_limite, prioridad, estado, proyecto_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (tarea._titulo, tarea._descripcion, tarea._fecha_creacion, tarea._fecha_limite,
          tarea._prioridad, tarea._estado, tarea._proyecto_id))
    
    tarea.id = cursor.lastrowid
    conn.commit()
    conn.close()
    return tarea