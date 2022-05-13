from hashlib import sha256
import time


class block:
    def __init__(self,timeStamp,data,previousHash=''): #genesis bloğunda önceki bloğun adresi olmadığından default boş gönderilir.
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.kuvvet = 1 #Blockchain'in bir kurala ihtiyacı olduğu için bu kuralı oluşturabilecek bir kuvvete ihtiyacımız var.
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet = self.kuvvet+1
            ozet = sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
            return ozet

class blockchain:
    def __init__(self):
        self.chain=[self.genesisOluştur()]

    def genesisOluştur(self):
        return block(time.ctime,"Asilturk","")

    def blockEkle(self,data):
        node = block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk = self.chain[i-1].hash
                suan = self.chain[i].previousHash
                if ilk!=suan:
                    return "Zincir Kopmuş"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash:
                    return "Zincir Kopmuş"
            return "Sağlam"

    def listeleme(self):
        print("BlockChain = \n")
        for i in range(len(self.chain)):
            print("Block => ",i,"\nHash = ",str(self.chain[i].hash),"\nZaman Damgası = ",str(self.chain[i].timeStamp),"\nData = ",str(self.chain[i].data),"\nKuvvet = ",str(self.chain[i].kuvvet),"\nPreviousHash = ",str(self.chain[i].previousHash))

AsilChain = blockchain()

while True:
    print("\n Lütfen Seçiminizi yapın \n 1-Block Ekle \n 2-Blockchain'in yapısını gör \n 3-Zinciri kontrol et \n 4-çıkış yap \n")
    data = input()
    if data == "1":
        print("*******************************************")
        print("Gönderilen miktarı giriniz")
        miktar = input()
        AsilChain.blockEkle(miktar)
        print("*******************************************")
    elif data == "2":
        print("*******************************************")
        AsilChain.listeleme()
        print("*******************************************")
    elif data == "3":
        print("*******************************************")
        print(str(AsilChain.kontrol()))
        print("*******************************************")
    elif data == "4":
        break
                