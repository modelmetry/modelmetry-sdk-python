import json
from modelmetry.openapi.models.assistant_message import AssistantMessage
from modelmetry.openapi.models.completion_family_data import CompletionFamilyData
from modelmetry.openapi.models.system_message import SystemMessage
from modelmetry.openapi.models.text_part import TextPart
from modelmetry.openapi.models.user_message import UserMessage
from modelmetry.openapi.types import Unset


data = CompletionFamilyData(
    messages=[
        SystemMessage(
            contents=[TextPart(text="You're a helpful assistant.")], role="system"
        ),
        UserMessage(contents=[TextPart(text="What's the weather like?")], role="user"),
        AssistantMessage(
            contents=[TextPart(text="The weather is nice today.")], role="assistant"
        ),
        UserMessage(contents=[TextPart(text="Thanks a lot!")], role="user"),
    ],
)

print(json.dumps(data.to_dict(), indent=2))


# CompletionFamilyData(
#   cost=None,
#   documents=None,
#   messages=[
#     SystemMessage(contents=[TextPart(text="You're a helpful assistant.")], role='system', name=<modelmetry.openapi.types.Unset object at 0x104f1dee0>),
#     UserMessage(contents=[TextPart(text="What's the weather like?")], role='user', name=<modelmetry.openapi.types.Unset object at 0x104f1dee0>),
#     AssistantMessage(contents=[TextPart(text='The weather is nice today.')], role='assistant', name=<modelmetry.openapi.types.Unset object at 0x104f1dee0>, tool_calls=<modelmetry.openapi.types.Unset object at 0x104f1dee0>),
#     UserMessage(contents=[TextPart(text='Thanks a lot!')], role='user', name=<modelmetry.openapi.types.Unset object at 0x104f1dee0>)],
#   options=None,
#   usage=None
# )
