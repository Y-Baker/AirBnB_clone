#!/usr/bin/python3
"""called every time you use this model"""
import sys
sys.path.append('/root/alx/AirBnB_clone') 
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
