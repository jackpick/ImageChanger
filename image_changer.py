from PIL import Image

old_image_name = input("Enter the name of the image that you want to change: ")
new_image_name = input("Enter the output file name (Default = output.format: ") or "output.{old_image_name.rsplit('.', 1)[-1]}"

image = Image.open(old_image_name) ## Insert any picture name here (would recommend Keith Haring though, since they are so simplistic. Can be many different formats ##
pixel = image.load() # load pic so it can be scanned
size = image.size # Get the width and hight of the image for iterating over

##find the individual X and Y sizes so they can be iterated over
size_x = int(size[0])
size_y = int(size[1])

not_first_pixel = False # creates a variable that can be checked, to see if the program is editing the first pixel or not - removes potential logic errors concerning the first pixel
for x in range (0, size_x): #loops through all the columns
    for y in range (0, size_y): #loops through all the rows
        if not_first_pixel: #do this if this isn't the first pixel
            current_pixel_value = pixel[x, y]  # Get the RGBA Value of the pixel
            bound = 50 # Make this higher if you want there to be a higher contrast in colour required for the program to change the RGB colour
            if (old_previous_pixel_value[0] - bound < current_pixel_value[0] < old_previous_pixel_value[0] + bound) and (old_previous_pixel_value[1] - bound < current_pixel_value[1] < old_previous_pixel_value[1] + bound) and (old_previous_pixel_value[2] - bound < current_pixel_value[2] < old_previous_pixel_value[2] + bound): #if this pixel is basically the same colour as the last pixel
                old_previous_pixel_value = pixel[x,y]  #remember what colour this pixel is for the next pixel
                pixel[x,y] = new_previous_pixel_value # change this pixels colour to the same as to what the prvious pixel now is since they were already pretty much the same colour
            else:
                old_previous_pixel_value = pixel[x,y]  #remember what colour this pixel is for the next pixel
                colour_counter += 1 # change the colour
                if colour_counter % 3 == 0: # if colour counter is a multiple of 3
                    pixel[x,y] = (0, 255, 0) # make pixel green
                    new_previous_pixel_value = (0, 255, 0)  #remember what colour this pixel now is for the next pixel
                elif colour_counter % 2 == 0: # if colour counter is a multiple of 2
                    pixel[x,y] = (0, 0, 255) # make pixel blue
                    new_previous_pixel_value = (0, 0, 255)  #remember what colour this pixel now is for the next pixel
                else: # if colour counter is a multiple of 1
                    pixel[x,y] = (255, 0, 0) # make pixel red
                    new_previous_pixel_value = (255, 0, 0)  #remember what colour this pixel now is for the next pixel                
        else: #do this if this is the first pixel
            old_previous_pixel_value = pixel[0,0]  #remember what colour this pixel is
            pixel[0,0] = (255, 0, 0) #changes the pixel colour to red
            new_previous_pixel_value = (255, 0, 0) #remember what colour it is now
            colour_counter = 1 #start the colour counter, this will be counting through, each time the colour is changed in order to make sure a different colour is chosen every time - according to what the counter can be divided by
            not_first_pixel = True #the first pixel has now finished being processed so the next pixel will not be the first pixel

#pixel[x,y] = value  # Set the RGBA Value of the image (tuple)
image.save(new_image_name)  # Save the modified pixels as .png
