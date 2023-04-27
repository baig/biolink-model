---
parent: Class Mixins
title: biolink:GeneGroupingMixin
grand_parent: Classes
layout: default
---

# Class: GeneGroupingMixin


any grouping of multiple genes or gene products

URI: [biolink:GeneGroupingMixin](https://w3id.org/biolink/vocab/GeneGroupingMixin)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Gene]%3Chas%20gene%20or%20gene%20product%200..%2A-%20[GeneGroupingMixin],[ProteinFamily]uses%20-.-%3E[GeneGroupingMixin],[ProteinDomain]uses%20-.-%3E[GeneGroupingMixin],[GenomicBackgroundExposure]uses%20-.-%3E[GeneGroupingMixin],[GeneFamily]uses%20-.-%3E[GeneGroupingMixin],[DrugToGeneInteractionExposure]uses%20-.-%3E[GeneGroupingMixin],[ProteinFamily],[ProteinDomain],[GenomicBackgroundExposure],[GeneFamily],[Gene],[DrugToGeneInteractionExposure])

---


## Mixin for

 * [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) (mixin)  - drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
 * [GeneFamily](GeneFamily.md) (mixin)  - any grouping of multiple genes or gene products related by common descent
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [ProteinDomain](ProteinDomain.md) (mixin)  - A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
 * [ProteinFamily](ProteinFamily.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [has gene or gene product](has_gene_or_gene_product.md)  <sub>0..\*</sub>
     * Description: connects an entity with one or more gene or gene products
     * Range: [Gene](Gene.md)
