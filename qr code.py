#qr code
import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/hunt-tech/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming
url.svg("mygithub.svg",  scale=8)