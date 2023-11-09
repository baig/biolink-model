---
parent: Class Mixins
title: biolink:CellLineToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: CellLineToEntityAssociationMixin


An relationship between a cell line and another entity

URI: [biolink:CellLineToEntityAssociationMixin](https://w3id.org/biolink/vocab/CellLineToEntityAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CellLine]%3Csubject%201..1-%20[CellLineToEntityAssociationMixin],[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[CellLineToEntityAssociationMixin],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[CellLine])

---


## Mixin for

 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.

## Referenced by class


## Attributes


### Own

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
