
package us.kbase.annotationontologyapi;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: AnnotationOntologyEvent</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "event_id",
    "ontology_id",
    "method",
    "method_version",
    "timestamp",
    "ontology_terms"
})
public class AnnotationOntologyEvent {

    @JsonProperty("event_id")
    private java.lang.String eventId;
    @JsonProperty("ontology_id")
    private java.lang.String ontologyId;
    @JsonProperty("method")
    private java.lang.String method;
    @JsonProperty("method_version")
    private java.lang.String methodVersion;
    @JsonProperty("timestamp")
    private java.lang.String timestamp;
    @JsonProperty("ontology_terms")
    private Map<String, List<AnnotationOntologyTerm>> ontologyTerms;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("event_id")
    public java.lang.String getEventId() {
        return eventId;
    }

    @JsonProperty("event_id")
    public void setEventId(java.lang.String eventId) {
        this.eventId = eventId;
    }

    public AnnotationOntologyEvent withEventId(java.lang.String eventId) {
        this.eventId = eventId;
        return this;
    }

    @JsonProperty("ontology_id")
    public java.lang.String getOntologyId() {
        return ontologyId;
    }

    @JsonProperty("ontology_id")
    public void setOntologyId(java.lang.String ontologyId) {
        this.ontologyId = ontologyId;
    }

    public AnnotationOntologyEvent withOntologyId(java.lang.String ontologyId) {
        this.ontologyId = ontologyId;
        return this;
    }

    @JsonProperty("method")
    public java.lang.String getMethod() {
        return method;
    }

    @JsonProperty("method")
    public void setMethod(java.lang.String method) {
        this.method = method;
    }

    public AnnotationOntologyEvent withMethod(java.lang.String method) {
        this.method = method;
        return this;
    }

    @JsonProperty("method_version")
    public java.lang.String getMethodVersion() {
        return methodVersion;
    }

    @JsonProperty("method_version")
    public void setMethodVersion(java.lang.String methodVersion) {
        this.methodVersion = methodVersion;
    }

    public AnnotationOntologyEvent withMethodVersion(java.lang.String methodVersion) {
        this.methodVersion = methodVersion;
        return this;
    }

    @JsonProperty("timestamp")
    public java.lang.String getTimestamp() {
        return timestamp;
    }

    @JsonProperty("timestamp")
    public void setTimestamp(java.lang.String timestamp) {
        this.timestamp = timestamp;
    }

    public AnnotationOntologyEvent withTimestamp(java.lang.String timestamp) {
        this.timestamp = timestamp;
        return this;
    }

    @JsonProperty("ontology_terms")
    public Map<String, List<AnnotationOntologyTerm>> getOntologyTerms() {
        return ontologyTerms;
    }

    @JsonProperty("ontology_terms")
    public void setOntologyTerms(Map<String, List<AnnotationOntologyTerm>> ontologyTerms) {
        this.ontologyTerms = ontologyTerms;
    }

    public AnnotationOntologyEvent withOntologyTerms(Map<String, List<AnnotationOntologyTerm>> ontologyTerms) {
        this.ontologyTerms = ontologyTerms;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((((("AnnotationOntologyEvent"+" [eventId=")+ eventId)+", ontologyId=")+ ontologyId)+", method=")+ method)+", methodVersion=")+ methodVersion)+", timestamp=")+ timestamp)+", ontologyTerms=")+ ontologyTerms)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
