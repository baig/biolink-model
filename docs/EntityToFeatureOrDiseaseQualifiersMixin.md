---
parent: Class Mixins
title: biolink:EntityToFeatureOrDiseaseQualifiersMixin
grand_parent: Classes
layout: default
---

# Class: EntityToFeatureOrDiseaseQualifiersMixin


Qualifiers for entity to disease or phenotype associations.

URI: [biolink:EntityToFeatureOrDiseaseQualifiersMixin](https://w3id.org/biolink/vocab/EntityToFeatureOrDiseaseQualifiersMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyQualifierMixin],[EntityToPhenotypicFeatureAssociationMixin],[Onset]%3Conset%20qualifier%200..1-%20[EntityToFeatureOrDiseaseQualifiersMixin%7Cfrequency_qualifier(i):frequency_value%20%3F],[SeverityValue]%3Cseverity%20qualifier%200..1-%20[EntityToFeatureOrDiseaseQualifiersMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[EntityToPhenotypicFeatureAssociationMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[EntityToDiseaseAssociationMixin],[FrequencyQualifierMixin]%5E-[EntityToFeatureOrDiseaseQualifiersMixin],[EntityToDiseaseAssociationMixin])

---


## Parents

 *  is_a: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations

## Children

 * [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) - mixin class for any association whose object (target node) is a disease
 * [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)

## Referenced by class


## Attributes


### Own

 * [onset qualifier](onset_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * Range: [Onset](Onset.md)
     * in subsets: (translator_minimal)
 * [severity qualifier](severity_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * Range: [SeverityValue](SeverityValue.md)
     * in subsets: (translator_minimal)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>0..1</sub>
     * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * Range: [FrequencyValue](types/FrequencyValue.md)
     * in subsets: (translator_minimal)
