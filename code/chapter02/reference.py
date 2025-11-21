from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]

# Ambil order berdasarkan _id
order = db.orders.find_one({
    "_id": ObjectId("67ac467e1a993001ba04f102")
})

# Ambil customer berdasarkan customer_id
customer = db.customers.find_one({
    "_id": order["customer_id"]
})

print("Order :", order)
print("Customer :", customer)