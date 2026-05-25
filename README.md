# Hybrid Search Retrieval Lab

Experimentation repo for hybrid retrieval patterns using Azure AI Search BM25, Pinecone vector search, BERT re-ranking, freshness boosting, and metadata-aware ranking.

## Retrieval Pipeline

1. Normalize documents and attach metadata
2. Create semantic chunks with overlap
3. Index lexical fields in Azure AI Search
4. Embed chunks into Pinecone
5. Retrieve top candidates from BM25 and vector search
6. Merge, deduplicate, and re-rank with BERT
7. Apply freshness, effective-date, and section weights
8. Return cite-ready context blocks

## Ranking Features

- BM25 lexical relevance
- Vector similarity
- Section priority
- Effective-date freshness
- Jurisdiction match
- Source authority
- Near-duplicate collapse
- Context-window budget score

## Metrics

Recall@k · nDCG · MRR · source diversity · duplicate rate · context token count · answer faithfulness
