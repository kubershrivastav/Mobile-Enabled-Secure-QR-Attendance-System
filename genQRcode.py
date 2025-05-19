import qrcode # generate qr code
import datetime  # yeh date & time will fetch from laptop
import time     #specific time ke baad run karne ke liye use hoga


class GenerateQR:
    def QRcodeFunc(self):
        for i in range(120000): #itne baar change hoga qr code
            #N = 10
            res = '/camera ' + str(datetime.datetime.now())
            print(res)
            img = qrcode.make(res) 
            img.save("C:/Users/singh/OneDrive/Documents/Mobile_Integrated Attandence system/Face-REcog/mongodb-user-login/static/img/myqrcode.png")
            time.sleep(15)

def main():
    genQR = GenerateQR()
    genQR.QRcodeFunc()

if __name__ == "__main__":
    main()