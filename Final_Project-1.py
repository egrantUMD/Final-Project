#!/usr/bin/python37all
import PIL
from PIL import Image
import cgi
import cgitb
import cv2


cgitb.enable()

data = cgi.FieldStorage() #holds values form HTML

a = data.getvalue("one") #input values from html
b = data.getvalue("two")
c = data.getvalue("three")
d = data.getvalue("four")
e = data.getvalue("five")
f = data.getvalue("six")
g = data.getvalue("seven")
h = data.getvalue("eight")
i = data.getvalue("nine")
j = data.getvalue("ten")
k = data.getvalue("eleven")

list = [a,b,c,d,e,f,g,h,i,j,k]

for num in range(10):
  list[num] = str(list[num])

photo = data["photos"].file

cv2.imwrite('tester.jpg', photo)
photo = Image.open("tester.jpg")
photo = photo.save('tester.jpg')



new_width = 1

# ascii characters used to build the output text
ASCII_CHARS = list

# resize image according to a new width
def resize_image(image):
    global new_width
    width, height = image.size
    ratioImage = width/height
    ratioPaper = 1.23015873016

    if ratioImage > ratioPaper:
        new_height = int(48 * ratioPaper / ratioImage)
        new_width= 116-1
    else:
        new_height = 48
        new_width = int(ratioImage / ratioPaper * 116) -1
    
    
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main():
    # attempt to open image from user-input
    #path = /lib/cgi-bin
    try:
        image = Image.open("tester.jpg")
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()

print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<div style="background:#FFFFFF;border:1px;text-align:center"> <br>')
print('Type Writer Site')
print('</head>')
print('<body>')
print('<form action="/cgi-bin/Final_Project-1.py" method="POST">')
print('<div style="background:#FFFFFF;border:1px;text-align:center"> <br>')
print('Please input all characters necessary for art <br>(Reapeats Allowed)<br>')
print('<input type="text" name="one"> <br>')
pront('<input type="text" name="two"><br>')
print('<input type="text" name="three"><br>')
print('<input type="text" name="four"><br>')
print('<input type="text" name="five"> <br>') 
print('<input type="text" name="six"><br>')
print('<input type="text" name="seven"> <br>')
print('<input type="text" name="eight"> <br>')
print('<input type="text" name="nine"> <br>') 
print('<input type="text" name="ten"><br>') 
print('<input type="text" name="eleven"> <br>')
print('<br>')
print('Uploa File: <br> <br>')
print('<input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg"> <br>')
print('<br> <input type="submit" value="Submit">')
print('<br>')
print('<p> <iframe src="ascii_image.txt" frameborder="0"></iframe> </p>')
print('<br>')
print('</body>')
print('</html>')