from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            # Call your processing function here
            result = process_photo(photo.image.path)
            return render(request, 'result.html', {'result': result})
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def process_photo(image_path):
    # Add your image processing logic here
    # Example: return the image size
    from PIL import Image
    with Image.open(image_path) as img:
        return img.size
