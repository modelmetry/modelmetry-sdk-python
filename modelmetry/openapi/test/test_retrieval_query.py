# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.retrieval_query import RetrievalQuery

class TestRetrievalQuery(unittest.TestCase):
    """RetrievalQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrievalQuery:
        """Test RetrievalQuery
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrievalQuery`
        """
        model = RetrievalQuery()
        if include_optional:
            return RetrievalQuery(
                embeddings = [
                    1.337
                    ],
                text_representation = ''
            )
        else:
            return RetrievalQuery(
                text_representation = '',
        )
        """

    def testRetrievalQuery(self):
        """Test RetrievalQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
