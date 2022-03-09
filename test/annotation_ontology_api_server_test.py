# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser



from annotation_ontology_api.annotation_ontology_apiImpl import annotation_ontology_api
from annotation_ontology_api.annotation_ontology_apiServer import MethodContext
from annotation_ontology_api.authclient  import KBaseAuth as _KBaseAuth
from installed_clients.WorkspaceClient import Workspace


class annotation_ontology_apiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = os.environ.get("KB_AUTH_TOKEN", None)
        config_file = os.environ.get("KB_DEPLOYMENT_CONFIG", None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items("annotation_ontology_api"):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg["auth-service-url"]
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update(
            {
                "token": token,
                "user_id": user_id,
                "provenance": [
                    {
                        "service": "annotation_ontology_api",
                        "method": "please_never_use_it_in_production",
                        "method_params": [],
                    }
                ],
                "authenticated": 1,
            }
        )
        cls.wsURL = cls.cfg["workspace-url"]
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = annotation_ontology_api(cls.cfg)
        cls.scratch = cls.cfg["scratch"]
        cls.callback_url = os.environ["SDK_CALLBACK_URL"]
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({"workspace": cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "wsName"):
            cls.wsClient.delete_workspace({"workspace": cls.wsName})
            print("Test workspace was deleted")

    def test_empty_genome(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        public_genome = "45053/16/1"
        parameters = {
            "input_ref": public_genome,
            "input_workspace": self.wsName
        }
        expected_output = [{'events': [{'description': 'GenomeFileUtils Genbank uploader from '
                                                       'annotations:0.11.2:GO:2021_01_28_17_24_10',
                                        'event_id': 'GenomeFileUtils Genbank uploader from '
                                                    'annotations:0.11.2:GO:2021_01_28_17_24_10',
                                        'method': 'GenomeFileUtils Genbank uploader from annotations',
                                        'method_version': '0.11.2',
                                        'ontology_id': 'GO',
                                        'ontology_terms': {},
                                        'original_description': None,
                                        'timestamp': '2021_01_28_17_24_10'}],
                            'feature_types': {}}]

        ret = self.serviceImpl.get_annotation_ontology_events(self.ctx, parameters)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        self.assertEqual(ret,expected_output)