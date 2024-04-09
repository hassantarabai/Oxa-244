# Oxa-244
The repository include helper scripts used in the Manuscript "Tracing the footprints of blaOXA-244 -producing E. coli: Comprehensive genomic and phenotypic insights from the Czech Republic"

# BHG.py - Bacterial Genome Heatmap Generator

BHG.py is a Python script designed for comparative genomic analysis, specifically to visualize the similarity and distribution of plasmid sequences or genomic regions of interest within bacterial genomes.

## Main Features
- **BLASTn for alignment**: Enables the identification and comparison of specific genomic regions.
- **Heatmap Visualization**: Generates heatmap for enhanced visualization and analysis of compared genomic regions.
- **Customizable Visualization**: Offers adjustable parameters such as bin size and color scheme to suit various datasets and preferences.

## Requirements
BHG.py requires Python 3.x and BioPython.

Other dependencies include (NumPy, Seaborn, Matplotlib) and NCBI BLAST+ will be downloade dautomatically when running the script. 

## Installation
BioPython can be installed using either pip or Conda:

Install BioPython using pip:
```bash
pip install biopython
```

Or using conda:
```
conda install -c conda-forge biopython
```
