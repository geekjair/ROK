import base64
import json
import requests


# def base64_api(uname, pwd, img):
#     with open(img, 'rb') as f:
#         base64_data = base64.b64encode(f.read())
#         b64 = base64_data.decode()
#     data = {"username": uname, "password": pwd, "image": b64, "typeid": 21}
#     result = json.loads(requests.post("https://api.ttshitu.com/imageXYPlus", json=data).text)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#     return ""
#
#
# if __name__ == "__main__":
#     img_path = "/Users/go/PycharmProjects/ROK/images/test123.png"
#     result = base64_api(uname='okiyar', pwd='okiyar', img=img_path)
#     print(result)
#     # 129,323|273,122|318,351
