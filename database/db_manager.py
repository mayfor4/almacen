import sqlite3
import os

from pathlib import Path

DB_PATH = Path("C:/Users/diego/OneDrive/Documentos/endcuatri/goyo/almacen/solicitudes.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            expediente TEXT,
            carrera TEXT,
            material TEXT,
            fecha TEXT DEFAULT CURRENT_TIMESTAMP,
            estado TEXT DEFAULT 'Pendiente'
        );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        rol TEXT  -- "estudiante" o "admin"
    )
    """)
    conn.commit()
    conn.close()

def insertar_solicitud( nombre, expediente,carrera, material,):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO solicitudes (nombre, expediente, carrera, material) VALUES (?, ?, ?, ?)",
                   ( nombre, expediente,carrera, material,))
    conn.commit()
    conn.close()

   

def agregar_usuario(username, password, rol):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)",
                   (username, password, rol))
    conn.commit()
    conn.close()

def validar_usuario(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuarios WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]  # Devuelve el rol
    return None