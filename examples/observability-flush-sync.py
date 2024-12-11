import os
import sys

sys.path.append(".")

import modelmetry.sdk
from devtools import pprint
from dotenv import load_dotenv

load_dotenv()


def main():

    # Instantiate the SDK with your tenant_id and api_key. You can find your API key in Modelmetry's settings
    client = modelmetry.sdk.Client(
        tenant_id=os.getenv("TENANT_ID"),
        api_key=os.getenv("API_KEY"),
        host=os.getenv("HOST"),
    )

    observability = client.observability()

    observability.on_flush_success_callback = lambda traces: print(
        f"Successfully flushed {len(traces)} traces"
    )

    observability.on_flush_failure_callback = lambda traces, exception: print(
        f"Failed to flush {len(traces)} traces: {exception}"
    )

    t1 = observability.trace("python.demo")
    t1.event("Just a quick event to show the first demo started :)")

    s1 = t1.completion("first-span", "openai/gpt-3.5-turbo")
    s1.add_system_text("You're a helpful assistant.")
    s1.add_user_text("What's the weather like?")
    s1.event("Just a quick event to show the first span started :)")
    s1.add_assistant_text("The weather is nice today.")
    s1.add_user_text("Thanks a lot!")
    s1.finding(
        name="cloudiness",
        value=0.2,
        comment="The sky is mostly clear, with a few clouds.",
        source="sdk",
    )
    s1.end()

    t1.end()

    observability.flush_sync()
    observability.shutdown()


if __name__ == "__main__":
    main()
