# Langkah 5: Ambil kembali pesan dari gambar
from kdi import decode_lsb


hasil = decode_lsb("gambar_teman/gambar_tersisip.png")
print("Pesan tersembunyi:", hasil)