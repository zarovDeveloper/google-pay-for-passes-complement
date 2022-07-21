import setup
import authAcc

###############################################################################
# Data update.
# https://developers.google.com/pay/passes/rest/v1/loyaltyclass/patch
###############################################################################

object_url = "https://walletobjects.googleapis.com/walletobjects/v1/loyaltyObject/" + setup.object_id
object_update = {
    "accountName": "Misha",
    "loyaltyPoints": {
        "balance": {
            "string": "3000"
        },
        "label": "Points"
    },
}

# Retrieve the object, or create it if it doesn't exist.
object_response = authAcc.http_client.get(object_url + setup.object_id)
if object_response.status_code == 404:
    object_response = authAcc.http_client.patch(object_url, json=object_update)
print("object GET or PATCH response:", object_response.text)
