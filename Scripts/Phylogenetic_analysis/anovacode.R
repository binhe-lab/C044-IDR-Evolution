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
#make a linear model and runs an anova of a molecular feature with the variable being if the species is Pho2 indendent or dependent (Group) RUNS
mol_feats_model<-lm(REP_Q2 ~ Group, data=mol_feats_df)
anova_results<-anova(mol_feats_model)
anova_results

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
