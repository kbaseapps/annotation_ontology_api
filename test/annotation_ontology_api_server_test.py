# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ

try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from annotation_ontology_api.annotation_ontology_apiImpl import annotation_ontology_api
from annotation_ontology_api.annotation_ontology_apiServer import MethodContext
from annotation_ontology_api.authclient import KBaseAuth as _KBaseAuth


class annotation_ontology_apiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('annotation_ontology_api'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'annotation_ontology_api',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = annotation_ontology_api(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_annotation_ontology_api_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_empty_genome(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        public_genome = "45053/16/1"
        parameters = {
            "input_ref": public_genome,
            "input_workspace": self.getWsName()
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

        ret = self.getImpl().get_annotation_ontology_events(self.getContext(), parameters)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        self.assertEqual(ret,expected_output)

