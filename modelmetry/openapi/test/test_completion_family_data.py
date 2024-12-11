# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.completion_family_data import CompletionFamilyData

class TestCompletionFamilyData(unittest.TestCase):
    """CompletionFamilyData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompletionFamilyData:
        """Test CompletionFamilyData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompletionFamilyData`
        """
        model = CompletionFamilyData()
        if include_optional:
            return CompletionFamilyData(
                cost = {
                    'key' : null
                    },
                documents = [
                    {
                        'key' : null
                        }
                    ],
                messages = [
                    modelmetry.openapi.models.completion_family_data_messages_inner.CompletionFamilyData_Messages_inner()
                    ],
                options = {
                    'key' : null
                    },
                usage = {
                    'key' : null
                    }
            )
        else:
            return CompletionFamilyData(
        )
        """

    def testCompletionFamilyData(self):
        """Test CompletionFamilyData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
