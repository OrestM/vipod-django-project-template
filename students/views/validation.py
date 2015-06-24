import magic

VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]

def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):    
    return any([url.endswith(e) for e in extension_list])

VALID_IMAGE_MINETYPES = [
    "image"
]

def get_mimetype(fobject):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype

def valid_image_minetype(fobject):
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False 

MAX_SIZE = 2*1024*1024

def valid_image_size(image, max_size=MAX_SIZE):
    width, height = image.size
    if (width * height) > max_size:
        return (False, "Image is too large")
    return (True, image)
