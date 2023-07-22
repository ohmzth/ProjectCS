
import collections
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

from datetime import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate('D:/seneir/testproject-9c07d-firebase-adminsdk-x56u8-201f05d790.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://testproject.firebaseio.com"
})

db = firestore.client()


#write

# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

LiveShops =db.collection("live_shop")
LiveShops.document("04").set({
        'Id':"A22",
        'Picture':"ff.img",
        'Price':"50 ",
        'ProductName':"kanom",
        'ShopName':"firstshop",
        'Time':dt_string ,
})

#read
LiveShops =db.collection("live_shop").stream()
print(LiveShops)
for LiveShop in LiveShops:
    print("{}".format(LiveShop.to_dict()))


