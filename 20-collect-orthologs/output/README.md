This folder contains all the output data to identify putative homologys in the 332 yeast genomes from Shen et al 2018 (PMID: 30415838) and the some exploratory analysis

# blastp_results directory
The blast database was generated from the .fasta files downloaded from the paper's Figshare site - https://figshare.com/articles/dataset/Tempo_and_mode_of_genome_evolution_in_the_budding_yeast_subphylum/5854692
The query sequence is stored S288C_YFR034C_PHO4_protein.fsa and contains a single sequence for ScPho4
I then blasted it agaisnt the entire 332 taxa_proteins.fasta using 1e and 1e-5 

# Content
| Filename | Content | Comment |
|----------|---------|---------|
| 20231205-blastp-343-1e-5-output.csv | blastp result using 1e-5 as cutoff |stringent, 298 single hits per species, no hits = 45  |
| 20231205-blastp-343-1e1-output.csv | blastp result using 1 as E-value cutoff |less stringent 367 hits, 303 single hits, 30 > 1 hit,no hit= 13 |

# File headers
The results -out in a .asn format and were formatted using blast_formatter with the following sseqid qcovs qstart qend slen sstart send qcovshsp pident mismatch evalue and -out .txt

- sseqid: Subject sequence ID. This is the identifier of the sequence in the subject database that the query sequence aligned with.
- qcovs: Query coverage per subject. It represents the percentage of the query sequence that is covered by the alignment with the subject sequence.
- qstart: Start position of the alignment on the query sequence.
- qend: End position of the alignment on the query sequence.
- slen: Length of the subject sequence.
- sstart: Start position of the alignment on the subject sequence.
- send: End position of the alignment on the subject sequence.
- qcovshsp: Query coverage per high-scoring pair. It represents the percentage of the query sequence that is covered by the high-scoring pair.
- pident: Percentage of identical matches. It represents the percentage of nucleotides or amino acids in the alignment that are identical between the query and subject sequences.
- mismatch: Number of mismatches in the alignment.
- evalue: E-value, or Expectation value. It represents the expected number of chance matches with a similar or better score that could occur in the database by random chance

#The blastp with 1e1 303 single hits, 30 > 1 hit, no hit= 13 were used for downstream explorative analysis  

# mult_seq_align directory  
Multisequence alignment were performed using Probcons with 500 interations, MAFFT, and MUSCLE. The results were visualized in jalview. Species showed conservation in the bHLH DNA binding domain, with large sequence divergence as expected 
# Content
| Filename | Content | Comment |
|----------|---------|---------|
| 20240108-343taxa-protein-homologs-mult-seq-align-Probcons.fasta|Probcons multisequence alignment||
| 20240107-343taxa-protein-homologs-multiseq-align.jvp| jalview file of 303 hit||
| 20240108-343taxa-protein-homologs-mult-seq-align-MAFFT.fasta | MAFFT multisequence alignment| |
| 20240108-343taxa-protein-homologs-mult-seq-align-MUSCLE.fasta  |MUSCLE multisequence alignment| |

# 343taxa-IDR-prediction
An explorative disorder content prediction was performed using RAPID. Some large sequences >1000 aa with low disorder content were explored. In addition all sequences with disroder content <40% were explored. PSIPRED secondary structure prediction and DISOPRED3 disorder prediction revealed other conserved domains in addition to the Ph04 bHLH DBD. This informed the next steps to perform hmmssearch and hmmscan against the Pfam data base to possibly detect these other domains.
# Content
| Filename | Content | Comment |
|----------|---------|---------|
| 20240101-343taxa-protein-homologs-seqlenght-RAPID-disord.csv| RAPID % disorder content prediction ||
| 20240108-343taxa-protein-homolog-IDR-UIPRED.fasta| UIPRED IDR prediction in .fas||
| 20240108-343taxa-protein-homolog-IDR-jronn.fasta| Jronn IDR prediction in .fas| |
|20240121-343taxa-protein-PSIPRED4-DISOPRED3-diord-less than 40 |RAPID IDR prediction <40%|further checked in PSIPRED DISOPRED3 |
|20240121-343taxa-protein-RAPID-diord-less40-phytree.png| tree of predicted less diord sequences||
|20240121-343taxa-protein-RAPID-diord-less40.fasta| .fas files of predicted less diord sequences||

# bHLH_hmmsearch_results 

The hmmsearch/scan searches a profile against a sequence database. We sort to confirm if all the .fas sequence contain the PF00010.hmm (Pho4 bHLH)/Pfam database domain as quality control 
Putative curated ScPho4 orthologs against Pfam using HMMER and checks for the presence of the S. cerevisiae Pho4 bHLH domain, as well as returns any other hits, respectively. .sh assumes that hmmer has beeen installed locally, if not check http://eddylab.org/software/hmmer/Userguide.pdf Also, the Pfam data base has been downloaded and hmmpress to create binary files for hmmscan 
Pho4_ortholog exploration.Rmd. Contains all the R code used in     processing the out data
# Content
| Filename | Content | Comment |
|----------|---------|---------|
| 20240117-hmmsearch-bHLH-in-Pho4-blast-hits.txt| 303 blastp hits hmmsearch using bHLH 1e-3|3 seq dropped out|
| 20240117-hmmsearch-bHLH-in-Pho4-blast-hits-clean. csv| tidied data|300 hits bHLH | |
|20240124_hmmscan_Pfam_Pho4_blast_hits.txt | hmmscan 303 hits against Pfam, 1e-3| 231 single bHLH, 54>1, no other Pfam, 13 bHLH, other Pfam|
|20240124_hmmscan_Pfam_Pho4_Blast_hits_clean.csv| tidied data||
|20240205_hmmscan_Pfam_30blastp_hitsgrt1seq_raw.txt| hmmscan blastp hits species >1 Pho4 seq|flagged for further investigation, Pho4 established as a single copy gene|
|20240205_hmmscan_Pfam_30blastp_hitsgrt1seq_clean.csv| tidied data| | 

All exploratory analysis can be replicated using files and codes in the script directory. 


