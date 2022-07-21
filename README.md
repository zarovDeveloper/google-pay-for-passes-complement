# google-pay-for-passes-complement
Google Pay For Passes complete with various functions for Loyalty Card.

# Start setup
1. Follow steps 1 and 2 in <a href="https://developers.google.com/pay/passes/guides/basic-setup/get-access-to-rest-api">Get Access to REST API</a> to create a Google Pay API for Passes account and tie your service account to it.
2. Set up <a href="https://virtualenv.pypa.io/en/stable/">virtualenv</a> to create an isolated python environment. See <a href="https://cloud.google.com/python/docs/setup#installing_and_using_virtualenv">installing and using virtualenv</a>
3. Make sure you've "activated" the virtualenv install dependencies:

		pip install -r requirements.txt
		
4. Upload your API.json to the root of the project

# Create desing card:

<li>
	<ul>Boarding Passes - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/flightclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/flightobject">Object</a></ul>
</li>
<li>
	<ul>Event Tickets - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template?vertical=event-tickets#pass-vertical">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/eventticketclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/eventticketobject">Object</a></ul>   
</li>
<li>
	<ul>Gift Cards - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template?vertical=gift-cards#pass-vertical">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/giftcardclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/giftcardobject">Object</a></ul>
</li>
<li>
	<ul>Loyalty - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template?vertical=loyalty#pass-vertical">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/loyaltyclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/loyaltyobject">Object</a></ul>
</li>
<li>	
	<ul>Offers - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template?vertical=offers#pass-vertical">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/offerclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/offerobject">Object</a></ul>
</li>
<li>
	<ul>Transit - <a href="https://developers.google.com/pay/passes/guides/pass-verticals/pass-template?vertical=transit-passes#pass-vertical">Design</a> | <a href="https://developers.google.com/pay/passes/rest/v1/transitclass">Class</a> | <a href="https://developers.google.com/pay/passes/rest/v1/transitobject">Object</a></ul>
</li>	
