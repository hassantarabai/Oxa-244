# Oxa-244
The repository include helper scripts used in the Manuscript "Tracing the footprints of blaOXA-244 -producing E. coli: Comprehensive genomic and phenotypic insights from the Czech Republic".

# BHG.py - Bacterial Genome Heatmap Generator

BHG.py is a Python script designed for comparative genomic analysis, specifically to visualize the similarity and distribution of plasmid sequences or genomic regions of interest within bacterial genomes.

## Main Features
- **BLASTn for alignment**: Enables the identification and comparison of genomic regions of interest.
- **Heatmap Visualization**: Generates heatmap for enhanced visualization and analysis of compared genomic regions.
- **Customizable Visualization**: Offers adjustable parameters such as bin size and color scheme to suit various datasets and preferences.

## Requirements
BHG.py requires Python 3.x and BioPython.

Other dependencies include (NumPy, Seaborn, Matplotlib) and NCBI BLAST+ will be downloaded automatically when running the script. 

## Installation
BioPython can be installed using either pip or Conda:

Install BioPython using pip:
```bash
pip install biopython
```

Or with conda:
```
conda install -c conda-forge biopython
```
### Input

The `BHG.py` script operates with the following inputs:

1. **Reference Genome File (FASTA format)**: Path to a reference genomic region/plasmid.

2. **Query Genome Files (FASTA format)**: Path to a folder containing query genome files.

3. **Bin Size**: Defines the bin size.

4. **Y-axis Bin Height (1-10)**: Height of bins on the Y-axis of the heatmap.

5. **Color Scheme for Heatmap**: Color scheme for the heatmap.

### Output

**Heatmap Image**: A heatmap is saved in both JPG and SVG formats in the specified output directory. This image visually represents the similarity of the query genomes to the reference genome, segmented according to the specified bin size.


### Run with

```bash
python BHG.py
```

# BHG_ordered.py

`BHG_ordered.py` add a functionality to the `BHG.py` script by providing the ability to order genomes on the heatmap according to a user-provided list.

### Run with

```bash
python BHG_ordered.py
```
