import base64

def image_to_uri(path):
    with open(path, 'rb') as f:
        img = f.read()
    return base64.b64encode(img).decode("utf-8")


