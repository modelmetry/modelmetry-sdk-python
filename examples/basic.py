import os
import sys

sys.path.append(".")

import modelmetry.sdk
from devtools import debug
from dotenv import load_dotenv

load_dotenv()


def main():

    # Instantiate the SDK with your tenant_id and api_key
    # You can find your API key in Modelmetry's settings
    client = modelmetry.sdk.Client(
        tenant_id=os.getenv("TENANT_ID"),
        api_key=os.getenv("API_KEY"),
        host=os.getenv("HOST"),
    )

    guardrails = client.guardrails()

    # Call the guardrail with the CallGuardrailRequestBody object
    res = guardrails.check(
        guardrail_id="grd_jaohzgcbd5hbt1grwmvp",
        input_text="I want to know the weather in London tomorrow",
    )

    # C'mon... who are we if we aren't even logging stuff to the terminal?
    debug(res)

    # Check the outcome of the guardrail and handle the happy and unhappy paths accordingly.
    if res.passed:
        print("Sorry user, I cannot help you with this query at the moment.")

        # You can have access to more data for debugging (scores, evaluation(s) that failed) in the Call
        for entry in res.check.summarised_entries:
            print(entry)

    else:
        print("Passed!")

    client.shutdown()
    return


if __name__ == "__main__":
    main()
