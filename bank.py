

class BankUser():
   def __init__(self,hesab_nomresi,balans):
    self.hesab_nomresi=hesab_nomresi,
    self.balans=balans
   
   def __str__(self):
    return f"Hesab nomresi:{self.hesab_nomresi} \n balans:{self.balans}"

   
   def balansArtir(self,miqdar):
    print("balans artirlildi")
    self.balans+=miqdar
   
   
   def pulCixar(self,miqdar):
    if(miqdar>self.balans):
        print("hesabinizda yeterli balans yoxdur")
    else:
        print("islem basarili")
        self.balans-=miqdar
   
   
   def balansiGoster(self):
        print(f"Balansiniz:{self.balans}")

yeniuser=BankUser(2552323,5000)
print(yeniuser)
yeniuser.balansArtir(525)
print(yeniuser.balans)
yeniuser.pulCixar(5000)
print(yeniuser.balans)
yeniuser.pulCixar(1000)
yeniuser.balansiGoster()



class Kredi(BankUser):
    

    def __init__(self,hesab_nomresi,balans,movcudKredit=0):
        super().__init__(hesab_nomresi,balans)
        self.movcudKredit=movcudKredit
        
        
    
    def krediVer(self,verilecekMiqdar):
        self.movcudKredit+=verilecekMiqdar
        print(f"kredit verildi .Ayliq odenisiniz{verilecekMiqdar/12}")
        self.balans+=self.movcudKredit
    
    def odenisEt(self,odenisMiqdari):
        self.movcudKredit-=odenisMiqdari

    def qalanKredit(self):
        print(f"Qalan kreditiniz {self.movcudKredit}")

    

kredi=Kredi(222,22)
kredi.krediVer(1000)

print(kredi.movcudKredit)
print(kredi.balans)
kredi.odenisEt(100)
kredi.qalanKredit()


