import ZODB.FileStorage.FileStorage
import ZODB.DB
import transaction


def save(user):
    connection = ZODB.connection(None)
    connection.add(user)
