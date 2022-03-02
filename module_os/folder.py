import os
def create_fold (foldername,inputprofile):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
        print ("Der Ordner    "+foldername +"    wurde erstellt")
        os.system("touch "+ foldername +"/profile.txt")
        os.system("echo "+ inputprofile +" >> "+ foldername +"/profile.txt") 
        return True
    else: 
        print("Der Ordner " +foldername+ " existiert bereits!")
        print("Bitte versuche es erneut")
        return False
        
