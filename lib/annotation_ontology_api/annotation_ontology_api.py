import json
import os
import re

# silence whining
import requests
requests.packages.urllib3.disable_warnings()

source_hash = {
    "MetaCyc" : "META",
    "KEGG" : "RO",
    "BiGG" : "BIGG",
    "rhea" : "RHEA"
}

ontology_translation = {
    "KEGGKO" : "KO",
    "KEGGRO" : "RO",
    "METACYC" : "META",
    "SEED" : "SSO",
    "TCDB" : "TC",
    "MODELSEED" : "MSRXN"
}

ontology_hash = {
    "KO" : 1,
    "EC" : 1,
    "SSO" : 1,
    "RO" : 1,
    "META" : 1,
    "MSRXN" : 1,
    "MSCPD" : 1,
    "MSCPX" : 1,
    "BIGG" : 1,
    "BIGGCPD" : 1,
    "GO" : 1,
    "TC" : 1,
    "RHEA" : 1
};

class AnnotationOntologyAPI:
    def __init__(self,config,ws_client = None, dfu_client = None):
        self.ws_client = ws_client
        self.dfu_client = dfu_client
        self.alias_hash = {}
        self.config = config
    
    def process_workspace_identifiers(self,id_or_ref, workspace=None):
        """
        IDs should always be processed through this function so we can interchangeably use
        refs, IDs, and names for workspaces and objects
        """
        objspec = {}
        if workspace is None or len(id_or_ref.split("/")) > 1:
            objspec["ref"] = id_or_ref
        else:
            if isinstance(workspace, int):
                objspec['wsid'] = workspace
            else:
                objspec['workspace'] = workspace
            if isinstance(id_or_ref, int):
                objspec['objid'] = id_or_ref
            else:
                objspec['name'] = id_or_ref
                
        #print("Object spec:")
        #for key in objspec:
        #    print(key+"\t"+objspec[key])
        return objspec
    
    def get_alias_hash(self,namespace):
        if "MSRXN" not in self.alias_hash:
            filename = self.config["data_directory"]+"/msrxn_hash.json"
            with open(filename) as json_file:
                self.alias_hash["MSRXN"] = json.load(json_file)
        if namespace not in self.alias_hash:
            self.alias_hash[namespace] = {}
            if namespace == "EC":
                filename = self.config["data_directory"]+"/EC_translation.tsv"
                data = ""
                with open(filename, 'r') as file:
                    data = file.read()
                lines = data.split("\n")
                lines.pop(0)
                for line in lines:
                    items = line.split("\t")
                    if len(items) >= 2:
                        modelseed = "MSRXN:"+items[0]
                        if modelseed in self.alias_hash["MSRXN"]:
                            modelseed = self.alias_hash["MSRXN"][modelseed][0]
                        if items[1] not in self.alias_hash["EC"]:
                            self.alias_hash["EC"]["EC:"+items[1]] = []
                        self.alias_hash["EC"]["EC:"+items[1]].append(modelseed)
            elif namespace == "META" or namespace == "RO" or namespace == "BIGG" or namespace == "RHEA":
                filename = self.config["data_directory"]+"/ModelSEED_Reaction_Aliases.txt"
                data = ""
                with open(filename, 'r') as file:
                    data = file.read()
                lines = data.split("\n")
                for line in lines:
                    items = line.split("\t")
                    if len(items) >= 3:
                        modelseed = "MSRXN:"+items[0]
                        if modelseed in self.alias_hash["MSRXN"]:
                            modelseed = self.alias_hash["MSRXN"][modelseed][0]
                        source = None
                        if items[2] in source_hash:
                            source = source_hash[items[2]]
                        if source != None:
                            if source not in self.alias_hash:
                                self.alias_hash[source] = {}
                            if items[1] not in self.alias_hash[source]:
                                self.alias_hash[source][source+":"+items[1]] = []
                            self.alias_hash[source][source+":"+items[1]].append(modelseed)
            elif namespace == "KO":
                filename = self.config["data_directory"]+"/kegg_95_0_ko_seed.tsv"
                data = ""
                with open(filename, 'r') as file:
                    data = file.read()
                lines = data.split("\n")
                lines.pop(0)
                for line in lines:
                    items = line.split("\t")
                    if len(items) >= 2:
                        if items[0] not in self.alias_hash["KO"]:
                            self.alias_hash["KO"]["KO:"+items[0]] = []
                        modelseed_ids = items[1].split(";")
                        id_hash = {}
                        for modelseed in modelseed_ids:
                            modelseed = "MSRXN:"+modelseed
                            if modelseed in self.alias_hash["MSRXN"]:
                                modelseed = self.alias_hash["MSRXN"][modelseed][0]
                            if modelseed not in id_hash:
                                self.alias_hash["KO"]["KO:"+items[0]].append(modelseed)
                            id_hash[modelseed] = 1
            elif namespace == "SSO":
                sso_template = dict()
                filename = self.config["data_directory"]+"/SSO_reactions.json"
                with open(filename) as json_file:
                    sso_template = json.load(json_file)
                for sso in sso_template:
                    id_hash = {}
                    for modelseed in sso_template[sso]:
                        modelseed = "MSRXN:"+modelseed
                        if modelseed in self.alias_hash["MSRXN"]:
                            modelseed = self.alias_hash["MSRXN"][modelseed][0]
                            if modelseed not in id_hash:
                                if sso not in self.alias_hash["SSO"]:
                                    self.alias_hash["SSO"][sso] = []
                                self.alias_hash["SSO"][sso].append(modelseed)
                            id_hash[modelseed] = 1             
            elif namespace == "GO":
                go_translation = dict()
                filename = self.config["data_directory"]+"/GO_ontology_translation.json"
                with open(filename) as json_file:
                    go_translation = json.load(json_file)
                for term in go_translation["translation"]:
                    adjusted_term = "GO:"+term
                    if "equiv_terms" in go_translation["translation"][term]:
                        id_hash = {}
                        for rxn_data in go_translation["translation"][term]["equiv_terms"]:
                            modelseed = rxn_data["equiv_term"]
                            if modelseed in self.alias_hash["MSRXN"]:
                                modelseed = self.alias_hash["MSRXN"][modelseed][0]
                            if adjusted_term not in self.alias_hash["KO"]:
                                self.alias_hash["GO"][adjusted_term] = []
                            if modelseed not in id_hash:
                                self.alias_hash["GO"][adjusted_term].append(modelseed)
                            id_hash[modelseed] = 1                   
        return self.alias_hash[namespace]
                
    def translate_term_to_modelseed(self,term):
        namespace = term.split(":").pop(0)
        if namespace == "MSRXN":
            if term not in self.get_alias_hash(namespace):
                return [term]
            else:
                return self.get_alias_hash(namespace)[term]
        elif term not in self.get_alias_hash(namespace):
            return []
        else:
            return self.get_alias_hash(namespace)[term]
        
    def get_annotation_ontology_events(self,params):
        #Building query hash
        event_query = None
        if "query_events" in params and not params["query_events"] == None:
            for event in params["query_events"]:
                event_query[event] = 1
        gene_query = None
        if "query_genes" in params and not params["query_genes"] == None:
            for gene in params["query_genes"]:
                gene_query[gene] = 1
        #Pull the object from the workspace is necessary
        if "object" not in params:
            res = self.ws_client.get_objects2({"objects": [self.process_workspace_identifiers(params["input_ref"], params["input_workspace"])]})
            params["object"] = res["data"][0]["data"]
            params["type"] = res["data"][0]["info"][2]
        #Get the feature data
        features = []
        if "features" in params["object"]:
            features = params["object"]["features"]
        elif "features_handle_ref" in params["object"]:
            shock_output = self.dfu_client.shock_to_file({
                "handle_id" : params["object"]["features_handle_ref"],
                "file_path" : self.scratch_path
            })
            os.system("gunzip --force ".shock_output["file_path"])
            shock_output["file_path"] = shock_output["file_path"][0:-3]
            with open(shock_output["file_path"]) as json_file:
                features = json.load(json_file)
        output = {"events" : []}
        if "ontology_events" in params["object"]:
            events_array = []
            for event in params["object"]["ontology_events"]:
                id = None
                if "description" in event:
                    id = event["description"]
                else: 
                    id = event["method"]+":"+event["method_version"]+":"+event["id"]+":"+event["timestamp"]
                newevent = {
                    "event_id" : id,
                    "ontology_id" : event["id"],
                    "method" : event["method"],
                    "method_version" : event["method_version"],
                    "timestamp" : event["timestamp"],
                    "ontology_terms" : {}
                }
                newevent["ontology_id"] = newevent["ontology_id"].upper()
                if newevent["ontology_id"] not in ontology_hash and newevent["ontology_id"] in ontology_translation:
                    newevent["ontology_id"] = ontology_translation[newevent["ontology_id"]]
                events_array.append(newevent)
                if event_query == None or id in event_query:
                    output["events"].append(newevent)
            for feature in features:
                if gene_query == None or feature["id"] in gene_query:
                    if "ontology_terms" in feature:
                        for tag in feature["ontology_terms"]:
                            original_tag = tag
                            tag = tag.upper()
                            if tag not in ontology_hash and tag in ontology_translation:
                                tag = ontology_translation[tag]
                            if tag in ontology_hash:
                                for term in feature["ontology_terms"][original_tag]:
                                    original_term = term
                                    array = term.split(":")
                                    if len(array) == 1:
                                        term = tag+":"+array[0]
                                    else:
                                        if array[0] == original_tag or array[0] == original_tag.upper():
                                            array[0] = tag
                                            term = ":".join(array)
                                        else:
                                            term = ":".join(array)
                                            term = tag+":"+term
                                    modelseed_ids = self.translate_term_to_modelseed(term)
                                    for event_index in feature["ontology_terms"][original_tag][original_term]:
                                        if feature["id"] not in events_array[event_index]["ontology_terms"]:
                                            events_array[event_index]["ontology_terms"][feature["id"]] = []
                                        termdata = {"term" : term}
                                        if len(modelseed_ids) > 0:
                                            termdata["modelseed_ids"] = modelseed_ids
                                        if "ontology_evidence" in feature:
                                            if original_term in feature["ontology_evidence"]:
                                                if event_index in feature["ontology_evidence"][original_term]:
                                                    termdata["evidence"] = feature["ontology_evidence"][original_term][event_index]
                                        events_array[event_index]["ontology_terms"][feature["id"]].append(termdata)
        return output
    
    def add_annotation_ontology_events(self,params):
        #Pull the object from the workspace is necessary
        if "object" not in params or params["object"] == None:
            res = self.ws_client.get_objects2({"objects": [self.process_workspace_identifiers(params["input_ref"], params["input_workspace"])]})
            params["object"] = res["data"][0]["data"]
            params["type"] = res["data"][0]["info"][2]
        #Adding ontology
        features = []
        if "features" in params["object"]:
            features = params["object"]["features"]
        elif "features_handle_ref" in params["object"]:
            shock_output = self.dfu_client.shock_to_file({
                "handle_id" : params["object"]["features_handle_ref"],
                "file_path" : self.scratch_path
            })
            os.system("gunzip --force ".shock_output["file_path"])
            shock_output["file_path"] = shock_output["file_path"][0:-3]
            with open(shock_output["file_path"]) as json_file:
                features = json.load(json_file)
        feature_hash = {}
        for feature in features:
           feature_hash[feature["id"]] = feature
        for event in params["events"]:
            event["ontology_id"] = event["ontology_id"].upper()
            if event["ontology_id"] in ontology_translation:
                event["ontology_id"] = ontology_translation[event["ontology_id"]]
            #Creating description
            if "event_id" not in event:
                event["event_id"] = event["method"]+":"+event["method_version"]+":"+event["ontology_id"]+":"+event["timestamp"]
            if "description" not in event:
                event["description"] = event["method"]+":"+event["method_version"]+":"+event["ontology_id"]+":"+event["timestamp"]
            elif event["description"].split(":").pop() != event["timestamp"]:
                event["description"] = event["description"]+":"+event["timestamp"]
            new_event = {
                "description" : event["description"],
                "id" : event["ontology_id"],
                "event_id" : event["method"]+":"+event["ontology_id"]+":"+event["timestamp"],
                "ontology_id" : event["ontology_id"],
                "method" : event["method"],
                "method_version" : event["method_version"],
                "timestamp" : event["timestamp"]
            }
            if "ontology_events" not in params["object"]:
                params["object"]["ontology_events"] = []
            for existing_event in params["object"]["ontology_events"]:
                if new_event["description"] == existing_event["description"]:
                    print("Event description already present in object")
                    return {}
            event_index = len(params["object"]["ontology_events"])
            params["object"]["ontology_events"].append(new_event)
            for gene in event["ontology_terms"]:
                if gene in feature_hash:
                    feature = feature_hash[gene]
                    if "ontology_terms" not in feature:
                        feature["ontology_terms"] = {}
                    if new_event["id"] not in feature["ontology_terms"]:
                        feature["ontology_terms"][new_event["id"]] = {}
                    for term in event["ontology_terms"][gene]:
                        if term["term"].split(":")[0] != new_event["id"]:
                            term["term"] = new_event["id"]+":"+term["term"]
                        if term["term"] not in feature["ontology_terms"][new_event["id"]]:
                            feature["ontology_terms"][new_event["id"]][term["term"]] = []
                        feature["ontology_terms"][new_event["id"]][term["term"]].append(event_index)
                        if "evidence" in term:
                            if "ontology_evidence" not in feature:
                                feature["ontology_evidence"] = {}
                            if term["term"] not in feature["ontology_evidence"]:
                                feature["ontology_evidence"][term["term"]] = {}
                            feature["ontology_evidence"][term["term"]][event_index] = term["evidence"]
        #Saving object
        if params["save"] == 1:
            #Setting provenance
            provenance_params = {}
            for key in params:
                if not key == "object" and not key == "events":
                    provenance_params[key] = params[key]            
            provenance = [{
                'description': 'A function that adds ontology terms to a genome or metagenome',
                'input_ws_objects': [],
                'method': 'add_annotation_ontology_events',
                'method_params': [provenance_params],
                'service': 'annotation_ontology_api',
                'service_ver': 1,
            }]
            params["object"].pop('genbank_handle_ref', None)
            ws_params = {
                'workspace': params["output_workspace"],
                'objects': [{
                    'data': params["object"],
                    'name': params["output_name"],
                    'type': params["type"],
                    'provenance': provenance
                }]
            }
            save_output = self.ws_client.save_objects(ws_params)
            return {"output_ref" : save_output[0][2]}
        else:
            return {
                "object" : params["object"],
                "type" : params["type"]
            }
