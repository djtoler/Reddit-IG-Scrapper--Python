import requests
import json

url = "https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile"

querystring = {"ig":"rap","response_type":"feeds"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "instagram-bulk-profile-scrapper.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
jsonResponse = response.json()[0]
# jsonParseResponse = json.loads(jsonResponse)

result = type(jsonResponse)
# print(json.loads(jsonResponse))

i = 0
x = jsonResponse.get("feed")
postUsername = jsonResponse.get("username")
postImage = x.get("data")[0].get("image_versions2").get("candidates")[3].get("url")
postCaption = x.get("data")[0].get("caption").get("text")

# xxx = xx[0].get("image_versions2")
# xxxx = xxx.get("candidates")
# pics = xxxx[3].get("url")
print(postUsername, "<<---USERNAME")
print(postImage, "<<---IMAGE")
print(postCaption, "<<---CAPTION")

# for key in jsonResponse:
#         i = i + 1
#         print(i, key, '->', jsonResponse[key])

# print(jsonResponse.keys())
# print(response[0].feed.data[0].has_audio)
# print(response[0].feed.data[0].image_versions2.candidates[3].url)