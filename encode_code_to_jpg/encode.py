
#Storing informations
# with open('testimage2.jpg', 'ab') as f:
#     f.write(b"Hello")  #Whatever text or code we wanna write


#Fetching informations
# with open('testimage2.jpg', 'rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))
#     f.seek(offset+2)
#     print(f.read())


#----Store png file informatiosn into jpg
import PIL.Image
import io

# img = PIL.Image.open('test.png')
# byte_arr = io.BytesIO()
# img.save(byte_arr, format='png')


# with open('testimage2.jpg', 'ab') as f:
#     f.write(byte_arr.getvalue())



#Lopading the image again
# with open('testimage2.jpg', 'rb') as f:
#     content = f.read()
#     offset = content.index(bytes.fromhex('FFD9'))
#     f.seek(offset+2)

#     new_img = PIL.Image.open(io.BytesIO(f.read()))
#     new_img.save("new_image.png")

