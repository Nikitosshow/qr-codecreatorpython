import qrcode
from PIL import Image
import uuid
import time

# Ввод данных
data = input("Введите текст или URL: ")

# Создание QR-кода
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Отображение QR-кода в консоли
matrix = qr.get_matrix()
for y in range(len(matrix)):
    row = ""
    for x in range(len(matrix)):
        if matrix[x][y]:
            row += "  "
        else:
            row += "██" 
    print(row)

# Сохранение QR-кода в файле
filename = str(uuid.uuid4())
qr.make_image(fill_color="black", back_color="white").save(f"{filename}.png")

# Вывод сообщения об успешном создании файла
print(f"\nQR-код сохранен в файле: {filename}.png")
time.sleep(60)
