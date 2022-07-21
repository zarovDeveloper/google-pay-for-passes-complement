import setup
import authAcc

from google.auth import jwt, crypt

###############################################################################
# Get or create an object via the API.
# https://developers.google.com/pay/passes/rest/v1/loyaltyobject
###############################################################################

# [START object]
object_url = "https://walletobjects.googleapis.com/walletobjects/v1/loyaltyObject/"
object_payload = {
    "id": setup.object_id,
    "classId": "%s.%s" % (setup.issuer_id, setup.class_id),
    "heroImage": {
        "sourceUri": {
            "uri": "https://farm4.staticflickr.com/3723/11177041115_6e6a3b6f49_o.jpg",
            "description": "Test heroImage description"
        }
    },
    "textModulesData": [
        {
            "header": "Test text module header",
            "body": "Test text module body"
        }
    ],
    "linksModuleData": {
        "uris": [
            {
                "kind": "walletobjects#uri",
                "uri": "http://maps.google.com/",
                "description": "Test link module uri description"
            },
            {
                "kind": "walletobjects#uri",
                "uri": "tel:6505555555",
                "description": "Test link module tel description"
            }
        ]
    },
    "imageModulesData": [
        {
            "mainImage": {
                "kind": "walletobjects#image",
                "sourceUri": {
                    "kind": "walletobjects#uri",
                    "uri": "http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg",
                    "description": "Test image module description"
                }
            }
        }
    ],
    "barcode": {
        "kind": "walletobjects#barcode",
        "type": "qrCode",
        "value": "Test QR Code"
    },
    "state": "active",
    "accountId": "Test account ID",
    "accountName": "Test account name",
    "loyaltyPoints": {
        "balance": {
            "string": "800"
        },
        "label": "Points"
    },
}

# Retrieve the object, or create it if it doesn't exist.
object_response = authAcc.http_client.get(object_url + setup.object_id)
if object_response.status_code == 404:
    object_response = authAcc.http_client.post(object_url, json=object_payload)
print("object GET or POST response:", object_response.text)
# [END object]

###############################################################################
# Create a JWT for the object, and encode it to create a "Save" URL.
###############################################################################

# [START jwt]
claims = {
    "iss": authAcc.http_client.credentials.service_account_email,  # `client_email` in service account file.
    "aud": "google",
    "origins": ["www.example.com"],
    "typ": "savetowallet",
    "payload": {
        "loyaltyObjects": [{"id": setup.object_id}]
    }
}

signer = crypt.RSASigner.from_service_account_file(setup.service_account_file)
token = jwt.encode(signer, claims).decode("utf-8")
save_url = "https://pay.google.com/gp/v/save/%s" % token
print(save_url)
# [END jwt]
