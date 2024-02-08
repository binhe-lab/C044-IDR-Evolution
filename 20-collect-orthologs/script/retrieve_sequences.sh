
#!/bin/bash                           
# author: Joshua Ayelazuno
# date: 12-11-2023
# title: .sh to retrieve .fas of Pho4 blastp homologs from the 332 yeast genomes from Shen et al 2018 (PMID: 30415838)
# use:retrive_sequences.sh
#########################
input_csv="blast_hit_grt1_seqnames.csv" # file containing the names of species and sequence identifiers only                                                 
fasta_file="343taxa_proteins.fasta"
output_folder="/Users/jayelazuno/Desktop/Pho4_orthologs /orthomcl_output/cd"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Read each line of the CSV file and perform the search
while IFS=, read -r Species seq_identifier; do
    # Concatenate species and seq_identifier with "@" to form the search string
    search_string="${Species}@${seq_identifier}"

    # Define the output file name
    output_file="${output_folder}/${species}_${seq_identifier}.fas"

    # Perform the search and save the result to the output file
    grep -A 1 -wF ">${search_string}" "$fasta_file" > "$output_file"

    # Print a message indicating the completion of the search for each sequence
    echo "Retrieved sequence for: ${species}_${seq_identifier}"
done < "$input_csv"