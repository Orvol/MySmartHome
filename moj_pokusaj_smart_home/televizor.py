class TVAparat:
    def __init__(self, ukljucen=False):  
        self.ukljucen = ukljucen
        

def ugasi_tv(self):         
        if self.ukljucen == False:
            print("TV je već ugašen")
        else:
            self.ukljucen = False
            print("TV uspješno ugašen.")



