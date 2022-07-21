import setup
import authAcc

###############################################################################
# Create message.
# https://developers.google.com/pay/passes/rest/v1/loyaltyobject/addmessage?hl=eu
###############################################################################

object_url = "https://walletobjects.googleapis.com/walletobjects/v1/loyaltyObject/" + setup.object_id + "/addMessage"
object_addMessage = {
  "message": {
      "header": "TEST MESSAGE",
      "body": "It's test message!",
      "messageType": "TEXT"
  },
}

###############################################################################
# Sending a message, using POST response.
###############################################################################

object_response = authAcc.http_client.post(object_url, json=object_addMessage)
print("object POST response:", object_response.text)
