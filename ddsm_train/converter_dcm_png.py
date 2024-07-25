import subprocess
import os

if __name__ == '__main__':
    in_dir = "/home/ulisses/INbreast/AllDICOMs"
    out_dir = "/home/ulisses/INbreast/AllIMG"
    
    for file in os.listdir(in_dir):
        name = file.split(".")
        if(name[1] == "dcm"):
            name = name[0].split("_")
            subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', in_dir + '/' + file, out_dir + '/' + name[0] + '.png'])
            print(name)

        
    