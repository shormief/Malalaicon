from PIL import Image
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("Malala.jpg")

new_pixel_values = []

pixel_values = list(im.getdata())
for elem in pixel_values:
	total_pixel_values = elem[0] + elem[1] + elem[2]
	if total_pixel_values < 182:
		new_pixel_values.append(darkBlue)
	elif total_pixel_values > 182 and total_pixel_values < 364:
		new_pixel_values.append(red)
	elif total_pixel_values > 364 and total_pixel_values < 546:
		new_pixel_values.append(lightBlue)
	else:
		new_pixel_values.append(yellow)


new_image = Image.new(im.mode, im.size)	
new_image.putdata(new_pixel_values)	
new_image.show()

#define a variable = "the intensity" of each pixels 
#Conditionals 
#Lists
#don't forget to add the color values 
