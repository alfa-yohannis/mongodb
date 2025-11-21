from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Seluruh dokumen
for p in produk.find():
    print(p)

# Dokumen kategori Elektronik
for p in produk.find({"kategori": "Elektronik"}):
    print(p)

# Harga > 1.000.000
for p in produk.find({"harga": {"$gt": 1_000_000}}):
    print(p)