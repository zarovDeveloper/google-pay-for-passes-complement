import setup

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

###############################################################################
# Create authenticated HTTP client, using service account file.
###############################################################################

# [START auth]
credentials = service_account.Credentials.from_service_account_file(setup.service_account_file,
    scopes=["https://www.googleapis.com/auth/wallet_object.issuer"])
http_client = AuthorizedSession(credentials)
# [END auth]
