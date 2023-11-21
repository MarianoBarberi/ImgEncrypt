# C:\Users\maria\Desktop\bobpat.jpg
# python imgenc.py

# try block to handle exception
try:
	# take path of image as a input
	path = input(r'Enter path of Image : ')

	# check if the file extension corresponds to an image format
	allowed_extensions = ('.jpg', '.jpeg', '.png')
	if not path.lower().endswith(allowed_extensions):
		raise ValueError("Invalid file format! Please provide a valid image file.")
	
	# taking encryption key as input
	key = input('Enter Key for encryption of Image : ')
	
	# print path of image file and encryption key that
	# we are using
	print('The path of file : ', path)
	print('Key for encryption : ', key)
	
	# open file for reading purpose
	fin = open(path, 'rb')
	
	# storing image data in variable "image"
	image = fin.read()
	fin.close()
	
	# converting image into byte array to 
	# perform encryption easily on numeric data
	image = bytearray(image)

	# si es str convierte cada caracter en su valor ascii y lo suma, luego lo divide por 256
	if isinstance(key, str):
		key = sum(ord(c) for c in key) % 256

	# performing XOR operation on each value of bytearray
	for index, values in enumerate(image):
		image[index] = values ^ key

	# opening file for writing purpose
	fin = open(path, 'wb')
	
	# writing encrypted data in image
	fin.write(image)
	fin.close()
	print('Encryption Done...')

	
except Exception as e:
    print('Error caught:', str(e))