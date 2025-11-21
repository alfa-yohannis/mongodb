from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Halaman pertama: 5 dokumen
page1 = produk.find().limit(5)
for p in page1:
    print(p)

# Halaman kedua: skip 5, ambil 5
page2 = produk.find().skip(5).limit(5)
for p in page2:
    print(p)

# Pagination dengan sorting
page_sorted = produk.find().sort("harga", 1).skip(2).limit(2)
for p in page_sorted:
    print(p)

