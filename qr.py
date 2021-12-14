import qrcode

class QRGenerator:


    def __init__(self):
        self.GenerateQRCode()


    def GenerateQRCode(self):

        self.inputText = input("Enter your text\n")
        self.imgName = input("Enter image file name\n")

        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        self.qr.add_data(f"{self.inputText}")

        self.qr.make(fit=True)
        
        self.img = self.qr.make_image(fill_color="black", back_color="white")

        self.img.save(f"{self.imgName}.png")


QRGenerator()