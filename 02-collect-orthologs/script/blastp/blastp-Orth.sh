#!/bin/bash
#title: blastp to identify putative Pho4 homologs in the 332 yeast genomes from Shen et al 2018 (PMID:30415838)
# date: 2023-11-30
# author: Joshua Ayelazuno
##################

# blastp (assumes the blastp package has been installed locally)
blastp -query S288C_YFR034C_PHO4_protein.fsa -subject 343taxa_proteins.fasta -evalue 1e-5 -outfmt 11 -out blastp_results/results.asn
# -db_gencode 12: yeast alternative genetic code table when we use the tblastn program
# -evalue 1e-160: based on the result, this is the cutoff that will only include the orthologs for XP_028889033
# -seg "no"     : turn off query masking
# -max_hsps 2   : show only top 2 high scoring pair per subject sequence
# -num_threads 4: use 4 threads
# -outfmt 11    : BLAST achive, can be later converted to other formats
echo "blastp search complete"

# reformat
echo "reformatting..."
blast_formatter -archive blastp_results/results.asn -outfmt "7 sseqid qcovs qstart qend slen sstart send qcovshsp pident mismatch evalue" -out blastp_results/results.txt
echo "done"
################
## clean the Blastp output files  
blastp_result_txt <- read_tsv("~/Desktop/Pho4_orthologs /orthomcl_output/blastp_results/blastp_results.txt",comment = "#", col_names = FALSE, show_col_types = FALSE  )
blastp_result<- blastp_result_txt %>%
  rename(Species = X1, QCoverage = X2, QStart = X3, QEnD = X4, SLength = X5, SStart = X6, SEnd = X7, Identity = X8, Mismatches = X9, EValues = X10)
blastp_results2  <- separate(blastp_result, Species, into = c("Species", "seq_identifier"), sep = "@")
folder_path <- "/Users/jayelazuno/Desktop/Pho4_orthologs /orthomcl_output/blastp_results/"
write_csv(blastp_results2, paste0(folder_path, "output_table.csv"))
write_xlsx(blastp_results2, paste0(folder_path, "output_table.xlsx"))
