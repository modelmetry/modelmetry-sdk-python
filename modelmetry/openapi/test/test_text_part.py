# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.text_part import TextPart

class TestTextPart(unittest.TestCase):
    """TextPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextPart:
        """Test TextPart
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextPart`
        """
        model = TextPart()
        if include_optional:
            return TextPart(
                text = ''
            )
        else:
            return TextPart(
                text = '',
        )
        """

    def testTextPart(self):
        """Test TextPart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()