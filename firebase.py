
import collections
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

# Fetch the service account key JSON file contents
cred = credentials.Certificate('livesshopdatabase-firebase-adminsdk-lw4q3-0c796ee8dd.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://LivesShopDatabase.firebaseio.com"
})

db = firestore.client()

LiveShops =db.collection("LiveShop").stream()
print(LiveShops)
for LiveShop in LiveShops:
    print("{}".format(LiveShop.to_dict()))


