---
parent: Entities
title: biolink:BiologicalProcess
grand_parent: Classes
layout: default
---

# Class: BiologicalProcess


One or more causally connected executions of molecular functions

URI: [biolink:BiologicalProcess](https://w3id.org/biolink/BiologicalProcess)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysiologicalProcess],[PhysicalEntity],[Pathway],[PathologicalProcess],[OrganismTaxon],[OntologyClass],[Occurrent],[NamedThing],[MacromolecularMachineToBiologicalProcessAssociation],[GeneOrGeneProduct],[BiologicalProcessOrActivity],[MacromolecularMachineToBiologicalProcessAssociation]-%20object%201..1%3E[BiologicalProcess%7Cprovided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[BiologicalProcess]uses%20-.-%3E[Occurrent],[BiologicalProcess]uses%20-.-%3E[OntologyClass],[BiologicalProcess]%5E-[PhysiologicalProcess],[BiologicalProcess]%5E-[Pathway],[BiologicalProcess]%5E-[PathologicalProcess],[BiologicalProcess]%5E-[Behavior],[BiologicalProcessOrActivity]%5E-[BiologicalProcess],[Behavior],[Attribute])

---


## Identifier prefixes

 * GO
 * REACT
 * metacyc.reaction
 * KEGG.MODULE
 * KEGG

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Children

 * [Behavior](Behavior.md)
 * [PathologicalProcess](PathologicalProcess.md) - A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.
 * [Pathway](Pathway.md)
 * [PhysiologicalProcess](PhysiologicalProcess.md)

## Referenced by class

 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of](acts_upstream_of.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of negative effect](acts_upstream_of_negative_effect.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of or within](acts_upstream_of_or_within.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of or within negative effect](acts_upstream_of_or_within_negative_effect.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of or within positive effect](acts_upstream_of_or_within_positive_effect.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[acts upstream of positive effect](acts_upstream_of_positive_effect.md)*  <sub>0..\*</sub>  **[BiologicalProcess](BiologicalProcess.md)**
 *  **[MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[BiologicalProcess](BiologicalProcess.md)**

## Attributes


### Inherited from biological process or activity:

 * [has input](has_input.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [enabled by](enabled_by.md)  <sub>0..\*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * Range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | GO:0008150 |
|  | | SIO:000006 |
|  | | WIKIDATA:Q2996394 |
| **Broad Mappings:** | | WIKIDATA:P682 |

