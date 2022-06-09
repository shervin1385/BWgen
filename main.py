from datetime import datetime
import random
from pyautogui import  press
# import keyboard
import time
class generator:
    def __init__ (self):
        print(f'program started \t {datetime.now()}')
        self.afrad = self.reader('afrad.txt')
        self.alghab = self.reader('alghab.txt')
        self.afal = self.reader('afal.txt')
        self.ashya = self.reader('ashya.txt')

        # select target
        targets = ["تو","شما","او","آنها"]
        for ind , c in enumerate(targets):
            print(f"[{ind}] - {c}")
        self.target = targets[int(input("target : "))]
        print(f"target : {self.target}")
        
        nor = int(input("number of runs : "))
        time.sleep(3)
        for i in range(nor):
            self.asleep()
            word = self.mixer()
            print(word)
            word = self.translater(word)
            for c in word:
                press(c)
            press("enter")

        print(f'program ended \t {datetime.now()}')
    def translater(self,word):
        linux_persian_layout_dict = {
             "ض" : "q" ,
             "ص" : "w" ,
             "ث" : "e" ,
             "ق" : "r" ,
             "ف" : "t" ,
             "غ" : "y" ,
             "ع" : "u" ,
             "ه" : "i" ,
             "خ" : "o" ,
             "ح" : "p" ,
             "ج" : "[" ,
             "چ" : "]" ,
             "ش" : "a" ,
             "س" : "s" ,
             "ی" : "d" ,
             "ب" : "f" ,
             "ل" : "g" ,
             "ا" : "h" ,
             "ت" : "j" ,
             "ن" : "k" ,
             "م" : "l" ,
             "ک" : ";" ,
             "گ" : "'" ,
             "ظ" : "z" ,
             "ط" : "x" ,
             "ز" : "c" ,
             "ر" : "v" ,
             "ذ" : "b" ,
             "د" : "n" ,
             "پ" : "m" ,
             "و" : "," ,
        }
        for c in word:
            if c in linux_persian_layout_dict:
                word = word.replace(c,linux_persian_layout_dict[c])
        return word
    def asleep(self):
        amount =  random.randint(30,130)/100.0
        print(f"sleeping for {amount} seconds")
        time.sleep(amount)
    def mixer(self):
        laghab = random.choice(self.alghab)
        fard = random.choice(self.afrad)
        shey = random.choice(self.ashya)
        fel = random.choice(self.afal)
        if self.target == "تو":
            zamir = "ت"
        elif self.target == "شما":
            zamir = "تون"
        elif self.target == "او":
            zamir = "ش"
        elif self.target == "آنها":
            zamir = "شون"
        else:
            return 1
        def corrector(word):
            if word.strip() == "جند":
                return f"جنده"
            else :
                return word
        types = [
            f"{shey}م تو {fard} {laghab}{zamir}",
            f"{fard}{zamir} رو {fel}م",
            f"{fard}{zamir} {corrector(laghab)} است"
        ]
        result = random.choice(types).replace("\n", '')
        return result

    def reader(self,filename):
        file = []
        with open(filename , "r") as f:
            for word in f.readlines() :
                file.append(word)
        return file
if __name__ == "__main__":
    g = generator()
    