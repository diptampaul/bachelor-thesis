from django.shortcuts import render
from .models import encodeFile, decodeFile
import PIL.Image
import io,os

# Create your views here.
def ecdc(request):
    if request.method == 'POST':
        file_type = request.POST.get('filetype')
        u_file = request.FILES.get('file', False)
        jpg_file = request.FILES.get('jpg', False)
        # print(u_file)
        # print(jpg_file)
        encode_obj = encodeFile(
            file_type = file_type,
            upload1 = u_file,
            upload2 = jpg_file
        )
        encode_obj.save()
        if encode_obj.file_type == 'text' or encode_obj.file_type == 'others':
            #Storing informations
            with open(f'media/{encode_obj.upload2}', 'ab') as f, open(f'media/{encode_obj.upload1}', 'rb') as e:
                f.write(e.read())
        elif encode_obj.file_type == 'png':
            img = PIL.Image.open(f'media/{encode_obj.upload1}')
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='png')
            with open(f'media/{encode_obj.upload2}', 'ab') as f:
                f.write(byte_arr.getvalue())

        return render(request, 'encode_download.htm', {'encode_obj': encode_obj})
                

    else:
        return render(request, 'encode_decode.htm',{})

def decode(request):
    if request.method == 'POST':
        our_file = request.FILES.get('o_file', False)
        print(our_file)
        decode_obj = decodeFile(
            encoded = our_file
        )
        decode_obj.save()
        try:
            with open(f'media/{decode_obj.encoded}', 'ab') as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FFD9'))
                f.seek(offset+2)

                new_img = PIL.Image.open(io.BytesIO(f.read()))
                new_img.save("new_image.png")
                file_name = 'new_image.png'
        except :
            with open(f'media/{decode_obj.encoded}', 'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FFD9'))
                f.seek(offset+2)
                with open('newfile.txt', 'wb') as e:
                    e.write(f.read())
                    file_name = 'newfile.txt'

        #print(os.listdir())
        return render(request, 'decode_download.htm', {'path': f'{os.listdir()}/{file_name}'})
    else:
        return render(request, 'encode_decode.htm',{})