
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
 * <p>Original spec-file type: GetAnnotationOntologyEventsParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input_ref",
    "input_workspace",
    "query_events",
    "query_genes"
})
public class GetAnnotationOntologyEventsParams {

    @JsonProperty("input_ref")
    private java.lang.String inputRef;
    @JsonProperty("input_workspace")
    private java.lang.String inputWorkspace;
    @JsonProperty("query_events")
    private List<String> queryEvents;
    @JsonProperty("query_genes")
    private List<String> queryGenes;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("input_ref")
    public java.lang.String getInputRef() {
        return inputRef;
    }

    @JsonProperty("input_ref")
    public void setInputRef(java.lang.String inputRef) {
        this.inputRef = inputRef;
    }

    public GetAnnotationOntologyEventsParams withInputRef(java.lang.String inputRef) {
        this.inputRef = inputRef;
        return this;
    }

    @JsonProperty("input_workspace")
    public java.lang.String getInputWorkspace() {
        return inputWorkspace;
    }

    @JsonProperty("input_workspace")
    public void setInputWorkspace(java.lang.String inputWorkspace) {
        this.inputWorkspace = inputWorkspace;
    }

    public GetAnnotationOntologyEventsParams withInputWorkspace(java.lang.String inputWorkspace) {
        this.inputWorkspace = inputWorkspace;
        return this;
    }

    @JsonProperty("query_events")
    public List<String> getQueryEvents() {
        return queryEvents;
    }

    @JsonProperty("query_events")
    public void setQueryEvents(List<String> queryEvents) {
        this.queryEvents = queryEvents;
    }

    public GetAnnotationOntologyEventsParams withQueryEvents(List<String> queryEvents) {
        this.queryEvents = queryEvents;
        return this;
    }

    @JsonProperty("query_genes")
    public List<String> getQueryGenes() {
        return queryGenes;
    }

    @JsonProperty("query_genes")
    public void setQueryGenes(List<String> queryGenes) {
        this.queryGenes = queryGenes;
    }

    public GetAnnotationOntologyEventsParams withQueryGenes(List<String> queryGenes) {
        this.queryGenes = queryGenes;
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
        return ((((((((((("GetAnnotationOntologyEventsParams"+" [inputRef=")+ inputRef)+", inputWorkspace=")+ inputWorkspace)+", queryEvents=")+ queryEvents)+", queryGenes=")+ queryGenes)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
