# import modules
import requests

# Request headers set Subscription key which provides access to this API. Found in your Cognitive Services accounts.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'b26c80db11e54e9bb5ae1e28eca80639',
}

img_path = "F:\\Downloads-F\\fawadTrain.jpg"

data =  open(img_path, 'rb').read()


# Request URL 
FaceApiDetect = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender,headPose,smile,facialHair' 

# try:
    # REST Call 
response = requests.post(FaceApiDetect, data=data, headers=headers) 
print("RESPONSE:" + str(response.json()))

# except Exception as e:
#     print(e)




personGroupId="friends"

data = dict()
data["name"] = "F.R.I.E.N.D.S"
data["userData"] = "All friends cast"
data = str(data)

#Request URL 
FaceApiCreateLargePersonGroup = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId 

# try:
    # REST Call 
response = requests.put(FaceApiCreateLargePersonGroup, data=data, headers=headers) 
print("RESPONSE:" + str(response.status_code))

# except Exception as e:
#     print(e)



headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b26c80db11e54e9bb5ae1e28eca80639',
}
#Request data
data = dict()
data["name"] = "Chandler"
data["userData"] = "Friends"
data = str(data)

#Request URL 
FaceApiCreatePerson = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons' 

# try:
#     # REST Call 
response = requests.post(FaceApiCreatePerson, data=data, headers=headers) 
responseJson = response.json()
print(responseJson)
personId = responseJson["personId"]
print("PERSONID: "+str(personId))
    
# except Exception as e:
#     print(e)






headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'b26c80db11e54e9bb5ae1e28eca80639',
}

# 5 random images of chandler
chandlerImageList = [
        # "http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659"
        # "https://i.pinimg.com/236x/b0/57/ff/b057ff0d16bd5205e4d3142e10f03394--muriel-matthew-perry.jpg",
        # "https://qph.fs.quoracdn.net/main-qimg-74677a162a39c79d6a9aa2b11cc195b1",
        # "https://pbs.twimg.com/profile_images/2991381736/e2160154f215a325b0fc73f866039311_400x400.jpeg",
        "F:\\Downloads-F\\fawadTrain.jpg"
    ]

#Request URL 
FaceApiCreatePerson = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId+'/persistedFaces' 

for image in chandlerImageList:
    # img_path = "F:\\Downloads-F\\facetest.png"

    data =  open(image, 'rb').read()

    # data = dict()
    # data["url"] = image
    # data = str(data)

    # try:
    # REST Call 
    response = requests.post(FaceApiCreatePerson, data=data, headers=headers) 
    responseJson = response.json()
    persistedFaceId = responseJson["persistedFaceId"]
    print("PERSISTED FACE ID: "+str(persistedFaceId))
    
    # except Exception as e:
    #     print(e)









#Request data
data = dict()

#Request URL 
FaceApiTrain = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/train'

# try:
    # REST Call 
response = requests.post(FaceApiTrain, data=data, headers=headers) 
print("RESPONSE:" + str(response.status_code))

# except Exception as e:
#     print(e)







# Request data

img_path = "F:\\Downloads-F\\fawadTest.jpg"

data =  open(img_path, 'rb').read()


# data = dict()
# data["url"] = "F:\\Downloads-F\\facetest.png"
# data = str(data)

# Request URL 
FaceApiDetect = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true' 

# try:
    # REST Call 
response = requests.post(FaceApiDetect, data=data, headers=headers) 
responseJson = response.json()
faceId = responseJson[0]["faceId"]
print("FACE ID: "+str(faceId))

# except Exception as e:
#     print(e)


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b26c80db11e54e9bb5ae1e28eca80639',
}






faceIdsList = [faceId]

# Request data
data = dict()
data["personGroupId"] = personGroupId
data["faceIds"] = faceIdsList
data["maxNumOfCandidatesReturned"] = 1 
data["confidenceThreshold"] = 0.5
data = str(data)

# Request URL 
FaceApiIdentify = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/identify' 

# try:
    # REST Call 
response = requests.post(FaceApiIdentify, data=data, headers=headers) 
responseJson = response.json()
personId = responseJson[0]["candidates"][0]["personId"]
confidence = responseJson[0]["candidates"][0]["confidence"]
print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
        
# except Exception as e:
#     print("Could not detect")











# Request URL 
FaceApiGetPerson = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId

# try:
response = requests.get(FaceApiGetPerson, headers=headers) 
responseJson = response.json()
print("This Is "+str(responseJson["name"]))
    
# except Exception as e:
#     print(e)