# Crop image

# Left corner- width:+125, height: +133, 
# Spacing: 8 per row, 2 per column

from PIL import Image

def crop_image(input_image_path, crop_width, crop_height, left_margin, top_margin, hor_spacing, ver_spacing):
    img = Image.open(input_image_path)
    img_width, img_height = img.size

    left = left_margin
    top = top_margin
    hor_counter = 1
    ver_counter = 1

    # Loop over the large image and crop smaller images
    for ver_counter in range(1, 3):
    	for hor_counter in range(1,4):
	        # Define the box to crop
	        right = left + crop_width
	        bottom = top + crop_height

	        # Crop the image
	        cropped_img = img.crop((left, top, right, bottom))

	        # Save the cropped image
	        cropped_img.save(f"{input_image_path}_{hor_counter}_{ver_counter}.png")
	        left = right + hor_spacing
	        hor_counter += 1

	    # Restart for the second row
    	top = bottom + ver_spacing
    	left = left_margin 
    	ver_counter += 1

crop_image("Ganyuan3.jpg", 244, 490, 115, 133, 15, 26)  
#						  pic_size   margins   spacing