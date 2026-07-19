# Knowledge Graph from Text

Build an interactive, queryable knowledge graph from a Wikipedia article using NLP — covering entity recognition, entity normalization, relationship extraction, and graph visualization.

---

## Overview

A knowledge graph concentrates information in a compact, connected form that makes it easy to retrieve and reason over. This project pulls a Wikipedia article, processes the raw text through a full NLP pipeline, extracts subject–predicate–object triples, and assembles them into a directed graph that can be explored visually and queried programmatically.

The article used in this project is the **New York** Wikipedia page. All text processing is handled by [spaCy](https://spacy.io/), graph construction by [NetworkX](https://networkx.org/), and interactive visualization by [pyvis](https://pyvis.readthedocs.io/).

---

## Skills Demonstrated

- End-to-end NLP pipeline design (data ingestion, preprocessing, entity extraction, relationship extraction)
- Practical graph engineering with directed graphs and labeled edges using NetworkX
- Resilient data engineering with multi-stage fetch fallbacks for restricted network environments
- NLP quality improvements through entity normalization and pronoun-link filtering
- Interactive data product delivery by exporting a browser-ready graph visualization
- Query design for machine consumption (neighbors, paths, centrality, and filtered relationships)

---

## Technical Problems Solved

- Replaced a legacy coreference dependency with a Python 3.14-compatible normalization strategy
- Added robust article-loading fallbacks to keep notebook execution stable when external APIs fail
- Improved triple quality by filtering ambiguous pronoun-only subject/object candidates
- Standardized graph output to a local UTF-8 HTML artifact for cross-environment portability
- Structured the project for reproducibility with pinned dependencies and environment templates

---

## Applications & Use Cases

Knowledge graphs turn raw text into a structured, machine-queryable network. Once built, this graph enables a wide range of downstream applications:

| Use Case | Description |
|---|---|
| **Question Answering** | Query the graph to answer "what is related to X?" — instantly surface all entities and relationships connected to any node |
| **Semantic Search** | Navigate relationship neighborhoods to find conceptually linked entities beyond simple keyword matching |
| **Knowledge Base Reasoning** | Trace multi-hop paths between entities to answer complex questions (e.g., "how is Brooklyn connected to Wall Street?") |
| **Fact Verification** | Check whether a specific subject–predicate–object relationship exists in the extracted knowledge |
| **Recommendation** | Surface related entities for a given node to power content or topic recommendations |
| **Graph-based ML** | Use graph structure, centrality scores, and node embeddings as features for downstream machine learning models |
| **API / Service Backend** | Expose the graph as a queryable REST or GraphQL endpoint to drive external applications |

---

## Graph Preview

> **Open `Knowledge_Graph.html` in a browser** to explore the fully interactive graph — hover over edges to read relationship labels, and click nodes to highlight their neighborhood.

<!-- TODO: Add a screenshot of the graph here -->
<!-- Example: ![Knowledge Graph Preview](screenshot.png) -->

---

## Pipeline

```
Wikipedia API
     │
     ▼
Preprocessing          — lowercase, strip punctuation, headings, parentheses
     │
     ▼
Named Entity Recognition (NER)    — identify people, places, organizations
     │
     ▼
Entity Alias Mapping              — normalize entity mentions to canonical forms
     │
     ▼
Pronoun Filtering                 — drop ambiguous pronoun-only links
     │
     ▼
Relationship Extraction           — extract subject–predicate–object triples
     │
     ▼
Graph Construction                — build a directed graph (NetworkX)
     │
     ▼
Interactive Visualization         — render as an HTML graph (pyvis)
     │
     ▼
Query / Information Extraction    — interrogate the graph for related entities
```

---

## Tech Stack

| Library | Purpose |
|---|---|
| [`wikipedia`](https://pypi.org/project/wikipedia/) | Fetch Wikipedia article content via the MediaWiki API |
| [`spaCy`](https://spacy.io/) (`en_core_web_sm` or larger) | Tokenization, part-of-speech tagging, noun chunking, named entity recognition |
| [`NetworkX`](https://networkx.org/) | Construct and query a directed graph from extracted triples |
| [`pyvis`](https://pyvis.readthedocs.io/) | Render the NetworkX graph as an interactive HTML visualization |
| [`requests`](https://pypi.org/project/requests/) | Fallback article retrieval when the Wikipedia wrapper/API is unavailable |
| `re` | Regex-based text cleaning during preprocessing |

---

## Project Structure

```
Knowledge-Graph-Project/
├── Exercise.ipynb        # Main notebook — full pipeline from data fetch to graph query
└── Knowledge_Graph.html  # Pre-rendered interactive knowledge graph (open in browser)
```

---

## Getting Started

### Prerequisites

- Python 3.14+ (tested)
- Jupyter Notebook or JupyterLab

### Install Dependencies

```bash
pip install -r requirements.txt
```

If you are installing manually instead of using `requirements.txt`, install at least:

```bash
pip install wikipedia requests spacy networkx pyvis
python -m spacy download en_core_web_sm
```

### Run the Notebook

```bash
jupyter notebook Exercise.ipynb
```

Run all cells in order. The graph will be saved as an HTML file and rendered inline in the notebook.

---

## How It Works

### Task 1 — Import Libraries
All required libraries are imported: `wikipedia`, `requests`, `spacy`, `networkx`, `pyvis`, and `re`.

### Task 2 — Load the Data
The notebook first tries the Wikipedia wrapper API to fetch the **New York** article, then falls back to a direct MediaWiki REST request, and finally uses a built-in fallback paragraph if both network calls fail. This keeps the pipeline runnable in restricted environments.

### Task 3 — Preprocess the Data
The raw text is cleaned: converted to lowercase, newlines removed, punctuation stripped, and content inside parentheses, section headings (`==...==`), and everything after the "See Also" heading is removed using regular expressions.

### Task 4 — Recognize Named Entities
spaCy processes the cleaned text and identifies named entities (people, locations, organizations, etc.), which are rendered with `displacy` for visual inspection. The notebook automatically tries `en_core_web_lg`, then `en_core_web_md`, then `en_core_web_sm`.

### Task 5 — Build an Entity Alias Map
Instead of a separate coreference package, the notebook builds a lightweight alias map from spaCy entities to normalize mentions to canonical names (for example, mapping token-level aliases back to full entities).

### Task 6 — Normalize Entities and Filter Pronoun Links
Entity mentions are normalized through the alias map, and pronoun-only subject/object candidates are filtered out. This improves triple quality while staying fully compatible with modern Python and spaCy versions.

### Task 7 — Extract Relationships
A custom function iterates over sentences and uses spaCy noun chunks to extract the first and last noun phrases as the **subject** and **object**, then applies normalization and quality checks before keeping the predicate between them. This yields cleaner subject–predicate–object triples.

### Task 8 — Create a Graph
A directed `NetworkX` graph is built from the extracted triples — nodes represent entities and edges represent the relationships between them. The graph is then passed to `pyvis` to generate an interactive HTML visualization where edges are labeled with the predicate text.

### Task 9 — List the Related Entities
The NetworkX graph is queried to extract information. Given a node (entity), all neighboring nodes — i.e., entities directly related to it — can be retrieved.

---

## Querying the Graph

Once the graph is built, NetworkX exposes a query API. Below are patterns that demonstrate the range of questions the graph can answer programmatically:

```python
# 1. Outgoing relationships — what does this entity connect to?
nx_graph.edges(['manhattan'])

# 2. Incoming relationships — what entities reference this one?
list(nx_graph.predecessors('manhattan'))

# 3. Multi-hop reasoning — shortest path between two entities
nx.shortest_path(nx_graph, source='new york', target='brooklyn')

# 4. Neighborhood subgraph — all nodes within 2 hops of an entity
nx.ego_graph(nx_graph, 'new york', radius=2)

# 5. Most connected entities — centrality analysis
sorted(nx.degree_centrality(nx_graph).items(), key=lambda x: x[1], reverse=True)[:10]

# 6. Predicate filtering — find edges whose relationship contains a keyword
[(u, v, d) for u, v, d in nx_graph.edges(data=True) if 'population' in d.get('title', '')]
```

These patterns cover the core interaction modes used in question answering systems, semantic search, and knowledge base reasoning — see [Applications & Use Cases](#applications--use-cases) for the full breakdown.

---

## Source

This project was completed as part of the **[educative.io](https://www.educative.io/)** guided project:  
*"Create a Knowledge Graph from Text"*
