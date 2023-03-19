import qrcode
from PIL import Image

link = 'python.png'
logo = Image.open(link) 

w = 150
size = (w/float(logo.size[0])) 
h = int((float(logo.size[1])*float(size))) 

logo = logo.resize((w,h), Image.LANCZOS) 
Qcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

url = 'http://www.vnrvjiet.ac.in/'
#Link for which QR Code is to be generated

Qcode.add_data(url) 
Qcode.make() 
QRcolor = 'Black'

image = Qcode.make_image(fill_color=QRcolor,back_color="white").convert('RGB') 

position = ((image.size[0]-logo.size[0])//2,(image.size[1]-logo.size[1])//2) 

image.paste(logo, position) 
image.save('logo.png') 

print('QR code generated using PIL') 
