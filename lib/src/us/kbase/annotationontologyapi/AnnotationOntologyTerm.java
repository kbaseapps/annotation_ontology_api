
package us.kbase.annotationontologyapi;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: AnnotationOntologyTerm</p>
 * <pre>
 * Insert your typespec information here.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "term",
    "modelseed_id",
    "evidence"
})
public class AnnotationOntologyTerm {

    @JsonProperty("term")
    private String term;
    @JsonProperty("modelseed_id")
    private String modelseedId;
    @JsonProperty("evidence")
    private String evidence;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("term")
    public String getTerm() {
        return term;
    }

    @JsonProperty("term")
    public void setTerm(String term) {
        this.term = term;
    }

    public AnnotationOntologyTerm withTerm(String term) {
        this.term = term;
        return this;
    }

    @JsonProperty("modelseed_id")
    public String getModelseedId() {
        return modelseedId;
    }

    @JsonProperty("modelseed_id")
    public void setModelseedId(String modelseedId) {
        this.modelseedId = modelseedId;
    }

    public AnnotationOntologyTerm withModelseedId(String modelseedId) {
        this.modelseedId = modelseedId;
        return this;
    }

    @JsonProperty("evidence")
    public String getEvidence() {
        return evidence;
    }

    @JsonProperty("evidence")
    public void setEvidence(String evidence) {
        this.evidence = evidence;
    }

    public AnnotationOntologyTerm withEvidence(String evidence) {
        this.evidence = evidence;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("AnnotationOntologyTerm"+" [term=")+ term)+", modelseedId=")+ modelseedId)+", evidence=")+ evidence)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
