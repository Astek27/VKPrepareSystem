from sqlalchemy import Enum


class CityEnum(Enum):
    MSK = "Москва"
    MO = "Московская область"

class CategoryEnum(Enum):
    OF = "офицеры"
    PSS = "ПСС"
    GP = "ГП"
    ATT = "АТТ"
