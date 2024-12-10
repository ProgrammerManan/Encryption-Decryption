import base64
"""BASE64 FUNCTION"""
def base64_transform(text, encode=True):
    if encode:
        return base64.b64encode(text.encode()).decode()
    else:
        try:
            return base64.b64decode(text.encode()).decode()
        except Exception as e:
            return "Invalid Base64 string"
