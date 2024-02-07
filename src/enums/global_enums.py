from enum import Enum


class UrlEnum(Enum):
    """
    Класс, в котором содержатся данные о протоколах, IP и доменах продукта
    """

    PROTOCOL: str = 'https:/'
    HOST_PROD: str = '/demo.opencart-cms.ru/'
    HOST_TEST: str = 'stub'
    HOST_PREVIEW: str = 'stub'
    HOST_DEV: str = 'stub'


class TimeoutEnum(Enum):
    """
    Класс, в котором содержится список необходимых тайм-аутов
    """

    HALF_SEC: float = 0.5
    ONE_SEC: float = 1.0
    ONE_AND_HALS_SEC: float = 1.5
    TWO_SEC: float = 2.0
    FIVE_SEC: float = 5.0
    TEN_SEC: float = 10.0
    FIFTY_SEC: float = 10.0
