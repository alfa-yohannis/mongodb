from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Mengubah harga
hasil_harga = produk.update_one(
    {"nama": "Laptop Pro X"},
    {"$set": {"harga": 17_900_000}}
)

print("Hasil update harga:")
print(" matched_count :", hasil_harga.matched_count)
print(" modified_count:", hasil_harga.modified_count)
print(" upserted_id   :", hasil_harga.upserted_id)

# Menambah stok
hasil_stok = produk.update_one(
    {"nama": "Laptop Pro X"},
    {"$inc": {"stok": 5}}
)

print("\nHasil update stok:")
print(" matched_count :", hasil_stok.matched_count)
print(" modified_count:", hasil_stok.modified_count)
print(" upserted_id   :", hasil_stok.upserted_id)
