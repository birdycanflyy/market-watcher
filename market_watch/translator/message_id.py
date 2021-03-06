import enum


class MessageID(enum.Enum):
    HELLO = 0
    ERROR = 1
    INVALID_PRODUCT_LIST_FORMAT = 2
    INVALID_PRODUCT_PLATFORMS = 3
    PRODUCT_SUBSCRIBED = 4
    PRODUCT_NOTIFY_HEADER = 5
    PRODUCT_NOTIFY_UPDATED = 6
    PRODUCT_NOTIFY_NOT_FOUND = 7
    PRODUCT_NOTIFY_FOOTER = 8
    PRODUCT_LIST_HEADER = 9
    PRODUCT_LIST_ITEM = 10
    INTEGER = 11
    BUTTON_FIRST = 12
    BUTTON_LAST = 13
    BUTTON_REMOVE = 14
    NOT_SUBSCRIBED = 15
    UNSUBSCRIBED = 16
    PRODUCT_LIST_EMPTY = 17
    INTEGER_WITH_BRACKETS = 18
