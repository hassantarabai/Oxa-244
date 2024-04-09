# Oxa-244
The repository include helper scripts used in the Manuscript "Tracing the footprints of blaOXA-244 -producing E. coli: Comprehensive genomic and phenotypic insights from the Czech Republic"

# BHG.py - Bacterial Genome Heatmap Generator

BHG.py is a Python script designed for comparative genomic analysis, specifically to visualize the similarity and distribution of plasmid sequences within bacterial genomes. It utilizes **BLASTn** for sequence alignment and employs heatmaps for sequence alignment and employs heatmaps for intuitive visualization of genomic identity percentages across multiple genomes within set bins representing distinct segments of the reference genome.

## Key Features
- **BLASTn Integration**: Leverages BLASTn for alignment, enabling the identification and comparison of specific genomic regions.
- **Heatmap Visualization**: Utilizes heatmaps to provide a clear, visual representation of sequence similarity, enhancing comparative genomic analysis.
- **Customizable Visualization**: Offers adjustable parameters such as bin size and color scheme to suit various datasets and preferences.

## Requirements
BHG.py requires Python 3.x and BioPython, along with few other Python libraries including NumPy, Seaborn, and Matplotlib for data manipulation and visualization. The script also requires the NCBI BLAST+ command line tools for sequence alignment.

Other dependencies (NumPy, Seaborn, Matplotlib) and NCBI BLAST+ will need to be installed, but are commonly included in scientific Python distributions or easily installable via pip.

## Installation
Ensure Python 3 is installed on your system. BioPython can be installed using either pip or Conda, depending on your preference and environment.

Install BioPython using pip:

```bash
pip install biopython

Or, using conda:
conda install -c conda-forge biopython
