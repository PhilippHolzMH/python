import os
def create_fold (foldername,inputprofile):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
        os.system("touch "+ foldername +"/profile.txt")
        os.system("echo "+ inputprofile +" >> "+ foldername +"/profile.txt") 
        return True
    else: 
        return False
        
