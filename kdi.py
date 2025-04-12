
# =================================
# Steganografi Sederhana dengan LSB
# =================================

from PIL import Image

# Langkah 1: Buka gambar lokal
img = Image.open("input/gambar_test_nabil.jpg")
img.save("input/gambar_awal.png")

# Langkah 2: Fungsi untuk encode
def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    binary_message = ''.join([format(ord(char), '08b') for char in message]) + '1111111111111110'
    encoded = img.copy()
    pixels = encoded.load()

    idx = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if idx < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                encoded.save(output_path)
                return
    encoded.save(output_path)

# Langkah 3: Fungsi untuk decode
def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ''
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)

    bytes_list = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    for byte in bytes_list:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))
    return message