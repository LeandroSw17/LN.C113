import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Leandro Oliveira/Desktop/prog/PRO_1-4_C113_TemplateDoProjeto-main/.gitattributes"

class ManipuladorEventos(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Criado: {event.src_path}")

    def on_deleted(self, event):
        print(f"Excluído: {event.src_path}")

    def on_modified(self, event):
        print(f"Modificado: {event.src_path}")

    def on_moved(self, event):
        print(f"Movido: de {event.src_path} para {event.dest_path}")


manipulador_eventos = ManipuladorEventos()

observer = Observer()

observer.schedule(manipulador_eventos, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
    observer.stop()
    observer.join()
