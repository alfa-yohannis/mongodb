from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Urutkan berdasarkan harga ascending
for p in produk.find().sort("harga", ASCENDING):
    print(p)

# Urutkan berdasarkan stok descending
for p in produk.find().sort("stok", DESCENDING):
    print(p)

