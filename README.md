# Example Flask Dance setup with an application factory

An example template for using flask dance with an application factory.  This
example uses Google Authentication.


## Setup

You will need to plugin your client_id and secret key into config.py or export
them as environment variables. 

## Execution

```
pip install -r requirements.txt
export FLASK_APP=example.py
OAUTHLIB_INSECURE_TRANSPORT=1
OAUTHLIB_RELAX_TOKEN_SCOPE=1

flask run
```
