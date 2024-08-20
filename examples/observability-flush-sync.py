import os
import sys

sys.path.append(".")

import modelmetry.sdk
from devtools import debug
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

    observability.on_flush_success_callback = lambda traces: debug(
        f"Successfully flushed {len(traces)} traces", traces
    )

    observability.on_flush_failure_callback = lambda traces, exception: debug(
        traces, exception
    )

    t1 = client.observability().trace("python.demo")
    t1.event("Just a quick event to show the first demo started :)")

    s1 = t1.completion("first-span", "openai/gpt-3.5-turbo")
    s1.event("Just a quick event to show the first span started :)")
    s1.end()

    t1.end()

    client.observability().flush_sync()
    client.observability().shutdown()


if __name__ == "__main__":
    main()
