import os
def create_fold (foldername,inputprofile):
    os.mkdir(foldername)
    os.system("touch "+ foldername +"/profile.txt")
    os.system("echo "+ inputprofile +" >> "+ foldername +"/profile.txt") 