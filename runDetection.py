import paho.mqtt.client as mqtt
from PlateReadHOGOCR import startProgramDetection
from CardReadHOGOCR import startProgramCardDetection
import requests
import json

host = "localhost"
port = 1883


def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("start_Program_Detection_Image")
    self.subscribe("start_Program_Card_Detection_Image")
    self.subscribe("start_Program_Check_Card")
    # self.publish("program_status_update","HEllow")


def on_message(client, userdata, msg):
    print("On_message.")
    data = json.loads(msg.payload.decode("utf-8", "strict"))
    print(data)
    if data['message'] == 'start program':
        uuid = data['uuid']
        finaldata = startProgramDetection(uuid)
        print(finaldata)
        # for final_data in finaldata:
        #     response = requests.post(
        #         'http://localhost:5000/api/insertdatabyimage', data=final_data)
        #     json_response = response.json()
        #     print("result => ", json_response)

        # response = requests.put(
        #     'http://localhost:5000/api/video/updateStatusImage', data={"upload_by": "image"})
        # json_response = response.json()
        # print("status => ", json_response)
        print("End!")

    elif data['message'] == 'start program card':
        uuid = data['uuid']
        finalData = startProgramCardDetection(uuid)
        print(finalData)
        # for final_data in finalData:
        #     response = requests.post(
        #         'http://localhost:5000/api/insertstudentbyimage', data=final_data)
        #     json_response = response.json()
        #     print("result => ", json_response)

        print("End!")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()
