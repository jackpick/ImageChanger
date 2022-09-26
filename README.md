# ImageChanger
A program that cycles through all the pixels in an image, turning them to either red, green or blue - changing colour at the original colour boundaries.
It does this by looping through each column of pixels, assessing how close in colour each pixel is to the last pixel. If they are deemed to be similar in colour then they will be changed to the same colour as the last pixel now is, however if they are not - they will be changed to a different colour (eg. if the last pixel was made red, then this one will be green or blue). It completes this process for the entire image, making every pixel in the image red, green, or blue.
