import pickle

path = "C:/Python/Inflearn/python/제19장(파일과 예외처리)/files/"
filename = path + "save.p"

# gameOption = {
#     "Sound" : 8,
#     "VideoQuality" : "High",
#     "Money" : 100000,
#     "WeaponList" : ["gun", "missile", "knife"]
# }

# file = open(filename, "wb")
# pickle.dump(gameOption, file)

# file.close()

file = open(filename, "rb")
obj = pickle.load(file)
print(obj)