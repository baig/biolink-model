---
parent: Other Classes
title: biolink:TaxonomicRank
grand_parent: Classes
layout: default
---

# Class: TaxonomicRank


A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

URI: [biolink:TaxonomicRank](https://w3id.org/biolink/vocab/TaxonomicRank)

WIKIDATA:Q427626
{: .mapping-label }


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]-%20has%20taxonomic%20rank%200..1%3E[TaxonomicRank%7Cid(i):string],[OntologyClass]%5E-[TaxonomicRank],[OrganismTaxon],[OntologyClass],[NamedThing])

---


## Identifier prefixes

 * TAXRANK

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has taxonomic rank](has_taxonomic_rank.md)*  <sub>0..1</sub>  **[TaxonomicRank](TaxonomicRank.md)**
 *  **[OrganismTaxon](OrganismTaxon.md)** *[has taxonomic rank](has_taxonomic_rank.md)*  <sub>0..1</sub>  **[TaxonomicRank](TaxonomicRank.md)**

## Attributes


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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WIKIDATA:Q427626 |

