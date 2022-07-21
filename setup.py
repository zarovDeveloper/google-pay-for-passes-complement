import os
import re

# [START setup]
# Path to service account key file obtained from Google CLoud Console.
service_account_file = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ".json")

# Issuer ID obtained from Google Pay Business Console/Google Wallet API/ID issuer.
issuer_id = os.environ.get("WALLET_ISSUER_ID", "ID issuer")

# Developer defined ID for the wallet class.
class_id = os.environ.get("WALLET_CLASS_ID", "123")

# Developer defined ID for the user, eg an email address.
user_id = os.environ.get("WALLET_USER_ID", "test@gmail.com")

# ID for the wallet object, must be in the form `issuer_id.user_id` where user_id is alphanumeric.
object_id = "%s.%s-%s" % (issuer_id, re.sub(r"[^\w.-]", "_", user_id), class_id)
# [END setup]
