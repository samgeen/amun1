'''
Copy all the figures into a final folder
Sam Geen, July 2015
'''

import os, string

letters = list(string.ascii_lowercase)

def makedir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def run(infile,ancils,nobib):
    makedir("final")
    makedir("final/plots")
    outfile = "final/"+infile
    lines = open(infile,"r").readlines()
    out = open(outfile,"w")
    figfile = open("figurelist.txt","w")
    infigure = False
    fig = 0
    plots = 0
    for line in lines:
        # In figure?
        if ("begin{figure}" in line or \
           "begin{figure*}" in line) and not "%" in line:
            plots = 0
            infigure = True
            fig += 1
            print "Figure",fig,"being processed..."
        if ("end{figure}" in line or \
           "end{figure*}" in line) and not "%" in line:
            infigure = False
            print "Figure",fig,"done!"
        # Look for plots
        tmp = line+""
        while infigure:
            # Find plot name iteratively in line
            pos = tmp.find("\includegraphics")
            if pos == -1:
                break
            tmp = tmp[pos:]
            tmp = tmp[tmp.find("{")+1:]
            epsfile = tmp[:tmp.find("}")]
            tmp = tmp[len(epsfile):]
            # Make a new plot name
            letter = letters[plots]
            plots += 1
            neweps = "plots/fig"+str(fig)+letter+".pdf"
            # Copy file
            print epsfile,"-->",neweps
            os.system("cp "+epsfile+" final/"+neweps)
            # Replace line text
            line = line.replace(epsfile,neweps)
            # Write to log of figure names
            figfile.write(epsfile)
            # Check for fits file containing point/image data and copy that too
            fitsfile = epsfile.replace(".pdf",".fits")
            if os.path.exists(fitsfile):
                newfits = neweps.replace(".pdf",".fits")
                os.system("cp "+fitsfile+" final/"+newfits)
                figfile.write(" (with .fits archive file)")
            figfile.write("\n")
        # Write line
        out.write(line)
    # End of lines
    # Close file
    out.close()
    figfile.close()
    # Copy ancilliary files
    for an in ancils:
        if not nobib or not ".bib" in an:
            os.system("cp "+an+" final/"+an)
    # Zip final
    os.system("zip -r final.zip final") 
    print "DONE!"

if __name__=="__main__":
    nobib=True
    run("amunpaper.tex",ancils=["samgeen.bib","amunpaper.bbl","mnras.cls","mnras.bst"],nobib=nobib)
