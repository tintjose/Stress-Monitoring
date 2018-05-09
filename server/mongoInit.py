
from pymongo import MongoClient


if __name__ == '__main__':

    client = MongoClient('localhost', 27017)

    db = client.savoring

    db.role.update({'name': 'admin'}, {'name': 'admin'}, upsert=True)
    superId = db.role.find_one({'name': 'admin'})['_id']
    db.role.update({'name': 'user'}, {'name': 'user'}, upsert=True)
    userId = db.role.find_one({'name': 'user'})['_id']

    db.user.update({'email': 'admin'}, {'email': 'admin', \
            'roles': [superId, userId], 'password':'MyBigSuperAdmin'},\
            upsert=True)
