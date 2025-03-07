# Make pngs of all plots

import fnmatch
import os

def run(forcererun=False):
    files = []
    for root, dirnames, filenames in os.walk("./"):
        for filename in fnmatch.filter(filenames, '*.pdf'):
            files.append(os.path.join(root, filename))
    for i, file in enumerate(files):
        infile = file[2:] # remove "./"
        outfile = infile.replace(".pdf",".png")
        outfile = "png/"+outfile
        syscall = "convert -density 200 "+infile+" "+outfile
        if "/" in infile:
            path = "png/"+infile[:infile.rfind("/")]
            try:
                os.makedirs(path)
            except:
                pass
        print str(i+1)+"/"+str(len(files))+": "+syscall
        if not os.path.exists(outfile) or forcererun:
            if not "oldvis" in infile:
                os.system(syscall)

if __name__=="__main__":
    run(forcererun=False)
