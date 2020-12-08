
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
 * <p>Original spec-file type: GetAnnotationOntologyEventsOutput</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "events"
})
public class GetAnnotationOntologyEventsOutput {

    @JsonProperty("events")
    private List<AnnotationOntologyEvent> events;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("events")
    public List<AnnotationOntologyEvent> getEvents() {
        return events;
    }

    @JsonProperty("events")
    public void setEvents(List<AnnotationOntologyEvent> events) {
        this.events = events;
    }

    public GetAnnotationOntologyEventsOutput withEvents(List<AnnotationOntologyEvent> events) {
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
        return ((((("GetAnnotationOntologyEventsOutput"+" [events=")+ events)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
