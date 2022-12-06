import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\AppData\Local\Tesseract-OCR\tesseract'


def read_images(images):

    for i in images:
        img = cv2.imread(i)
        print(type(img))
        print(img.shape)
        dim = (1000, 600)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(blackAndWhiteImage)
        print(f"Tekscior = {text}")
        cv2.imshow('Pokaz slajdow', blackAndWhiteImage)
        cv2.waitKey(0)


if __name__ == '__main__':

    images = ['images/test.jpg', 'images/usa.jpg', 'images/usa2.jpg', 'images/wurst.jpg', 'images/messi.jpeg', 'images/nowy_meksyk.jpg', 'images/mtg.jpg']
    read_images(images)














