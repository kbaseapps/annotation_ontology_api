# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import shutil
import gzip
import json
import requests
import datetime
from pprint import pformat
from annotation_ontology_api.annotation_ontology_api import AnnotationOntologyAPI
from Workspace.WorkspaceClient import Workspace as workspaceService
from DataFileUtil.DataFileUtilClient import DataFileUtil
# silence whining
requests.packages.urllib3.disable_warnings()
#END_HEADER


class annotation_ontology_api:
    '''
    Module Name:
    annotation_ontology_api

    Module Description:
    A KBase module: annotation_ontology_api
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/annotation_ontology_api.git"
    GIT_COMMIT_HASH = "515c9c1b8f029cc18c5f27904771adc706820376"

    #BEGIN_CLASS_HEADER
    def cache(self,params):
        if not os.path.exists(self.config["scratch"]+"/cache/"):
            os.makedirs(self.config["scratch"]+"/cache/")
        if "cache" in self.config and self.config["cache"] == 1:
            json_str = json.dumps(params)
            json_bytes = json_str.encode('utf-8')
            ct = datetime.datetime.now()
            ct = ct.replace(" ","")
            ct = ct.replace(":","_")
            jsonfilename = self.config["scratch"]+"/cache/"+self.config["ctx"]["user_id"]+"-"+ct+".gz"
            with gzip.open(jsonfilename, 'w') as fout:
                fout.write(json_bytes)
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.ws_client = None
        self.dfu_client = None
        if 'SDK_CALLBACK_URL' in os.environ:
            self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
            self.dfu_client = DataFileUtil(self.config['SDK_CALLBACK_URL'])
            self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
            self.ws_client = workspaceService(config["workspace-url"])
        #END_CONSTRUCTOR
        pass


    def get_annotation_ontology_events(self, ctx, params):
        """
        Retrieves annotation ontology events in a standardized form cleaning up inconsistencies in underlying data
        :param params: instance of type "GetAnnotationOntologyEventsParams"
           -> structure: parameter "input_ref" of String, parameter
           "input_workspace" of String, parameter "query_events" of list of
           String, parameter "query_genes" of list of String, parameter
           "standardize_modelseed_ids" of Long
        :returns: instance of type "GetAnnotationOntologyEventsOutput" ->
           structure: parameter "events" of list of type
           "AnnotationOntologyEvent" -> structure: parameter "event_id" of
           String, parameter "description" of String, parameter "ontology_id"
           of String, parameter "method" of String, parameter
           "method_version" of String, parameter "timestamp" of String,
           parameter "feature_types" of mapping from String to String,
           parameter "ontology_terms" of mapping from String to list of type
           "AnnotationOntologyTerm" -> structure: parameter "term" of String,
           parameter "modelseed_ids" of list of String, parameter "evidence"
           of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_annotation_ontology_events
        self.config['ctx'] = ctx
        self.cache(params)
        #print(("Input parameters: " + pformat(params)))
        anno_api = None
        if self.ws_client == None:
            if "workspace-url" in params:
                anno_api = AnnotationOntologyAPI(self.config,workspaceService(params['workspace-url'], token=ctx['token']),self.dfu_client)
            else:
                anno_api = AnnotationOntologyAPI(self.config,workspaceService(self.config['workspace-url'], token=ctx['token']),self.dfu_client)
        else:
            anno_api = AnnotationOntologyAPI(self.config,self.ws_client,self.dfu_client)
        output = anno_api.get_annotation_ontology_events(params)
        #END get_annotation_ontology_events

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method get_annotation_ontology_events return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def add_annotation_ontology_events(self, ctx, params):
        """
        Adds a new annotation ontology event to a genome or AMA
        :param params: instance of type "AddAnnotationOntologyEventsParams"
           -> structure: parameter "input_ref" of String, parameter
           "input_workspace" of String, parameter "output_name" of String,
           parameter "output_workspace" of String, parameter "clear_existing"
           of Long, parameter "overwrite_matching" of Long, parameter
           "events" of list of type "AnnotationOntologyEvent" -> structure:
           parameter "event_id" of String, parameter "description" of String,
           parameter "ontology_id" of String, parameter "method" of String,
           parameter "method_version" of String, parameter "timestamp" of
           String, parameter "feature_types" of mapping from String to
           String, parameter "ontology_terms" of mapping from String to list
           of type "AnnotationOntologyTerm" -> structure: parameter "term" of
           String, parameter "modelseed_ids" of list of String, parameter
           "evidence" of String
        :returns: instance of type "AddAnnotationOntologyEventsOutput" ->
           structure: parameter "output_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN add_annotation_ontology_events
        self.config['ctx'] = ctx
        self.cache(params)
        #print(("Input parameters: " + pformat(params)))
        anno_api = None
        if self.ws_client == None:
            if "workspace-url" in params:
                anno_api = AnnotationOntologyAPI(self.config,workspaceService(params['workspace-url'], token=ctx['token']),self.dfu_client)
            else:
                anno_api = AnnotationOntologyAPI(self.config,workspaceService(self.config['workspace-url'], token=ctx['token']),self.dfu_client)
        else:
            anno_api = AnnotationOntologyAPI(self.config,self.ws_client,self.dfu_client)
        output = anno_api.add_annotation_ontology_events(params)
        #END add_annotation_ontology_events

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method add_annotation_ontology_events return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def svradmin(self, ctx, params):
        """
        Admin function for use in debugging
        :param params: instance of unspecified object
        :returns: instance of unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN svradmin
        self.cache(params)
        output = {}
        if ctx["user_id"] != "chenry":
            return {"error":"unauthorized"}
        for command in params["commands"]:
            if command == "clear_cache":
                folder = os.path.join(self.config["scratch"], "cache")
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))
            if command == "list":
                output[command] = os.listdir(os.path.join(self.config["scratch"], "cache"))
            if command == "fetch":
                jsonfilename = os.path.join(self.config["scratch"],"cache",params["commands"][command])
                with gzip.open(jsonfilename, 'r') as fin:
                    json_bytes = fin.read()
                    json_str = json_bytes.decode('utf-8')
                    output[command] = json.loads(json_str)
        #END svradmin

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method svradmin return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
