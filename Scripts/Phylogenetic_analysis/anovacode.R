rm(list=ls())
getwd()
#library(ape)
#library(geiger)
#library(phytools)

file_name=readline(prompt="Ener file name: ") #enter file name
mol_feats_data<-read.csv(file_name, header=TRUE, stringsAsFactors=TRUE) #assign file content to variable
mol_feats_data
mol_feats_df<-data.frame(mol_feats_data[1:21,], stringsAsFactors = True) #make the file into a data frame excluding rows on the file which should not be used in analysis
mol_feats_df
row.names(mol_feats_df)<-mol_feats_df$Species
mol_feats_df

#Read in tree data and make rooted and dichromous
#Tree_data<-ape::read.tree(text='((YALI0F05126g1_1_PHO4_Protein__Yarrowia_lipolytica_:1.857129,(XP_458014_2_DEHA2C07656p__Debaryomyces_hansenii_CBS767_:0.153091,(XP_049262169_1_PHO4___Candida__subhashii_:0.186861,AFA36294_1_PHO4_protein__Candida_albicans_:0.384033):0.24962):0.76444):0.42699,((SAKL0F07392g1_1_PHO4_Protein__Lachancea_kluyveri_:0.251054,QEU60988_1_Pho4__Kluyveromyces_lactis_:0.300142):0.017606,(((((((((QID84820_1_phosphate_sensing_transcription_factor__Saccharomyces_pastorianus_:0.005033,CAI1973783_1_hypothetical_protein_SEUBUCD650_0F00940__Saccharomyces_eubayanus_:0.000422):0.039353,EJT41994_1_PHO4_like_protein__Saccharomyces_kudriavzevii_IFO_1802_:0.009523):0.008653,EJS43866_1_pho4p__Saccharomyces_arboricola_H_6_:0.030823):0.02769,QHB08372_1_Pho4__Saccharomyces_cerevisiae_:0.007775):0.011486,XP_033766099_1_Pho4__Saccharomyces_paradoxus_:0.004073):0.222529),XP_003676616_1_hypothetical_protein_NCAS_0E01860__Naumovozyma_castellii_CBS_4309_:1.344686):0.092661,((BN121_CACA0s05e10208g1_1_PHO4_Protein__Nakaseomyces_castellii_:0.529461,BN123_NABA0s03e02948g1_1_PHO4_Protein__Nakaseomyces_bacillisporus_:0.364638):0.11897,(((BN122_CANI0s08e01177g1_1_PHO4_Protein__Nakaseomyces_nivariensis_:0.067468,BN124_NADE0s12e00990g1_1_PHO4_Protein__Nakaseomyces_delphensis_:0.069615):0.006272,BN119_CABR0s16e03993g1_1_PHO4_Protein__Nakaseomyces_bracarensis_:0.068697):0.111579,UCS35305_1_PHO4___Candida__glabrata_:0.235527):0.303645):0.103684):0.13248,LAWA0B04082g1_1_PHO4_Protein__Lachancea_waltii_:0.330133):0.027239):0.108783,AQZ14724_1_PHO4__YFR034C___Zygosaccharomyces_parabailii_:0.184308);')
Tree_data<-ape::read.tree(text='((Y_lipolytica:1.857129,(D_hansenii:0.153091,(C_subhashii:0.186861,C_albicans:0.384033):0.24962):0.76444):0.42699,((L_kluyveri:0.251054,K_lactis:0.300142):0.017606,(((((((((S_pastorianus:0.005033,S_eubayanus:0.000422):0.039353,S_kudriavzevii:0.009523):0.008653,S_arboricola:0.030823):0.02769,S_cerevisiae:0.007775):0.011486,S_paradoxus:0.004073):0.222529),Nm_castellii:1.344686):0.092661,((Nk_castellii:0.529461,N_bacillisporus:0.364638):0.11897,(((N_nivariensis:0.067468,N_delphensis:0.069615):0.006272,N_bracarensis:0.068697):0.111579,C_glabrata:0.235527):0.303645):0.103684):0.13248,L_waltii:0.330133):0.027239):0.108783,Z_parabailii:0.184308);')
is.rooted(Tree_data)
outgroup<-c("Y_lipolytica", "D_hansenii", "C_subhashii", "C_albicans")
Tree_root<-ape::root(Tree_data, outgroup, resolve.root=TRUE)
is.rooted(Tree_root)
Tree_data_1<-multi2di(Tree_root, random=FALSE)
is.rooted(Tree_data_1)
tree_data_2<-collapse.singles(Tree_data_1)
balance(tree_data_2)
is.rooted(tree_data_2)
plot(tree_data_2)

#make a linear model and runs an anova of a molecular feature with the variable being if the species is Pho2 indendent or dependent (Group) RUNS
mol_feats_model<-lm(REP_Q2 ~ Group, data=mol_feats_df)
anova_results<-anova(mol_feats_model)
anova_results
#Phylogenetic anova x is grouping variable y is continous variable
print(mol_feats_df$REP_Q2)
print(tree_data_2$tip.label)
print(row.names(mol_feats_df))
tip.label and row.names appear to be the same
phyloanova<-phylANOVA(tree_data_2, mol_feats_df$Group, mol_feats_df$REP_Q2, nsim=1000, posthoc=TRUE, p.adj="holm")
phyloanova #Warning no labels for x and y #Error in pic(y, multi2di(tree, random = FALSE)) : 
  NA/NaN/Inf in foreign function call (arg 4)

#variables<-colnames(mol_feats_data) #not in use
#variables
#loop to run through column names (molecular features) and create a linear model and run an anova for each based on the group (dependent or independent) FAILS
for(i in 3:ncol(mol_feats_df)){
  print(as.factor(colnames(mol_feats_df)[i])) #Print REP_Q2
  #variable_fact<-as.factor(colnames(mol_feats_df)[i])
  #variable_fact
  mol_feats_model<-lm(as.factor(colnames(mol_feats_df)[i]) ~ Group, data=mol_feats_df) #Error variable lengths differ (found for 'Group')
  #mol_feats_model
  #anova_results<-anova(mol_feats_model)
  }
#anova_results

# Bin's suggestion
res <- lapply(mol_feats_df[,3:ncol(mol_feats_df)], function(x){
  mol_feats_model<-lm(x ~ mol_feats_df$Group)
})
