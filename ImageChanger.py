from PIL import Image

im = Image.open("Keith Haring 3.jpg") ## Insert any picture name here (would recommend Keith Haring though, since they are so simplistic. Can be many different formats ##
pix = im.load() # load pic so it can be scanned
Size = im.size # Get the width and hight of the image for iterating over

##find the individual X and Y sizes so they can be iterated over
XSize = int(Size[0])
YSize = int(Size[1])

NotFirstPixel = 0 # creates a variable that can be checked, to see if the program is editing the first pixel or not - removes potential logic errors concerning the first pixel
for x in range (0, XSize): #loops through all the columns
    for y in range (0, YSize): #loops through all the rows
        if NotFirstPixel == 1: #do this if this isn't the first pixel
            CurrentPixelValue = pix[x,y]  # Get the RGBA Value of the pixel
            Bound = 50 # Make this higher if you want there to be a higher contrast in colour required for the program to change the RGB colour
            if (OldPreviousPixelValue[0]-Bound < CurrentPixelValue[0] < OldPreviousPixelValue[0]+Bound) and (OldPreviousPixelValue[1]-Bound < CurrentPixelValue[1] < OldPreviousPixelValue[1]+Bound) and (OldPreviousPixelValue[2]-Bound < CurrentPixelValue[2] < OldPreviousPixelValue[2]+Bound): #if this pixel is basically the same colour as the last pixel
                OldPreviousPixelValue = pix[x,y]  #remember what colour this pixel is for the next pixel
                pix[x,y] = NewPreviousPixelValue # change this pixels colour to the same as to what the prvious pixel now is since they were already pretty much the same colour
            else:
                OldPreviousPixelValue = pix[x,y]  #remember what colour this pixel is for the next pixel
                ColourCounter = ColourCounter+1 # change the colour
                if ColourCounter % 3 == 0: # if colour counter is a multiple of 3
                    pix[x,y] = (0, 255, 0) # make pixel green
                    NewPreviousPixelValue = (0, 255, 0)  #remember what colour this pixel now is for the next pixel
                elif ColourCounter % 2 == 0: # if colour counter is a multiple of 2
                    pix[x,y] = (0, 0, 255) # make pixel blue
                    NewPreviousPixelValue = (0, 0, 255)  #remember what colour this pixel now is for the next pixel
                else: # if colour counter is a multiple of 1
                    pix[x,y] = (255, 0, 0) # make pixel red
                    NewPreviousPixelValue = (255, 0, 0)  #remember what colour this pixel now is for the next pixel                
        else: #do this if this is the first pixel
            OldPreviousPixelValue = pix[0,0]  #remember what colour this pixel is
            pix[0,0] = (255, 0, 0) #changes the pixel colour to red
            NewPreviousPixelValue = (255, 0, 0) #remember what colour it is now
            ColourCounter = 1 #start the colour counter, this will be counting through, each time the colour is changed in order to make sure a different colour is chosen every time - according to what the counter can be divided by
            NotFirstPixel = 1 #the first pixel has now finished being processed so the next pixel will not be the first pixel

#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
im.save('ModifiedImage.png')  # Save the modified pixels as .png
