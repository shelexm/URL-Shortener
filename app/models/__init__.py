from app.database.base import Base
from app.models.user import User
from app.models.link import Link  # укажи точное имя файла и класса твоей модели ссылок

# Это заставит Python прочитать файлы и зарегистрировать таблицы в метаданных Base
__all__ = ["Base", "User", "Link"]