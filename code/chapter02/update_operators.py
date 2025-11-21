from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

def print_hasil(header, hasil):
    print("#", header)
    print("  matched_count :", hasil.matched_count)
    print("  modified_count:", hasil.modified_count)
    print("  upserted_id   :", hasil.upserted_id)

# $set
hasil = produk.update_one(
    {"nama": "Mouse Wireless"},
    {"$set": {"harga": 275000, "warna": "Hitam"}}
)
print_hasil("$set", hasil)

# $addToSet
hasil = produk.update_one(
    {"nama": "Headset Gaming"},
    {"$addToSet": {"tag": "gaming"}}
)
print_hasil("$addToSet", hasil)

# $unset
hasil = produk.update_one(
    {"nama": "Webcam HD"},
    {"$unset": {"promo": ""}}
)
print_hasil("$unset", hasil)

# $mul
hasil = produk.update_one(
    {"nama": "Monitor 27 inch"},
    {"$mul": {"harga": 0.95}}
)
print_hasil("$mul", hasil)
