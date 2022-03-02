import os
def create_fold (foldername,inputprofile):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
        print ("Der Ordner    "+foldername +"    wurde erstellt")
        os.system("touch "+ foldername +"/profile.txt")
        os.system("echo "+ inputprofile +" >> "+ foldername +"/profile.txt") 
    else:
        success = False 
        while success == False:
            print("Der Ordner " +foldername+ " existiert bereits!")
            foldername = input("Gebe einen persönlichen Ordnernamen an: ")
            if not os.path.exists(foldername):
                os.mkdir(foldername)
                print ("Der Ordner    "+foldername +"    wurde erstellt")
                os.system("touch "+ foldername +"/profile.txt")
                os.system("echo "+ inputprofile +" >> "+ foldername +"/profile.txt")
                success=True 