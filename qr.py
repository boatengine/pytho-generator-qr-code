import qrcode


qrlink = input("Enter Link : ");
qrname = input("Export name QRcode : ");
lastfile = ".jpg";

filesave = qrname+lastfile;
# print(filesave);

qrimg = qrcode.make(qrlink);
qrimg.save(filesave)        