# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.assistant_message import AssistantMessage

class TestAssistantMessage(unittest.TestCase):
    """AssistantMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssistantMessage:
        """Test AssistantMessage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssistantMessage`
        """
        model = AssistantMessage()
        if include_optional:
            return AssistantMessage(
                contents = [
                    modelmetry.openapi.models.assistant_message_contents_inner.AssistantMessage_Contents_inner()
                    ],
                name = '',
                role = 'assistant',
                tool_calls = [
                    modelmetry.openapi.models.tool_call.ToolCall(
                        function = modelmetry.openapi.models.function.Function(
                            arguments = null, 
                            name = '', ), 
                        id = '', 
                        type = 'function', )
                    ]
            )
        else:
            return AssistantMessage(
                contents = [
                    modelmetry.openapi.models.assistant_message_contents_inner.AssistantMessage_Contents_inner()
                    ],
                role = 'assistant',
        )
        """

    def testAssistantMessage(self):
        """Test AssistantMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
