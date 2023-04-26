
# Slot: object


the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as a proxy for the gene or vice versa.

URI: [biolink:gene_to_gene_association_object](https://w3id.org/biolink/gene_to_gene_association_object)


## Domain and Range

[GeneToGeneAssociation](GeneToGeneAssociation.md) &#8594;  <sub>1..1</sub> [GeneOrGeneProduct](GeneOrGeneProduct.md)

## Parents

 *  is_a: [object](object.md)

## Children

 *  [gene to gene homology association➞object](gene_to_gene_homology_association_object.md)
 *  [pairwise molecular interaction➞object](pairwise_molecular_interaction_object.md)

## Used by

 * [GeneToGeneAssociation](GeneToGeneAssociation.md)
 * [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md)
 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Local names:** | | descriptor (ga4gh) |
|  | | node with incoming relationship (neo4j) |
| **Mappings:** | | rdf:object |
| **Exact Mappings:** | | owl:annotatedTarget |
|  | | OBAN:association_has_object |

