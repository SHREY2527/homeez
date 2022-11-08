
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import cv2

@csrf_exempt
def get_image(request):
     if request.method == 'POST':
        myfile = request.FILES["image_file"]
        fs = FileSystemStorage(location="flask/media/")
        image_files = fs.save(myfile.name, myfile)
        # file_path= f"flask/media/{image_files}"
        IMAGE_files = cv2.imread(f"flask/media/{image_files}") 
        print(IMAGE_files)
        data={
            'a':'b',
            'd':'e',
        }
        return JsonResponse(data)

#         myfile = request.FILES["data"]
#         fs = FileSystemStorage(location=save_path)
#          filename = fs.save(myfile.name, myfile)
#           training_data = f"fqa_chatbot_api/tmp/{filename}"


        # image_file = open("C:\Users\ASUS\Desktop\homeez_api\flask\media\image.jpeg", "r")
        # fs = FileSystemStorage()
        # filename = fs.save(image_file.name, image_file)
        
        # context={
        #     'fn':filename
        # }
        # return JsonResponse (context)

        
#         myfile = request.FILES["data"]
#         fs = FileSystemStorage(location=save_path)
#          filename = fs.save(myfile.name, myfile)
#           training_data = f"fqa_chatbot_api/tmp/{filename}"

        # image_file = request.FILES['image_file'].read()
        # image_file = request.FILES["image_file"]