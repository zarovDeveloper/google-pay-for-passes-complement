import setup
import authAcc

###############################################################################
# Create a class via the API (this can also be done in the business console).
# https://developers.google.com/pay/passes/rest/v1/loyaltyclass
###############################################################################

# [START class]
class_url = "https://walletobjects.googleapis.com/walletobjects/v1/loyaltyClass/"
class_payload = {
    "id": "%s.%s" % (setup.issuer_id, setup.class_id),
    "issuerName": "test issuer name",
    "programName": "test program name",
    "programLogo": {
        "kind": "walletobjects#image",
        "sourceUri": {
            "kind": "walletobjects#uri",
            "uri": "http://farm8.staticflickr.com/7340/11177041185_a61a7f2139_o.jpg"
        }
    },
    "reviewStatus": "underReview"
}

class_response = authAcc.http_client.post(class_url, json=class_payload)
print("class POST response:", class_response.text)
# [END class]
