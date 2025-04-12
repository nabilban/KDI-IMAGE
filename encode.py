# Langkah 4: Sisipkan pesan
from kdi import encode_lsb


pesan_rahasia = "INI PESAN TEMPE BANGET, GAK ADA YANG TAHU"
encode_lsb("input/gambar_awal.png", pesan_rahasia, "output/gambar_tersisip.png")