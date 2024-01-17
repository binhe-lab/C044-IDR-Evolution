# title: use hmmsearch to identify bHLH in candidate Pho4 orthologs
# author: Bin He
# date: 2024-01-07

# assumes hmmer is installed. if not, try `conda`

today=`date +"%Y%m%d"`

hmmsearch \
	-o ${today}-hmmsearch.log \
	--domtblout ../output/bHLH_hmmsearch_result/${today}-hmmsearch-bHLH-in-Pho4-blast-hits.txt \
	--noali \
	--domE 1e-3 \
	../input/bHLH_profile/PF00010.hmm \
	../output/Pho4-Homologs-fas/20231212-343taxa-proteins-homologs.fas

# -o: output log file, this redirects the output on the screen to a file
# --domtblout: output a simpler and parsable table output with one row per domain hit
# --noali: don't output the alignment to make the output more readable
# --domE: domain E value cutoff
# last two rows are the HMM profile and the sequence to be searched
