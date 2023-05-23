---
parent: Entities
title: biolink:InformationContentEntity
grand_parent: Classes
layout: default
---

# Class: InformationContentEntity


a piece of information that typically describes some topic of discourse or is used as support.

URI: [biolink:InformationContentEntity](https://w3id.org/biolink/vocab/InformationContentEntity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyVariable],[StudyResult],[RetrievalSource],[Publication],[NamedThing],[ContributorAssociation]-%20subject%201..1%3E[InformationContentEntity%7Clicense:string%20%3F;rights:string%20%3F;format:string%20%3F;creation_date:date%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[InformationContentEntity]%5E-[StudyVariable],[InformationContentEntity]%5E-[StudyResult],[InformationContentEntity]%5E-[RetrievalSource],[InformationContentEntity]%5E-[Publication],[InformationContentEntity]%5E-[EvidenceType],[InformationContentEntity]%5E-[DatasetVersion],[InformationContentEntity]%5E-[DatasetSummary],[InformationContentEntity]%5E-[DatasetDistribution],[InformationContentEntity]%5E-[Dataset],[InformationContentEntity]%5E-[ConfidenceLevel],[InformationContentEntity]%5E-[CommonDataElement],[NamedThing]%5E-[InformationContentEntity],[EvidenceType],[DatasetVersion],[DatasetSummary],[DatasetDistribution],[Dataset],[ContributorAssociation],[ConfidenceLevel],[CommonDataElement],[Attribute],[Agent])

---


## Identifier prefixes

 * doi

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [CommonDataElement](CommonDataElement.md) - A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable  responses, used systematically across different sites, studies, or clinical trials to ensure consistent  data collection. Multiple CDEs (from one or more Collections) can be curated into Forms.  (https://cde.nlm.nih.gov/home)
 * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
 * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
 * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
 * [DatasetSummary](DatasetSummary.md) - an item that holds summary level information about a dataset.
 * [DatasetVersion](DatasetVersion.md) - an item that holds version level information about a dataset.
 * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
 * [Publication](Publication.md) - Any ‘published’ piece of information. Publications are considered broadly  to include any document or document part made available in print or on the  web - which may include scientific journal issues, individual articles, and  books - as well as things like pre-prints, white papers, patents, drug  labels, web pages, protocol documents,  and even a part of a publication if  of significant knowledge scope (e.g. a figure, figure legend, or section  highlighted by NLP). 
 * [RetrievalSource](RetrievalSource.md) - Provides information about how a particular InformationResource served as a source from which knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved.
 * [StudyResult](StudyResult.md) - A collection of data items from a study that are about a particular study subject or experimental unit (the  'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of this data as evidence.
 * [StudyVariable](StudyVariable.md) - a variable that is used as a measure in the investigation of a study

## Referenced by class

 *  **[Agent](Agent.md)** *[contributor](contributor.md)*  <sub>0..\*</sub>  **[InformationContentEntity](InformationContentEntity.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[InformationContentEntity](InformationContentEntity.md)**
 *  **[Agent](Agent.md)** *[provider](provider.md)*  <sub>0..\*</sub>  **[InformationContentEntity](InformationContentEntity.md)**

## Attributes


### Own

 * [creation date](creation_date.md)  <sub>0..1</sub>
     * Description: date on which an entity was created. This can be applied to nodes or edges
     * Range: [Date](types/Date.md)
 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rights](rights.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from gene product mixin:

 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rights](rights.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | information |
|  | | information artefact |
|  | | information entity |
| **Exact Mappings:** | | IAO:0000030 |
| **Narrow Mappings:** | | UMLSSG:CONC |
|  | | STY:T077 |
|  | | STY:T078 |
|  | | STY:T079 |
|  | | STY:T080 |
|  | | STY:T081 |
|  | | STY:T082 |
|  | | STY:T089 |
|  | | STY:T102 |
|  | | STY:T169 |
|  | | STY:T171 |
|  | | STY:T185 |

