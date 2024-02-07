import os
from enum import Enum



class UserEnum(Enum):
    """
    Класс, в котором хранятся данные пользователей
    """

    LOGIN = os.environ.get('LOGIN')
    PASSWORD = os.environ.get('PASSWORD')

