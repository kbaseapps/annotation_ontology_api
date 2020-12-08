/*
A KBase module: annotation_ontology_api
*/

module annotation_ontology_api {
    typedef structure {
    	string term;
    	list<string> modelseed_ids;#Ignored on input - set automatically on output
    	string evidence;#Optional
    } AnnotationOntologyTerm;
    
    typedef structure {
		string event_id;#On input - this is always method:ontology_id:timestamp
		string description;#Keep description if provided but enforce uniqueness using timestamp
		string ontology_id;#Replacing current "id" field
		string method;
		string method_version;
		string timestamp;
		mapping<string gene_id,list<AnnotationOntologyTerm> terms> ontology_terms;
	} AnnotationOntologyEvent;
    
    #Need to handle translation of obsolete ModelSEED rxn IDs both from translations or when the ontology fed in is an ModelSEED rxn ID    
    typedef structure {
		string input_ref;
		string input_workspace;
		list<string> query_events;
		list<string> query_genes;
		bool standardize_modelseed_ids;
    } GetAnnotationOntologyEventsParams;
    
    typedef structure {
		list<AnnotationOntologyEvent> events;
    } GetAnnotationOntologyEventsOutput;
    
    /*
        Retrieves annotation ontology events in a standardized form cleaning up inconsistencies in underlying data
    */
    funcdef get_annotation_ontology_events(GetAnnotationOntologyEventsParams params) returns (GetAnnotationOntologyEventsOutput output) authentication optional;
	
	typedef structure {
		string input_ref;
		string input_workspace;
		string output_name;
		string output_workspace;
		list<AnnotationOntologyEvent> events;
    } AddAnnotationOntologyEventsParams;
    
    typedef structure {
		string output_ref;
    } AddAnnotationOntologyEventsOutput;
    
    /*
        Adds a new annotation ontology event to a genome or AMA
    */
	funcdef add_annotation_ontology_events(AddAnnotationOntologyEventsParams params) returns (AddAnnotationOntologyEventsOutput output) authentication optional;
};
