import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-iufbfeavfqqzri2a1toob4eqpp1o0os7qa33jorulvz','4b171c068dcccc74c1a0155dae6533f5')
service = CloudantV1(authenticator=authenticator)
service.set_service_url('https://245c54f0-3778-46cb-bfd9-6e1bfca37902-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
  _, frame = cap.read()
  decodedObjects = pyzbar.decode(frame)
  for obj in decodedObjects:
    a=obj.data.decode('UTF-8')
    cv2.putText(frame, "Ticket", (50,50), font, 2, (255, 0, 0), 3)
    try:
      response = service.get_document(db='booking', doc_id =a).get_result()
      print(response)
      time.sleep(5)
    except Exception as e:
      print("Not a Valid Ticket")
      time.sleep(5)

  cv2.imshow("Frame", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
client.disconnect()
