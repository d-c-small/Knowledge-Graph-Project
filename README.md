# Knowledge Graph from Text

Build an interactive, queryable knowledge graph from a Wikipedia article using NLP — covering entity recognition, coreference resolution, relationship extraction, and graph visualization.

---

## Overview

A knowledge graph concentrates information in a compact, connected form that makes it easy to retrieve and reason over. This project pulls a Wikipedia article, processes the raw text through a full NLP pipeline, extracts subject–predicate–object triples, and assembles them into a directed graph that can be explored visually and queried programmatically.

The article used in this project is the **New York** Wikipedia page. All text processing is handled by [spaCy](https://spacy.io/), graph construction by [NetworkX](https://networkx.org/), and interactive visualization by [pyvis](https://pyvis.readthedocs.io/).

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
Coreference Resolution            — replace pronouns with their referents
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
| [`spaCy`](https://spacy.io/) (`en_core_web_lg`) | Tokenization, part-of-speech tagging, named entity recognition |
| [`spacy-transformers`](https://spacy.io/usage/embeddings-transformers) | Transformer-based model support for spaCy pipelines |
| [`coreferee`](https://github.com/msg-systems/coreferee) | Coreference resolution — resolve pronouns to their noun referents |
| [`NetworkX`](https://networkx.org/) | Construct and query a directed graph from extracted triples |
| [`pyvis`](https://pyvis.readthedocs.io/) | Render the NetworkX graph as an interactive HTML visualization |
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

- Python 3.8+
- Jupyter Notebook or JupyterLab

### Install Dependencies

```bash
pip install wikipedia spacy spacy-transformers networkx pyvis coreferee
```

Download the required spaCy language model:

```bash
python -m spacy download en_core_web_lg
```

Install the coreferee model for English:

```bash
python -m coreferee install en
```

### Run the Notebook

```bash
jupyter notebook Exercise.ipynb
```

Run all cells in order. The graph will be saved as an HTML file and rendered inline in the notebook.

---

## How It Works

### Task 1 — Import Libraries
All required libraries are imported: `wikipedia`, `spacy`, `coreferee`, `networkx`, `pyvis`, and `re`.

### Task 2 — Load the Data
The Wikipedia API is used to fetch the full text content of the **New York** article in English. The raw content is stored as a string for downstream processing.

### Task 3 — Preprocess the Data
The raw text is cleaned: converted to lowercase, newlines removed, punctuation stripped, and content inside parentheses, section headings (`==...==`), and everything after the "See Also" heading is removed using regular expressions.

### Task 4 — Recognize Named Entities
spaCy's `en_core_web_lg` model processes the cleaned text and identifies named entities (people, locations, organizations, etc.), which are rendered with `displacy` for visual inspection.

### Task 5 — Compute Coreference Clusters
The `coreferee` component is added to the spaCy pipeline. It identifies coreference chains — groups of expressions that refer to the same real-world entity (e.g., "New York" → "the city" → "it").

### Task 6 — Resolve Coreferences
Each token in the document is checked against the coreference chains. Pronouns and referring expressions are replaced with their resolved noun phrase referents, producing cleaner, more explicit text for relationship extraction.

### Task 7 — Extract Relationships
A custom function iterates over sentences and uses spaCy's noun chunk detection to extract the first and last noun phrases as the **subject** and **object**, with the text in between serving as the **predicate**. This yields subject–predicate–object triples.

### Task 8 — Create a Graph
A directed `NetworkX` graph is built from the extracted triples — nodes represent entities and edges represent the relationships between them. The graph is then passed to `pyvis` to generate an interactive HTML visualization where edges are labeled with the predicate text.

### Task 9 — List the Related Entities
The NetworkX graph is queried to extract information. Given a node (entity), all neighboring nodes — i.e., entities directly related to it — can be retrieved.

---

## Example Query

After building the graph, you can extract related entities for any node:

```python
# Find all entities directly related to "manhattan"
print(nx_graph.edges(['manhattan']))
```

This returns all outgoing edges from the `manhattan` node, revealing the entities and relationships the graph has extracted for that subject.

---

## Source

This project was completed as part of the **[educative.io](https://www.educative.io/)** guided project:  
*"Create a Knowledge Graph from Text"*
