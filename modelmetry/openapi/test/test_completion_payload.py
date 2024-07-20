# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.completion_payload import CompletionPayload

class TestCompletionPayload(unittest.TestCase):
    """CompletionPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompletionPayload:
        """Test CompletionPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompletionPayload`
        """
        model = CompletionPayload()
        if include_optional:
            return CompletionPayload(
                context = modelmetry.openapi.models.completion_payload_context.CompletionPayloadContext(
                    parsed_system = '', 
                    retrieved_items = [
                        {
                            'key' : null
                            }
                        ], ),
                input = modelmetry.openapi.models.input.Input(
                    chat = modelmetry.openapi.models.chat_input.ChatInput(
                        messages = [
                            modelmetry.openapi.models.simple_message.SimpleMessage(
                                contents = [
                                    modelmetry.openapi.models.simple_part.SimplePart(
                                        detail = 'auto', 
                                        mime_type = '', 
                                        text = '', 
                                        uri = '', )
                                    ], 
                                name = '', 
                                role = 'system', 
                                tool_call_id = '', 
                                tool_calls = [
                                    modelmetry.openapi.models.tool_call.ToolCall(
                                        function = modelmetry.openapi.models.function.Function(
                                            arguments = null, 
                                            name = '', ), 
                                        id = '', 
                                        type = 'function', )
                                    ], )
                            ], 
                        settings = modelmetry.openapi.models.simple_options.SimpleOptions(
                            frequency_penalty = 1.337, 
                            logprobs = True, 
                            max_tokens = 56, 
                            n = 56, 
                            presence_penalty = 1.337, 
                            seed = 56, 
                            stream = True, 
                            temperature = 0, 
                            timeout = 0, 
                            tool_choice = '', 
                            tools = [
                                modelmetry.openapi.models.tool.Tool(
                                    description = '', 
                                    name = '', 
                                    parameters = null, )
                                ], 
                            top_logprobs = 56, 
                            top_p = 0, 
                            user = '', ), ), 
                    text = modelmetry.openapi.models.text_input.TextInput(
                        text = '', ), ),
                model = '',
                options = modelmetry.openapi.models.simple_options.SimpleOptions(
                    frequency_penalty = 1.337, 
                    logprobs = True, 
                    max_tokens = 56, 
                    n = 56, 
                    presence_penalty = 1.337, 
                    seed = 56, 
                    stream = True, 
                    temperature = 0, 
                    timeout = 0, 
                    tool_choice = '', 
                    tools = [
                        modelmetry.openapi.models.tool.Tool(
                            description = '', 
                            name = '', 
                            parameters = null, )
                        ], 
                    top_logprobs = 56, 
                    top_p = 0, 
                    user = '', ),
                output = modelmetry.openapi.models.output.Output(
                    chat = modelmetry.openapi.models.chat_input.ChatInput(
                        messages = [
                            modelmetry.openapi.models.simple_message.SimpleMessage(
                                contents = [
                                    modelmetry.openapi.models.simple_part.SimplePart(
                                        detail = 'auto', 
                                        mime_type = '', 
                                        text = '', 
                                        uri = '', )
                                    ], 
                                name = '', 
                                role = 'system', 
                                tool_call_id = '', 
                                tool_calls = [
                                    modelmetry.openapi.models.tool_call.ToolCall(
                                        function = modelmetry.openapi.models.function.Function(
                                            arguments = null, 
                                            name = '', ), 
                                        id = '', 
                                        type = 'function', )
                                    ], )
                            ], 
                        settings = modelmetry.openapi.models.simple_options.SimpleOptions(
                            frequency_penalty = 1.337, 
                            logprobs = True, 
                            max_tokens = 56, 
                            n = 56, 
                            presence_penalty = 1.337, 
                            seed = 56, 
                            stream = True, 
                            temperature = 0, 
                            timeout = 0, 
                            tool_choice = '', 
                            tools = [
                                modelmetry.openapi.models.tool.Tool(
                                    description = '', 
                                    name = '', 
                                    parameters = null, )
                                ], 
                            top_logprobs = 56, 
                            top_p = 0, 
                            user = '', ), ), 
                    text = modelmetry.openapi.models.text_input.TextInput(
                        text = '', ), )
            )
        else:
            return CompletionPayload(
                model = '',
                options = modelmetry.openapi.models.simple_options.SimpleOptions(
                    frequency_penalty = 1.337, 
                    logprobs = True, 
                    max_tokens = 56, 
                    n = 56, 
                    presence_penalty = 1.337, 
                    seed = 56, 
                    stream = True, 
                    temperature = 0, 
                    timeout = 0, 
                    tool_choice = '', 
                    tools = [
                        modelmetry.openapi.models.tool.Tool(
                            description = '', 
                            name = '', 
                            parameters = null, )
                        ], 
                    top_logprobs = 56, 
                    top_p = 0, 
                    user = '', ),
        )
        """

    def testCompletionPayload(self):
        """Test CompletionPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
