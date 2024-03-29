import requests

def videoAnalysis(sas_token, sas_url, search):
    url = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/my-video-index?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }

    data = {
        "metadataSchema": {
            "fields": [
                {
                    "name": "cameraId",
                    "searchable": False,
                    "filterable": True,
                    "type": "string"
                },
                {
                    "name": "timestamp",
                    "searchable": False,
                    "filterable": True,
                    "type": "datetime"
                }
            ]
        },
        "features": [
            {
                "name": "vision",
                "domain": "surveillance"


            },
            {
                "name": "speech"
            }
        ]
    }

    # Assuming you want to create a new index with a different name
    # Update the index name in the URL to make it unique
    url = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/new-video-index?api-version=2023-05-01-preview"

    response = requests.put(url, json=data, headers=headers)
    
    # test code for errors
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)


    url_index = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/my-video-index/ingestions/my-ingestion?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }


    data_index = {
        "videos": [
            {
                "mode": "add",
                "documentId": sas_token,
                "documentUrl": sas_url,
                "metadata": {
                    "cameraId": "camera1",
                    "timestamp": "2024-02-09 00:02:14"
                }
            }
        ]
    }


    response_index = requests.put(url_index, json=data_index, headers=headers)

    #test code for errors
    print("Index Ingestion - Response Status Code:", response_index.status_code)
    print("Index Ingestion - Response Content:", response_index.text)

    # Assuming you want to ingest another video with a different ingestion name
    url_new_ingestion = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/my-video-index/ingestions/new-ingestion?api-version=2023-05-01-preview"

    data_new_ingestion = {
        "videos": [
            {
                "mode": "add",
                "documentId": "new_document_id",
                "documentUrl": "https://example.blob.core.windows.net/videos/new_video.mp4?sas_token_here",
                "metadata": {
                    "cameraId": "camera3"
                }
            }
        ]
    }


    response_new_ingestion = requests.put(url_new_ingestion, json=data_new_ingestion, headers=headers)

    #used to test code for errors
    print("New Ingestion - Response Status Code:", response_new_ingestion.status_code)
    print("New Ingestion - Response Content:", response_new_ingestion.text)


    url_query = "https://explosion.cognitiveservices.azure.com/computervision/retrieval/indexes/my-video-index:queryByText?api-version=2023-05-01-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "c54eec632ae5413e8075e3f825727822",
        "Content-Type": "application/json"
    }

    data_query = {
        "queryText": search,
        "filters": {
            "stringFilters": [
                {
                    "fieldName": "cameraId",
                    "values": [
                        "camera1"
                    ]
                }
            ],
            "featureFilters": ["vision"]
        }
    }


    response_query = requests.post(url_query, json=data_query, headers=headers)

    return response_query.text

#Enter the sas token
sas_token_1 = "sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D"
#the sas url
sas_url_1= "https://store1video.blob.core.windows.net/haptic-vid/test_video.mp4?sp=r&st=2024-02-09T12:33:24Z&se=2025-08-06T20:33:24Z&spr=https&sv=2022-11-02&sr=b&sig=V%2Fq56JjGcL60r0vt3oAPjzx%2FZMu5%2BJo%2BfjKkJF2ccgo%3D"
#query of what you are looking for 
instance_1 = "Explosion"

#calling the method returns the nested list of the time frames
test_explosion = videoAnalysis(sas_token_1, sas_url_1, instance_1)
print(test_explosion)

#Enter the sas token
sas_token_2 = "sp=r&st=2024-03-17T11:55:51Z&se=2026-04-30T19:55:51Z&spr=https&sv=2022-11-02&sr=b&sig=RNdeiWnjbULMa3icBc1%2FqYuIVrdEMquvksokWZMVL20%3D"
#the sas url
sas_url_2= "https://store1video.blob.core.windows.net/haptic-vid/suv-in-the-dust.mp4?sp=r&st=2024-03-17T11:55:51Z&se=2026-04-30T19:55:51Z&spr=https&sv=2022-11-02&sr=b&sig=RNdeiWnjbULMa3icBc1%2FqYuIVrdEMquvksokWZMVL20%3D"
#query of what you are looking for 
instance_2 = "Vehicle racing" 

#calling the method returns the nested list of the time frames
# test_vehicle = videoAnalysis(sas_token_2, sas_url_2, instance_2)
# print(test_vehicle)