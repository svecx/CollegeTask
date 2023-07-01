import cv2
import pytesseract
import pyperclip

# load gambar
image = cv2.imread('Screenshot 2023-04-08 115752.jpg')

# konversi gambar ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# aplikasikan thresholding
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# terapkan teknik noise removal
gray = cv2.medianBlur(gray, 3)

# konversi gambar ke teks
text = pytesseract.image_to_string(gray)

# salin teks ke clipboard
pyperclip.copy(text)

# tampilkan teks di console
print(text)
