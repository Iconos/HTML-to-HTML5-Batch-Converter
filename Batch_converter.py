__author__ = 'Iconos'
import os;
path = os.getcwd()



def OpenPage(file):
    newFile = open("updated_"+file,"w")
    try:
        openFile = open(file,"r+")
    except:
        print "unable to open" + file
    # break into lines and remove leading and trailing space on each
    for line in openFile:  
        if ".wav" in line: # replace <audio with old audio plugin tags
            print "Converting audio tags..."
            line = ReplaceWaveTags(line)
        if ".mp3" in line:
            print "Conveting old mp3 tags..."
            line = ReplaceMp3Tags(line)
        if ".pdf" in line: #This should return lines containing the pdf embeds
            print "Updating pdf tags..."
            line = ReplacePDFTags(line)
        newFile.write(line)
    print file + " converted."
    return newFile

    # Replaces the old audio embeds with HTML 5 tags
def ReplaceWaveTags(string):
    #split line by " and keep *.wav as string var.
    print string
    (waveString) = string.split('"',2) #pulling from file name instead of lines from file...
    print "wav file is: " + waveString[1]
    (audio) = waveString[1].split('.')
    mp3String = audio[0] + ".mp3"
    startString = "    <td><audio controls autoplay> <source src="+'"'
    endString =  '"'+"type="+'"'+"audio/mpeg"+'"'+"></audio></td>"
    string = startString+mp3String+endString+"\n"
    print string
    return(string)
    
def ReplaceMp3Tags(string):
    #split line by " and keep *.mp3 as string var.
    print string
    (mp3String) = string.split('"',2) #pulling from file name instead of lines from file...
    print "mp3 file is: " + mp3String[1]
    startString = "<td><audio controls autoplay> <source src="+'"'
    endString =  '"'+"type="+'"'+"audio/mpeg"+'"'+"></audio></td>"
    string = startString+mp3String[1]+endString+"\n"
    print string
    return(string)

    # Replaces the old pdf embeds with new html5 versions
def ReplacePDFTags(string):
    print string
    (pdfString) = string.split('"',2)
    print "pdf file is: " + pdfString[1]
    startString1 = "<object data="+'"'
    endString1 =  '"'+"type="+'"'+"application/pdf"+'"'+" width="+'"'+"100%"+'"'+" height="+'"'+"100%"+'"'+">"
    startString2 = "Browser cannot handle pdf files: <a href="+'"'
    endString2 = '"'+">Click_here_to_open_the_pdf.htm</a></object>"
    string = startString1+pdfString[1]+endString1+"\n"+startString2+pdfString[1]+endString2+"\n"
    print string
    return(string)


for dirpath, dirnames, filenames in os.walk(path):
    procFileCount = 0
    skipFileCount = 0
    print path
    for filename in filenames:
        if filename.endswith('.htm'):
            print "Updating " + filename
            OpenPage(filename)
            procFileCount+=1
        else:
            print "Skipping " + filename
            skipFileCount +=1
    print "Conversion Complete \nFiles Processed: "+ str(procFileCount)+"\nFilesSkipped: "+ str(skipFileCount)
