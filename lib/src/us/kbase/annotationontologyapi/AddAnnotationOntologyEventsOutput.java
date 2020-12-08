
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
 * <p>Original spec-file type: AddAnnotationOntologyEventsOutput</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "output_ref"
})
public class AddAnnotationOntologyEventsOutput {

    @JsonProperty("output_ref")
    private String outputRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("output_ref")
    public String getOutputRef() {
        return outputRef;
    }

    @JsonProperty("output_ref")
    public void setOutputRef(String outputRef) {
        this.outputRef = outputRef;
    }

    public AddAnnotationOntologyEventsOutput withOutputRef(String outputRef) {
        this.outputRef = outputRef;
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
        return ((((("AddAnnotationOntologyEventsOutput"+" [outputRef=")+ outputRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
