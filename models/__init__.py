#!/usr/bin/python3
"""called every time you use this model"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
