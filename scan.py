import cv2
import numpy as np

def detect_color(hue):
    if hue < 5 or hue >= 170:
        return "Merah"
    elif 5 <= hue < 10:
        return "Merah Tua"
    elif 10 <= hue < 15:
        return "Jingga"
    elif 15 <= hue < 25:
        return "Jingga Cerah"
    elif 25 <= hue < 35:
        return "Kuning"
    elif 35 <= hue < 45:
        return "Kuning Hijau"
    elif 45 <= hue < 60:
        return "Hijau"
    elif 60 <= hue < 75:
        return "Hijau Cerah"
    elif 75 <= hue < 85:
        return "Hijau Tua"
    elif 85 <= hue < 100:
        return "Biru"
    elif 100 <= hue < 120:
        return "Biru Cerah"
    elif 120 <= hue < 130:
        return "Biru Tua"
    elif 130 <= hue < 150:
        return "Ungu"
    elif 150 <= hue < 160:
        return "Ungu Muda"
    elif 160 <= hue < 170:
        return "Biru Muda"
    elif 170 <= hue < 180:
        return "Cyan"
    elif 180 <= hue < 210:
        return "Biru Cyan"
    elif 210 <= hue < 240:
        return "Magenta"
    elif 240 <= hue < 260:
        return "Magenta Muda"
    elif 260 <= hue < 290:
        return "Merah Muda"
    elif 290 <= hue < 300:
        return "Coklat"
    elif 300 <= hue < 320:
        return "Kuning Coklat"
    elif 320 <= hue < 340:
        return "Kuning Emas"
    elif 340 <= hue < 360:
        return "Merah Cerah"
    elif 360 <= hue < 375:
        return "Hijau Laut"
    elif 375 <= hue < 390:
        return "Hijau Mint"
    elif 390 <= hue < 405:
        return "Hijau Zaitun"
    elif 405 <= hue < 420:
        return "Biru Langit"
    elif 420 <= hue < 435:
        return "Ungu Anggur"
    elif 435 <= hue < 450:
        return "Cyan Muda"
    elif 450 <= hue < 465:
        return "Ungu Lavender"
    elif 465 <= hue < 480:
        return "Merah Ceri"
    elif 480 <= hue < 495:
        return "Merah Jambu"
    elif 495 <= hue < 510:
        return "Kuning Lemon"
    elif 510 <= hue < 525:
        return "Kuning Mentega"
    elif 525 <= hue < 540:
        return "Biru Raja"
    elif 540 <= hue < 555:
        return "Biru Steel"
    elif 555 <= hue < 570:
        return "Merah Salmon"
    elif 570 <= hue < 585:
        return "Hijau Tua Gelap"
    elif 585 <= hue < 600:
        return "Hijau Limau"
    elif 600 <= hue < 615:
        return "Merah Peria"
    elif 615 <= hue < 630:
        return "Merah Kecil"
    elif 630 <= hue < 645:
        return "Kuning Hangat"
    elif 645 <= hue < 660:
        return "Biru Langit Cerah"
    elif 660 <= hue < 675:
        return "Biru Malam"
    elif 675 <= hue < 690:
        return "Magenta Cerah"
    elif 690 <= hue < 705:
        return "Cyan Gelap"
    elif 705 <= hue < 720:
        return "Merah Coklat"
    elif 720 <= hue < 735:
        return "Merah Oranye"
    elif 735 <= hue < 750:
        return "Kuning Coklat"
    elif 750 <= hue < 765:
        return "Hijau Air"
    elif 765 <= hue < 780:
        return "Biru Hijau"
    elif 780 <= hue < 795:
        return "Ungu Tua"
    elif 795 <= hue < 810:
        return "Biru Cerulean"
    elif 810 <= hue < 825:
        return "Kuning Tua"
    elif 825 <= hue < 840:
        return "Hijau Kekuningan"
    elif 840 <= hue < 855:
        return "Ungu Pink"
    elif 855 <= hue < 870:
        return "Cyan Kecil"
    elif 870 <= hue < 885:
        return "Magenta Tua"
    elif 885 <= hue < 900:
        return "Biru Tua Kecil"
    elif 900 <= hue < 915:
        return "Merah Timah"
    elif 915 <= hue < 930:
        return "Merah Tanah"
    elif 930 <= hue < 945:
        return "Coklat Kecil"
    elif 945 <= hue < 960:
        return "Kuning Hijau Kecil"
    elif 960 <= hue < 975:
        return "Biru Pastel"
    elif 975 <= hue < 990:
        return "Hijau Pastel"
    elif 990 <= hue < 1005:
        return "Kuning Pastel"
    elif 1005 <= hue < 1020:
        return "Ungu Pastel"
    elif 1020 <= hue < 1035:
        return "Merah Pastel"
    else:
        return "Tidak Dikenal"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv], [0], None, [360], [0, 360])
    hue_value = np.argmax(hist)

    color_name = detect_color(hue_value)

    cv2.putText(frame, f'Warna: {color_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Alat Deteksi Warna Anjay Mabar', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
