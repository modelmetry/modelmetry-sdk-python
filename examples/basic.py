import sys
sys.path.append('.')

import modelmetry.sdk
from modelmetry.openapi.models import CallGuardrailRequestBody, Payload, Input, TextInput
from devtools import debug

def main():

  # Instantiate the SDK with your tenant_id and api_key
  # You can find your API key in Modelmetry's settings
  client = modelmetry.sdk.Client(tenant_id = "ten_xxx", api_key = "abcdef")

  # Call the guardrail with the CallGuardrailRequestBody object
  res = client.call_guardrail(CallGuardrailRequestBody(
    # Use the guardrail ID your want to call and check your payload against.
    # And you can edit the various evaluators used by this guardrail in your Modelmetry dashboard.
    GuardrailID="grd_xyz",
    # The payload object is used to pass the data your guardrail should evaluate synchronously.
    Payload=Payload(
      Input=Input(
        Text=TextInput(
          Text="Hello, World!"
        )
      )
    ),
  ))

  # C'mon... who are we if we aren't even logging stuff to the terminal?
  debug(res)

  # Check the outcome of the guardrail and handle the happy and unhappy paths accordingly.
  if not res.Passed:
    print("Sorry user, I cannot help you with this query at the moment. I've forward this to the team so they can get back to you shortly.")

    # You can have access to more data for debugging (scores, evaluation(s) that failed) in the Call
    for entry in res.Call.summarised_entries:
      print(entry)

if __name__ == "__main__":
    main()