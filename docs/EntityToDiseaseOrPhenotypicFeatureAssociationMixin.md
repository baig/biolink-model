---
parent: Class Mixins
title: biolink:EntityToDiseaseOrPhenotypicFeatureAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToDiseaseOrPhenotypicFeatureAssociationMixin




URI: [biolink:EntityToDiseaseOrPhenotypicFeatureAssociationMixin](https://w3id.org/biolink/vocab/EntityToDiseaseOrPhenotypicFeatureAssociationMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]%3Cobject%201..1-%20[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[CellLineToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[DiseaseOrPhenotypicFeature],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation],[ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation],[CellLineToDiseaseOrPhenotypicFeatureAssociation])

---


## Mixin for

 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
 * [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary, typically (but not always) undesirable effect.
 * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary undesirable effect.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An association between a material sample and a disease or phenotype.

## Referenced by class


## Attributes


### Own

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
