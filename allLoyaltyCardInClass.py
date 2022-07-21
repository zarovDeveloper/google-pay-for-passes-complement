import setup
import authAcc

###############################################################################
# Create all objects.
# https://developers.google.com/pay/passes/rest/v1/loyaltyobject/list
###############################################################################

allObjects_url = 'https://walletobjects.googleapis.com/walletobjects/v1/loyaltyClass/'
allObjects = {

}

allObject_response = authAcc.http_client.get(allObjects_url + setup.class_id)
print("object GET response:", allObject_response.text)
