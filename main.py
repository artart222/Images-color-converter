from PIL import Image


imLocation = input("Please enter image location: ")
inputIm = Image.open(imLocation)
extension = inputIm.format.lower()


width, height = inputIm.size


#this list will become a list of color of pixels in grayscale
list = []


print("Please wait.")
#iterate over pixel of input image.
for y in range(height):
    for x in range(width):
        r, g, b = inputIm.getpixel((x, y))
        #convert colors based on weighting method
        #for more detile go to this link at wikipedia: https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
        lValue = 0.2126 * r + 0.7152 * g + 0.0722 * b
        list.append(lValue)


outputIm = Image.new("L", inputIm.size)
outputIm.putdata(list)
outputIm.save("output." + extension)
