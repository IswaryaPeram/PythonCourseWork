class Hotstar:
    def __nit__(self,name):
        print(f"welcome to the hotstar,{name}")
    def auth(self):
        print("you can login/register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see the history")
    def playcontroller(self):
        print("pause play resume")
    def ads(self):
        print("ads will be run")
    def quality(self):
        print("you have limited quality")
    def devices(self):
        print("single login")
    def access(self):
        print("limited access")
    def download(self):
        print("you can't download")

class premiumHotstar(Hotstar):
    def __nit__(self,name):
        print(f"welcome to the hotstar,{name}")
    def auth(self):
        print("you can login/register")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see the history")
    def playcontroller(self):
        print("pause play resume")
    def ads(self):
        print("ads will not run")
    def quality(self):
        print("you have high quality")
    def devices(self):
        print("multiple login")
    def access(self):
        print("unlimited access")
    def download(self):
        print("you can't download")
iswarya=Hotstar('iswarya')
iswarya.auth()
iswarya.dashboard()
iswarya.history()
iswarya.playcontroller()
iswarya.ads()
iswarya.devices()
iswarya.access()
iswarya.download()
iswarya.search()
lalitha=premiumHotstar('lalitha')
lalitha.auth()


