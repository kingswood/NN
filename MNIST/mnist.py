import sys

def get_data_and_labels(images_filename, labels_filename):
	print("Opening files ...")
	images_file = open(images_filename, "rb")
	labels_file = open(labels_filename, "rb")

	try:
		print("Reading files ...")
		images_file.read(4)
		num_of_items = int.from_bytes(images_file.read(4), byteorder="big") #6000
		num_of_rows = int.from_bytes(images_file.read(4), byteorder="big") #28
		num_of_colums = int.from_bytes(images_file.read(4), byteorder="big") #28
		
		labels_file.read(8) #8800388049504
		
	

		num_of_image_values = num_of_rows * num_of_colums # 28 * 28
		
		data = [[None for x in range(num_of_image_values)] for y in range(num_of_items)] # (28 * 28) * 6000
		labels = []
		
		for item in range(50):
			for value in range(num_of_image_values):
				data[item][value] = int.from_bytes(images_file.read(1),byteorder="big")
			labels.append(int.from_bytes(labels_file.read(1), byteorder="big"))
			
			#for i in range(data[0].len)
			#print(len(data[item]))
			for i in range(len(data[item])):
				if((i%num_of_rows)==0):
					print()
				sys.stdout.write(str(data[item][i]).ljust(3))
			
			print()
			print(labels[item])
		
		return data, labels
	finally:
		images_file.close()
		labels_file.close()
		print("Files closed.")


images_filename = "data/train-images.idx3-ubyte"
labels_filename = "data/train-labels.idx1-ubyte"
data, labels = get_data_and_labels(images_filename, labels_filename)