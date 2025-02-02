# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.options import Options

class TestOptions(unittest.TestCase):
    """Options unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Options:
        """Test Options
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Options`
        """
        model = Options()
        if include_optional:
            return Options(
                api_key = '',
                api_version = '',
                base_url = '',
                deployment_id = '',
                frequency_penalty = 1.337,
                function_call = '',
                functions = [
                    ''
                    ],
                logit_bias = None,
                logprobs = True,
                max_tokens = 56,
                model = '',
                model_list = [
                    ''
                    ],
                n = 56,
                presence_penalty = 1.337,
                provider = '',
                response_format = None,
                seed = 56,
                stop = None,
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
                user = ''
            )
        else:
            return Options(
        )
        """

    def testOptions(self):
        """Test Options"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
