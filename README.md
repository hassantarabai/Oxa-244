# Oxa-244
The repository include helper scripts used in the Manuscript "Tracing the footprints of blaOXA-244 -producing E. coli: Comprehensive genomic and phenotypic insights from the Czech Republic"

# BHG.py - Bacterial Genome Heatmap Generator

BHG.py is a Python script designed for comparative genomic analysis, specifically to visualize the similarity and distribution of plasmid sequences or genomic regions of interest within bacterial genomes.

## Main Features
- **BLASTn for alignment**: Enables the identification and comparison of genomic regions of interest.
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
### Input

The `BHG.py` script operates with the following inputs:

1. **Reference Genome File (FASTA format)**: The user is prompted to enter the path to a reference genome file. This file should be in FASTA format and serves as the base for comparison against query sequences.

2. **Query Genome Files (FASTA format)**: The user is also asked to specify the path to a folder containing query genome files in FASTA format. These genomes are compared to the reference genome to assess similarity.

3. **Bin Size**: Through a prompt, the user defines the bin size, which dictates how the reference genome is segmented for comparison purposes. This size affects the resolution of the heatmap visualization.

4. **Y-axis Bin Height (1-10)**: This input allows the user to control the height of each bin on the Y-axis of the heatmap, affecting the visual representation of the data.

5. **Color Scheme for Heatmap**: The user selects a color scheme for the heatmap visualization, impacting the aesthetic and readability of the output.

### Output

The script generates a heatmap visualization, providing a comparative analysis of the query genomes against the reference. Specifically, the outputs include:

1. **Heatmap Image**: A heatmap is saved in both JPG and SVG formats in the specified output directory. This image visually represents the similarity of the query genomes to the reference genome, segmented according to the specified bin size.

2. **Terminal Output**: Throughout its execution, the script prints status messages to the terminal, including notifications of the BLAST process for each query genome and any critical errors or warnings encountered.

### Example Command

To run the script, navigate to its directory and execute it via the command line, following the interactive prompts to input the required paths and parameters:

```bash
python BHG.py
