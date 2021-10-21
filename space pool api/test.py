import requests


# url = "https://developer.pool.space/api/v1/farms/0xaa44f53b655e33a2d565786bfc5537f992d90ca48e28a01695994e38c004b15c/partials"
# url = "https://developer.pool.space/api/v1/farms/0xaa44f53b655e33a2d565786bfc5537f992d90ca48e28a01695994e38c004b15c/payouts"
# url = "https://developer.pool.space/api/v1/farms/0xaa44f53b655e33a2d565786bfc5537f992d90ca48e28a01695994e38c004b15c/rewards"
url = "https://developer.pool.space/api/v1/farms/0xaa44f53b655e33a2d565786bfc5537f992d90ca48e28a01695994e38c004b15c"
# url = "https://developer.pool.space/api/v1/pool"

spacePoolHeaders = {
    "Accept": "text/plain",
    "Developer-Key": "O0jlUJr1Es2lEsqdQmSZTTnfc5Q2pxCUc8pKWXQ3Czz18EmTANYvnVoAjIyX3EYT",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
response = requests.request("GET", url, headers=spacePoolHeaders)

print(response.text)

# def lineNotifyMessage(token, msg):
#     lineHeaders = {
#         "Authorization": "Bearer " + token, 
#         "Content-Type" : "application/x-www-form-urlencoded"
#     }
#     linePayload = {'message': msg }
#     r = requests.post("https://notify-api.line.me/api/notify", headers = lineHeaders, params = linePayload)
#     return r.status_code


# token = '5GwyfbOA7RxjwIpLP3UVtpPuYPs9ZBdwWzUzu9jGuLx'
# lineNotifyMessage(token, response.text)



