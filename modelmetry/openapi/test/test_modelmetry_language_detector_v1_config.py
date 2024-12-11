# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from modelmetry.openapi.models.modelmetry_language_detector_v1_config import ModelmetryLanguageDetectorV1Config

class TestModelmetryLanguageDetectorV1Config(unittest.TestCase):
    """ModelmetryLanguageDetectorV1Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelmetryLanguageDetectorV1Config:
        """Test ModelmetryLanguageDetectorV1Config
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelmetryLanguageDetectorV1Config`
        """
        model = ModelmetryLanguageDetectorV1Config()
        if include_optional:
            return ModelmetryLanguageDetectorV1Config(
                confidence_threshold = 0,
                word_count_threshold = 0
            )
        else:
            return ModelmetryLanguageDetectorV1Config(
                confidence_threshold = 0,
                word_count_threshold = 0,
        )
        """

    def testModelmetryLanguageDetectorV1Config(self):
        """Test ModelmetryLanguageDetectorV1Config"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
