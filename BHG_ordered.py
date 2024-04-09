import os
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def perform_blast(reference, query):
    cline = NcbiblastnCommandline(query=query, subject=reference, outfmt=6)
    stdout, stderr = cline()
    return stdout

def parse_blast_output(blast_output, bin_size, ref_length):
    num_bins = ref_length // bin_size + (1 if ref_length % bin_size != 0 else 0)
    identity_array = np.full(num_bins, np.nan)  # Use NaN for bins with no alignment
    lines = blast_output.strip().split('\n')
    for line in lines:
        parts = line.split('\t')
        start, end = int(parts[8]), int(parts[9])
        identity = float(parts[2])
        for i in range(start // bin_size, min((end // bin_size) + 1, num_bins)):
            identity_array[i] = max(identity_array[i], identity) if not np.isnan(identity_array[i]) else identity
    return identity_array

if __name__ == '__main__':
    reference_fasta = input("Enter the path to the reference fasta: ")
    input_folder = input("Enter the path to the folder with fasta genomes for comparison: ")
    genome_ids_file = input("Enter the path to the file with genome IDs: ")
    output_folder = input("Enter the path to the output folder: ")
    bin_size = int(input("Enter bin size: "))
    y_bin_height = float(input("Enter Y-axis bin height (1-10): "))
    color_map = input("Enter the color for the heatmap (e.g., Blues, Greens_r, viridis, winter): ")

    with open(genome_ids_file, 'r') as f:
        ordered_genome_filenames = [line.strip() for line in f.readlines()]

    fasta_files_ordered = [os.path.join(input_folder, filename) for filename in ordered_genome_filenames]
    heatmap_data = []
    y_labels = [os.path.splitext(os.path.basename(filename))[0] for filename in ordered_genome_filenames]

    for file in fasta_files_ordered:
        print(f"Performing BLAST for {os.path.basename(file)} against reference")
        blast_output = perform_blast(reference_fasta, file)
        with open(reference_fasta, 'r') as ref_fasta:
            for reference_record in SeqIO.parse(ref_fasta, "fasta"):
                ref_length = len(reference_record.seq)
                identities = parse_blast_output(blast_output, bin_size, ref_length)
                heatmap_data.append(identities)

    heatmap_data = np.array(heatmap_data)
    ref_length = len(SeqIO.read(reference_fasta, "fasta").seq)

    # Adjusting x-axis labels to start from the beginning
    x_labels_positions = np.arange(0, ref_length, bin_size)
    x_labels = [str(int(label)) for label in x_labels_positions]

    # Plotting with seaborn
    plt.figure(figsize=(10, len(fasta_files_ordered) * y_bin_height / 10))
    ax = sns.heatmap(heatmap_data, cmap=color_map, vmin=0, vmax=100, yticklabels=y_labels, xticklabels=x_labels, cbar_kws={'label': 'Identity %'})
    ax.set_xticks(np.linspace(0, len(heatmap_data[0]) - 1, len(x_labels)))  # Adjust x-ticks to match positions
    ax.set_xticklabels(x_labels, rotation=45)

    plt.title('Genome Identity Heatmap')
    plt.xlabel('Genome Position')
    plt.ylabel('Genome')
    plt.tight_layout()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    plt.savefig(os.path.join(output_folder, 'heatmap.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(output_folder, 'heatmap.svg'), bbox_inches='tight')
    plt.show()
