import glob
import os.path

path = r"C:\Users\Shireesha\handson\DAY2"
folder = glob.glob(path+r"\*")
data = r"C:\Users\Shireesha\handson\DAY2\data.txt"

def finalFile(folder,data):
    for file in folder:
        if os.path.isfile(file):
            if file .endswith(".txt"):
                with open(file,"rt") as f:
                    lines = f.readlines()
                with open(data,"at") as ft:
                    ft.write("\n-------***-------file start--------***--------\n")
                    ft.write("Data from file "+file+"\n")
                    ft.writelines(lines)
                    ft.write("\n-------***-------file end--------***--------\n")
        else :
            sub = glob.glob(os.path.join(file, "*"))
            finalFile(sub , data)
            
finalFile(folder,data)