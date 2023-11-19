from PIL import Image

while True:
	pngfile = input("Enter the file path and name and remember that end of the file enter '.png' or q to Quit: ")
	if pngfile != 'q':
		saveIco = input("Enter the file name and path that you want to save the file and remember that end of the file enter '.ico': ")
		logo = Image.open(pngfile)
		logo.save(saveIco,format='ICO')
	elif pngfile == 'q':
		break