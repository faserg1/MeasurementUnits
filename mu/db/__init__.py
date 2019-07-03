#!/usr/bin/env python3

from .database import Database
from .scheme.model import Model

# Инициализация базовой модели базой данных
Model.init(Database.get())