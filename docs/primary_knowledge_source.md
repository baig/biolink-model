---
parent: Edge Properties
title: biolink:primary_knowledge_source
grand_parent: Slots
layout: default
---

# Slot: primary_knowledge_source


The most upstream source of the knowledge expressed in an Association that an implementer can identify.  Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources.

URI: [biolink:primary_knowledge_source](https://w3id.org/biolink/vocab/primary_knowledge_source)

## Domain and Range

[Association](Association.md) ->  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [knowledge source](knowledge_source.md)

## Children


## Used by

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)
 * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)
 * [Association](Association.md)
 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md)
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md)
 * [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md)
 * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md)
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)
 * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
 * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md)
 * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)
 * [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)
 * [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)
 * [ContributorAssociation](ContributorAssociation.md)
 * [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md)
 * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md)
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md)
 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md)
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md)
 * [DrugToGeneAssociation](DrugToGeneAssociation.md)
 * [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md)
 * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md)
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md)
 * [FunctionalAssociation](FunctionalAssociation.md)
 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)
 * [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)
 * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)
 * [GeneToGeneAssociation](GeneToGeneAssociation.md)
 * [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md)
 * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md)
 * [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md)
 * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)
 * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
 * [GeneToPathwayAssociation](GeneToPathwayAssociation.md)
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
 * [GenomicSequenceLocalization](GenomicSequenceLocalization.md)
 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)
 * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md)
 * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md)
 * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)
 * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md)
 * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)
 * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)
 * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md)
 * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md)
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md)
 * [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md)
 * [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md)
 * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md)
 * [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)
 * [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md)
 * [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md)
 * [SequenceAssociation](SequenceAssociation.md)
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)
 * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
 * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)
 * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToGeneAssociation](VariantToGeneAssociation.md)
 * [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md)
