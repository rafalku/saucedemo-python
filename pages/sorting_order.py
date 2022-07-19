from enum import Enum


class SortingOrder(Enum):
    NAME_ASC = "Name (A to Z)"
    NAME_DESC = "Name (Z to A)"
    PRICE_ASC = "Price (low to high)"
    PRICE_DESC = "Price (high to low)"
