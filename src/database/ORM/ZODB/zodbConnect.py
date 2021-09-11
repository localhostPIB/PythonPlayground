import ZODB.FileStorage
import BTrees.OOBTree
import account

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

root.accounts = BTrees.OOBTree.BTree()
root.accounts['account-1'] = account.Account("Konto1")
print (root.items())
