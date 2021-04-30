
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
 * <p>Original spec-file type: AnnotationOntologyTerm</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "term",
    "modelseed_ids",
    "evidence"
})
public class AnnotationOntologyTerm {

    @JsonProperty("term")
    private java.lang.String term;
    @JsonProperty("modelseed_ids")
    private List<String> modelseedIds;
    @JsonProperty("evidence")
    private java.lang.String evidence;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("term")
    public java.lang.String getTerm() {
        return term;
    }

    @JsonProperty("term")
    public void setTerm(java.lang.String term) {
        this.term = term;
    }

    public AnnotationOntologyTerm withTerm(java.lang.String term) {
        this.term = term;
        return this;
    }

    @JsonProperty("modelseed_ids")
    public List<String> getModelseedIds() {
        return modelseedIds;
    }

    @JsonProperty("modelseed_ids")
    public void setModelseedIds(List<String> modelseedIds) {
        this.modelseedIds = modelseedIds;
    }

    public AnnotationOntologyTerm withModelseedIds(List<String> modelseedIds) {
        this.modelseedIds = modelseedIds;
        return this;
    }

    @JsonProperty("evidence")
    public java.lang.String getEvidence() {
        return evidence;
    }

    @JsonProperty("evidence")
    public void setEvidence(java.lang.String evidence) {
        this.evidence = evidence;
    }

    public AnnotationOntologyTerm withEvidence(java.lang.String evidence) {
        this.evidence = evidence;
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
        return ((((((((("AnnotationOntologyTerm"+" [term=")+ term)+", modelseedIds=")+ modelseedIds)+", evidence=")+ evidence)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
