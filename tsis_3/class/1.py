class String:
    user_string = None
    def __init__(self):
        pass

    def getString(self):
        self.user_string= input()

    def printString(self):
        print(self.user_string.upper())
    
string = String()
string.getString()
string.printString()