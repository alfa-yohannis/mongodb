from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Memberikan diskon 10% untuk kategori Elektronik
hasil_diskon = produk.update_many(
    {"kategori": "Elektronik"},
    {"$mul": {"harga": 0.90}}
)

print("Hasil update diskon (Elektronik):")
print(" matched_count :", hasil_diskon.matched_count)
print(" modified_count:", hasil_diskon.modified_count)
print(" upserted_id   :", hasil_diskon.upserted_id)

# Menambah field promo pada kategori Aksesoris
hasil_promo = produk.update_many(
    {"kategori": "Aksesoris"},
    {"$set": {"promo": True}}
)

print("\nHasil update promo (Aksesoris):")
print(" matched_count :", hasil_promo.matched_count)
print(" modified_count:", hasil_promo.modified_count)
print(" upserted_id   :", hasil_promo.upserted_id)
