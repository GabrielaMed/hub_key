import win32ui
from PIL import Image, ImageWin

def print_img(imgs, printer, selected_pages, copies):
	selected_imgs = imgs

	if "-" in selected_pages:
		index_toPrint = selected_pages.split("-")
		selected_imgs = []
		i = int(index_toPrint[-1])
		# i = 5
		while i >= int(index_toPrint[0]): # [0] = 2
			print(f"valor de i: {i} / valor de {index_toPrint[0]}")
			selected_imgs.insert(0, imgs[int(i)-1])
			print(f"aqui : {selected_imgs}")
			i -= 1
			
	if "," in selected_pages:
		index_toPrint = selected_pages.split(",")
		selected_imgs = []
		i = int(index_toPrint[-1])
		# i = 5
		for i in index_toPrint:
			selected_imgs.append(imgs[int(i)-1])
	# Constants for GetDeviceCaps
	#
	#
	# HORZRES / VERTRES = printable area
	#
	HORZRES = 8
	VERTRES = 10
	#
	# LOGPIXELS = dots per inch
	#
	LOGPIXELSX = 88
	LOGPIXELSY = 90
	#
	# PHYSICALWIDTH/HEIGHT = total area
	#
	PHYSICALWIDTH = 110
	PHYSICALHEIGHT = 111
	#
	# PHYSICALOFFSETX/Y = left / top margin
	#
	PHYSICALOFFSETX = 112
	PHYSICALOFFSETY = 113

	printer_name = printer

	#
	# You can only write a Device-independent bitmap
	#  directly to a Windows device context; therefore
	#  we need (for ease) to use the Python Imaging
	#  Library to manipulate the image.
	#
	# Create a device context from a named printer
	#  and assess the printable size of the paper.
	#
	hDC = win32ui.CreateDC()
	hDC.CreatePrinterDC(printer_name)
	printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
	printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
	printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
		
	hDC.StartDoc(selected_imgs[0])

	for cop in range(copies):
		for i in selected_imgs:
			file_name = i

			#
			# Open the image, rotate it if it's wider than
			#  it is high, and work out how much to multiply
			#  each pixel by to get it as big as possible on
			#  the page without distorting.
			#
			bmp = Image.open (file_name)
			if bmp.size[0] > bmp.size[1]:
				bmp = bmp.rotate (90)

			ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
			scale = min (ratios)

			#
			# Start the print job, and draw the bitmap to
			# the printer device at the scaled size.
			#
			hDC.StartPage()

			dib = ImageWin.Dib (bmp)
			scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
			x1 = int ((printer_size[0] - scaled_width) / 2)
			y1 = int ((printer_size[1] - scaled_height) / 2)
			x2 = x1 + scaled_width
			y2 = y1 + scaled_height
			dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

			hDC.EndPage()
	hDC.EndDoc()
	hDC.DeleteDC()