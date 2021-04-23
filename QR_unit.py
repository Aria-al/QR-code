import qrcode
from PIL import Image
import cv2 as cv 

class QR_treatment:
    def create (adresse):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(adresse)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img.save("%s.png" % (adresse))

    def read (qrcode) :
        im = cv.imread(qrcode)
        det = cv.QRCodeDetector()
        retval, points, straight_qrcode = det.detectAndDecode(im)
        #print (retval,points,straight_qrcode)
        return retval
    

    def MK5 ():
        # initalize the cam
        cap = cv2.VideoCapture(0)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            # check if there is a QRCode in the image
            if bbox is not None:
                # display the image with lines
                for i in range(len(bbox)):
                    # draw all lines
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                if data:
                    print("[+] QR Code detected, data:", data)
            # display the result
            cv2.imshow("img", img)    
            if cv2.waitKey(1) == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

"""
QR_treatment.create(401)
QR_treatment.read()
"""
