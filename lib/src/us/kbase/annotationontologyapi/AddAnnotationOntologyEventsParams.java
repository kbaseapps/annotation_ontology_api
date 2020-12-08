
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
 * <p>Original spec-file type: AddAnnotationOntologyEventsParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input_ref",
    "input_workspace",
    "output_name",
    "output_workspace",
    "events"
})
public class AddAnnotationOntologyEventsParams {

    @JsonProperty("input_ref")
    private String inputRef;
    @JsonProperty("input_workspace")
    private String inputWorkspace;
    @JsonProperty("output_name")
    private String outputName;
    @JsonProperty("output_workspace")
    private String outputWorkspace;
    @JsonProperty("events")
    private List<AnnotationOntologyEvent> events;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("input_ref")
    public String getInputRef() {
        return inputRef;
    }

    @JsonProperty("input_ref")
    public void setInputRef(String inputRef) {
        this.inputRef = inputRef;
    }

    public AddAnnotationOntologyEventsParams withInputRef(String inputRef) {
        this.inputRef = inputRef;
        return this;
    }

    @JsonProperty("input_workspace")
    public String getInputWorkspace() {
        return inputWorkspace;
    }

    @JsonProperty("input_workspace")
    public void setInputWorkspace(String inputWorkspace) {
        this.inputWorkspace = inputWorkspace;
    }

    public AddAnnotationOntologyEventsParams withInputWorkspace(String inputWorkspace) {
        this.inputWorkspace = inputWorkspace;
        return this;
    }

    @JsonProperty("output_name")
    public String getOutputName() {
        return outputName;
    }

    @JsonProperty("output_name")
    public void setOutputName(String outputName) {
        this.outputName = outputName;
    }

    public AddAnnotationOntologyEventsParams withOutputName(String outputName) {
        this.outputName = outputName;
        return this;
    }

    @JsonProperty("output_workspace")
    public String getOutputWorkspace() {
        return outputWorkspace;
    }

    @JsonProperty("output_workspace")
    public void setOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
    }

    public AddAnnotationOntologyEventsParams withOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
        return this;
    }

    @JsonProperty("events")
    public List<AnnotationOntologyEvent> getEvents() {
        return events;
    }

    @JsonProperty("events")
    public void setEvents(List<AnnotationOntologyEvent> events) {
        this.events = events;
    }

    public AddAnnotationOntologyEventsParams withEvents(List<AnnotationOntologyEvent> events) {
        this.events = events;
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
        return ((((((((((((("AddAnnotationOntologyEventsParams"+" [inputRef=")+ inputRef)+", inputWorkspace=")+ inputWorkspace)+", outputName=")+ outputName)+", outputWorkspace=")+ outputWorkspace)+", events=")+ events)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
