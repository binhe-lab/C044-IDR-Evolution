20231212-343taxa-proteins-homologs.fas This folder contains single Pho4 blastp hit .fas sequence/ single blastp hits with a single bHLH domain which were retrieved from the Shen et al 2018 ( (PMID: 30415838). 
The hits were obtained from an already orthomcl_out reciprocal blast file used in the genome assembly file containing the fasta sequences.
The hits were filtered for seqeunces with a single hit and using the species_name@seq_identifier, were retrieved using the retrive_sequences.sh script
The hits were filtered for seqeunces with a single hit and using the species_name@seq_identifier, were retrieved using the retrive_sequences.sh script, located under scripts
These .fas sequence will be used for further analysis to explore the evolution of ScPho4 protein
A hmmscan (details in script dir) was performed 231 blastp hits also had a single hmmscan bHLH hits
20240201-54species-grt-1bHLH.txt is a subset 20231212-343taxa-proteins-homologs.fas, from hmmscan which returned > 1 bHLH domain hits and no other pfam hits. Upon domain examination, of domain architecture, these were added back to 20231212-343taxa-proteins-homologs.fas making 285 core species  
20241212_blast_hitsseq_grtq.fasta - blastp hits, where a single species had more than 1 Ph04 hit sequences. 
