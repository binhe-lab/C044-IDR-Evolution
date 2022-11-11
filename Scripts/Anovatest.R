rm(list=ls())
getwd()
library(dplyr)
library(ape)
#library(geiger)
library(phytools)

file_name=readline(prompt="Ener file name: ")
normal_file<-read.csv("IDR_molecular_features_data_Full_sequence.csv", header=TRUE, sep=',', stringsAsFactors=TRUE)
mol_feats_df1<-data.frame(normal_file[1:21,], stringsAsFactors = TRUE)
mol_feats_df1
mol_feats_data<-read.csv(file_name, header=TRUE, sep=',', stringsAsFactors=TRUE)
mol_feats_data
mol_feats_df<-data.frame(mol_feats_data, stringsAsFactors = TRUE)
mol_feats_df
mol_feats_mat<-data.matrix(mol_feats_data)
mol_feats_mat
row.names(mol_feats_df)<-mol_feats_df$Features
mol_feats_df

#Tree_data<-ape::read.tree(text='((YALI0F05126g1_1_PHO4_Protein__Yarrowia_lipolytica_:1.857129,(XP_458014_2_DEHA2C07656p__Debaryomyces_hansenii_CBS767_:0.153091,(XP_049262169_1_PHO4___Candida__subhashii_:0.186861,AFA36294_1_PHO4_protein__Candida_albicans_:0.384033):0.24962):0.76444):0.42699,((SAKL0F07392g1_1_PHO4_Protein__Lachancea_kluyveri_:0.251054,QEU60988_1_Pho4__Kluyveromyces_lactis_:0.300142):0.017606,(((((((((QID84820_1_phosphate_sensing_transcription_factor__Saccharomyces_pastorianus_:0.005033,CAI1973783_1_hypothetical_protein_SEUBUCD650_0F00940__Saccharomyces_eubayanus_:0.000422):0.039353,EJT41994_1_PHO4_like_protein__Saccharomyces_kudriavzevii_IFO_1802_:0.009523):0.008653,EJS43866_1_pho4p__Saccharomyces_arboricola_H_6_:0.030823):0.02769,QHB08372_1_Pho4__Saccharomyces_cerevisiae_:0.007775):0.011486,XP_033766099_1_Pho4__Saccharomyces_paradoxus_:0.004073):0.222529),XP_003676616_1_hypothetical_protein_NCAS_0E01860__Naumovozyma_castellii_CBS_4309_:1.344686):0.092661,((BN121_CACA0s05e10208g1_1_PHO4_Protein__Nakaseomyces_castellii_:0.529461,BN123_NABA0s03e02948g1_1_PHO4_Protein__Nakaseomyces_bacillisporus_:0.364638):0.11897,(((BN122_CANI0s08e01177g1_1_PHO4_Protein__Nakaseomyces_nivariensis_:0.067468,BN124_NADE0s12e00990g1_1_PHO4_Protein__Nakaseomyces_delphensis_:0.069615):0.006272,BN119_CABR0s16e03993g1_1_PHO4_Protein__Nakaseomyces_bracarensis_:0.068697):0.111579,UCS35305_1_PHO4___Candida__glabrata_:0.235527):0.303645):0.103684):0.13248,LAWA0B04082g1_1_PHO4_Protein__Lachancea_waltii_:0.330133):0.027239):0.108783,AQZ14724_1_PHO4__YFR034C___Zygosaccharomyces_parabailii_:0.184308);')
Tree_data<-ape::read.tree(text='((Y_lipolytica:1.857129,(D_hansenii:0.153091,(C_subhashii:0.186861,C_albicans:0.384033):0.24962):0.76444):0.42699,((L_kluyveri:0.251054,K_lactis:0.300142):0.017606,(((((((((S_pastorianus:0.005033,S_eubayanus:0.000422):0.039353,S_kudriavzevii:0.009523):0.008653,S_arboricola:0.030823):0.02769,S_cerevisiae:0.007775):0.011486,S_paradoxus:0.004073):0.222529),Nm_castellii:1.344686):0.092661,((Nk_castellii:0.529461,N_bacillisporus:0.364638):0.11897,(((N_nivariensis:0.067468,N_delphensis:0.069615):0.006272,N_bracarensis:0.068697):0.111579,C_glabrata:0.235527):0.303645):0.103684):0.13248,L_waltii:0.330133):0.027239):0.108783,Z_parabailii:0.184308);')
Tree_data_2<-ape::read.tree(text='(C_albicans:0.30626966,C_subhashii:0.25744492,(D_hansenii:0.16577512,(Y_lipolytica:1.80943042,(((S_eubayanus:0.00000036,S_pastorianus:0.00640897)0.928:0.0407689,(S_arboricola:0.03889683,(S_kudriavzevii:0.00636331,(S_paradoxus:0.01265768,S_cerevisiae:0.00642689)0.892:0.01269612)0:0.00000033)0:0.00000087)1:0.79737216,((Nm_castellii:1.56326279,((C_glabrata:0.13419969,(N_bracarensis:0.06657034,(N_delphensis:0.09053431,N_nivariensis:0.09546541)0.845:0.04179842)0.963:0.13043302)0.994:0.30153016,(N_bacillisporus:0.39972077,Nk_castellii:0.41781228)0.93:0.18115291)0.663:0.06194901)0.67:0.14948166,(L_waltii:0.25871208,(Z_parabailii:0.30821008,(K_lactis:0.29356437,L_kluyveri:0.18269486)0.843:0.06901341)0:0.0272539)0.85:0.08421475)0:0.03710744)0.94:0.57873488)0.879:0.45902581)0.931:0.229247);')
is.rooted(Tree_data)
outgroup<-c("Y_lipolytica", "D_hansenii", "C_subhashii", "C_albicans")
Tree_root<-ape::root(Tree_data, outgroup, resolve.root=TRUE)
is.rooted(Tree_root)
#Tree_root$edge.length[Tree_root$edge.length<0.1]<-0
#addTip<-max(vcv(Tree_root))-diag(vcv(Tree_root))
#Tree_root$edge.length[Tree_root$edge[,2]<=length(Tree_root$tip)]<- Tree_root$edge.length[Tree_root$edge[,2]<=length(Tree_root$tip)]+addTip
Tree_data_2<-multi2di(Tree_root, random=TRUE)
is.rooted(Tree_data_2)
tree_data_3<-collapse.singles(Tree_data_2)
balance(tree_data_3)
is.rooted(tree_data_3)
is.ultrametric(tree_data_3)
plot(tree_data_3)

#Testing
mol_feats_model<-lm(REP_Q2 ~ Group, data=mol_feats_df1)
anova_results<-anova(mol_feats_model)
anova_results
print(mol_feats_df1$REP_Q2)
scale5<-(mol_feats_df1$REP_Q2)+0.5
scale5
rtrans<-log10(scale5)
rtrans
ltrans<-log10(max(scale5+1)-scale5)
ltrans
mol_feats_model1<-lm(rtrans~mol_feats_df1$Group)
anova1_results<-anova(mol_feats_model1)
anova1_results
#loop testing
scaled_df<-lapply(mol_feats_df1[,3:5], function(x) {
  scaled_model<-as.numeric(x)+0.5
})
scaled_df
rlog_transform_df<-lapply(scaled_df, function (x) {
  rlog_transform_model<-log10(as.numeric(x))
})
rlog_transform_df
lm_models<-lapply(rlog_transform_df, function(x){
  mol_feats_model<-lm(as.numeric(x)~mol_feats_df1$Group)
})
lm_models
anova_results<-lapply(lm_models, anova)
anova_results

#phylotesting
print(mol_feats_df$REP_Q2)
print(tree_data_2$tip.label)
print(row.names(mol_feats_df))
#names()<-row.names(mol_feats_df)
print(mol_feats_df["Group",])
print(mol_feats_df["REP_Q2",])
names(mol_feats_df)
phyloanova<-phylANOVA(multi2di(tree_data_2), mol_feats_df["Group",2:ncol(mol_feats_df)], mol_feats_df["REP_Q2",2:ncol(mol_feats_df)], nsim=1000, posthoc=TRUE, p.adj="holm")
phyloanova
print(mol_feats_mat[1, 2:ncol(mol_feats_mat)])
print(as.numeric(mol_feats_mat[2, 2:ncol(mol_feats_mat)]))
mol_feats_modela<-lm(mol_feats_mat[2, 2:ncol(mol_feats_mat)]~mol_feats_mat[1, 2:ncol(mol_feats_mat)])
anova_results<-anova(mol_feats_modela)
anova_results
phyloanova1<-phylANOVA(tree_data_3, mol_feats_mat[1,2:ncol(mol_feats_mat)], mol_feats_df[2,2:ncol(mol_feats_mat)], nsim=1000, posthoc=TRUE, p.adj="holm")
phyloanova1


#anova for full sequence control
#normally distributed
full_nd_df<-mol_feats_df1 %>% select(Species, Group, REP_S2, REP_PR, REP_FG2, REP_SG2, REP_SR2, REP_PTS2, DOC_WW_Pin1_4, MOD_CK1_1, MOD_CK2_1, MOD_GSK3_1, MOD_PKA_2, MOD_ProDKin_1, R_plus_Y, AA_S, AA_T, AA_Q, AA_R, AA_D, AA_E, AA_F, AA_I, AA_K, AA_L, AA_V, AA_Y, acidic, basic, aliphatic, polar_fraction, chain_expanding, disorder_promoting, net_charge, KL_hydropathy, isoelectric_point, ED_ratio, RK_ratio, SCD, kappa., omega., aromatic_spacing., omega_aromatic.)
full_nd_df
inv_full_nd_df<-t(full_nd_df)
inv_full_nd_df
#log transform skew right
full_sright_df<-mol_feats_df %>% select(Species, Group, REP_R2, REP_QN2, REP_RG2, REP_KAP2, CLV_C14_Caspase3.7, LIG_SH2_STAT5, MOD_N.GLC_1, MOD_PIKK_1, TRG_ER_diArg_1, AA_P, AA_A, AA_H, AA_N, AA_G, AA_M)
full_sright_df
#log transform skew left
full_sleft_df<-mol_feats_df %>% select(Species, Group, aromatic, WF_complexity, FCR)
full_sleft_df
#log transform 0.1 skew right
full_sright_01_df<-mol_feats_df %>% select(Species, Group, DEG_APCC_KENBOX_2, DEG_Kelch_Keap1_1, DOC_ANK_TNKS_1, DOC_CYCLIN_RxL_1, DOC_MAPK_JIP1_4, DOC_MAPK_MEF2A_6, DOC_PP1_RVXF_1, DOC_PP2A_B56_1, LIG_CtBP_PxDLS_1, LIG_KLC1_WD_1, LIG_PCNA_PIPBox_1, LIG_PTB_Phospho_1, LIG_SH2_NCK_1, LIG_SH2_SRC, LIG_SH2_STAP1, LIG_SH3_2, MOD_CDK_SPxK_1, MOD_DYRK1A_RPxSP_1, MOD_PKB_1, MOD_SUMO_for_1, TRG_NES_CRM1_1, TRG_NLS_MonoExtN_4, D_homorep, N_homorep, P_homorep, Q_homorep, S_homorep, T_homorep, FRG, SGFYSG, PG_rich, REP_RGG)
full_sright_01_df
#log transform 0.1 skew left
full_sleft_01_df<-mol_feats_df %>% select(Species, Group, LIG_SH2_CRK, MOD_CDK_SPK_2)
full_sleft_01_df
#log transform 0.25 skew right
full_sright_025_df<-mol_feats_df %>% select(Species, Group, DOC_MAPK_gen_1, DOC_PP4_FxxP_1, LIG_LIR_Gen_1, LIG_PTB_Apo_2, LIG_SH2_GRB2like, LIG_SUMO_SIM_par_1, MOD_CDK_SPxxK_3, MOD_SUMO_rev_2, PY, AA_C)
full_sright_025_df
#log transform 0.25 skew left
full_sleft_025_df<-mol_feats_df %>% select(Species, Group, MOD_PKA_1, MOD_Plk_1, TRG_LysEnd_APsAcLL_1, AA_W)
full_sleft_025_df
#log transform 0.5 skew right
full_sright_05_df<-mol_feats_df %>% select(Species, Group, REP_Q2, REP_N2, REP_G2, REP_E2, REP_D2, REP_P2, LIG_14.3.3_CanoR_1)
full_sright_05_df
#log transform 0.5 skew left
#log transform negative

#anova for attempt 3 method 1
#normally distributed
A3M1_nd_df<-mol_feats_df %>% select(Species, Group, REP_S2, REP_PR, REP_FG2, REP_SG2, REP_SR2, REP_PTS2, DOC_WW_Pin1_4, MOD_CK1_1, MOD_CK2_1, MOD_GSK3_1, MOD_PKA_2, MOD_ProDKin_1, R_plus_Y, AA_S, AA_T, AA_R, AA_D, AA_E, AA_F, AA_I, AA_K, AA_L, AA_V, acidic, basic, aliphatic, polar_fraction, chain_expanding, disorder_promoting, net_charge, KL_hydropathy, ED_ratio, RK_ratio, kappa., omega., aromatic_spacing., omega_aromatic.)
A3M1_nd_df
#log transform skew right
A3M1_sright_df<-mol_feats_df %>% select(Species, Group, REP_D2, REP_QN2, REP_RG2, REP_KAP2, CLV_C14_Caspase3.7, DOC_PP4_FxxP_1, LIG_14.3.3_CanoR_1, MOD_N.GLC_1, MOD_PIKK_1, AA_P, AA_A, AA_H, AA_Q, AA_N, AA_G, AA_M, AA_Y, isoelectric_point)
A3M1_sright_df
#log transform skew left
A3M1_sleft_df<-mol_feats_df %>% select(Species, Group, REP_R2, MOD_PKA_1, aromatic, WF_complexity, FCR)
A3M1_sleft_df
#log transform 0.1 skew right
A3M1_sright_01_df<-mol_feats_df %>% select(Species, Group, REP_E2, DEG_APCC_KENBOX_2, DEG_Kelch_Keap1_1, DOC_ANK_TNKS_1, DOC_CYCLIN_RxL_1, DOC_MAPK_gen_1, DOC_MAPK_JIP1_4, DOC_MAPK_MEF2A_6, DOC_PP1_RVXF_1, DOC_PP2A_B56_1, LIG_CtBP_PxDLS_1, LIG_KLC1_WD_1, LIG_PTB_Phospho_1, LIG_SH2_NCK_1, LIG_SH2_SRC, LIG_SH2_STAP1, LIG_SH3_2, LIG_SUMO_SIM_par_1, MOD_CDK_SPxK_1, MOD_DYRK1A_RPxSP_1, MOD_PKB_1, MOD_SUMO_for_1, TRG_NES_CRM1_1, TRG_NLS_MonoExtN_4, D_homorep, N_homorep, P_homorep, Q_homorep, S_homorep, T_homorep, SGFYSG, REP_RGG, AA_C)
A3M1_sright_01_df
#log transform 0.1 skew left
A3M1_sleft_01_df<-mol_feats_df %>% select(Species, Group, MOD_CDK_SPK_2)
A3M1_sleft_01_df
#log transform 0.25 skew right
A3M1_sright_025_df<-mol_feats_df %>% select(Species, Group, REP_G2, REP_P2, LIG_LIR_Gen_1, LIG_PTB_Apo_2, LIG_SH2_GRB2like, LIG_SH2_STAT5, MOD_CDK_SPxxK_3, MOD_SUMO_rev_2, TRG_LysEnd_APsAcLL_1, PY, FRG, PG_rich)
A3M1_sright_025_df
#log transform 0.25 skew left
A3M1_sleft_025_df<-mol_feats_df %>% select(Species, Group, REP_K2, LIG_SH2_CRK, TRG_ER_diArg_1, AA_W)
A3M1_sleft_025_df
#log transform 0.5 skew right
A3M1_sright_05_df<-mol_feats_df %>% select(Species, Group, REP_Q2, REP_N2)
A3M1_sright_05_df
#log transform 0.5 skew left
A3M1_sleft_05_df<-mol_feats_df %>% select(Species, Group, MOD_Plk_1)
A3M1_sleft_05_df
#log transform negative +10.6 
A3M1_negright_df<-mol_feats_df %>% select(Species, Group, SCD)
A3M1_negright_df

#anova for attempt 3 method 2
#normally distributed
A3M2_nd_df<-mol_feats_df %>% select(Species, Group, REP_S2, REP_PR, REP_FG2, REP_SG2, REP_SR2, REP_PTS2, DOC_WW_Pin1_4, MOD_CK1_1, MOD_CK2_1, MOD_GSK3_1, MOD_ProDKin_1, R_plus_Y, AA_S, AA_T, AA_D, AA_E, AA_F, AA_I, AA_V, acidic, basic, aliphatic, polar_fraction, chain_expanding, net_charge, KL_hydropathy, ED_ratio, RK_ratio, SCD, kappa., omega., aromatic_spacing., omega_aromatic.)
A3M2_nd_df
#log transform skew right
A3M2_sright_df<-mol_feats_df %>% select(Species, Group, REP_R2, REP_QN2, REP_RG2, REP_KAP2, CLV_C14_Caspase3.7, DOC_PP4_FxxP_1, LIG_14.3.3_CanoR_1, MOD_N.GLC_1, MOD_PIKK_1, MOD_PKA_1, MOD_PKA_2, AA_P, AA_A, AA_H, AA_Q, AA_N, AA_G, AA_R, AA_K, AA_M, AA_Y, disorder_promoting, isoelectric_point)
A3M2_sright_df
#log transform skew left
A3M2_sleft_df<-mol_feats_df %>% select(Species, Group, AA_L, aromatic, WF_complexity, FCR)
A3M2_sleft_df
#log transform 0.1 skew right
A3M2_sright_01_df<-mol_feats_df %>% select(Species, Group, REP_E2, DEG_APCC_KENBOX_2, DEG_Kelch_Keap1_1, DOC_ANK_TNKS_1, DOC_CYCLIN_RxL_1, DOC_MAPK_JIP1_4, DOC_MAPK_MEF2A_6, DOC_PP1_RVXF_1, DOC_PP2A_B56_1, LIG_CtBP_PxDLS_1, LIG_KLC1_WD_1, LIG_PCNA_PIPBox_1, LIG_PTB_Apo_2, LIG_PTB_Phospho_1, LIG_SH2_SRC, LIG_SH2_STAP1, LIG_SH3_2, LIG_SUMO_SIM_par_1, MOD_CDK_SPxK_1, MOD_DYRK1A_RPxSP_1, MOD_PKB_1, MOD_SUMO_for_1, TRG_NES_CRM1_1, TRG_NLS_MonoExtN_4, D_homorep, N_homorep, P_homorep, Q_homorep, S_homorep, T_homorep, SGFYSG, REP_RGG, AA_C)
A3M2_sright_01_df
#log transform 0.1 skew left
A3M2_sleft_01_df<-mol_feats_df %>% select(Species, Group, MOD_CDK_SPK_2)
A3M2_sleft_01_df
#log transform 0.25 skew right
A3M2_sright_025_df<-mol_feats_df %>% select(Species, Group, REP_G2, REP_P2, DOC_MAPK_gen_1, LIG_LIR_Gen_1, LIG_SH2_GRB2like, LIG_SH2_NCK_1, LIG_SH2_STAT5, MOD_CDK_SPxxK_3, MOD_SUMO_rev_2, TRG_ER_diArg_1, TRG_LysEnd_APsAcLL_1, PY, FRG, PG_rich)
A3M2_sright_025_df
#log transform 0.25 skew left
A3M2_sleft_025_df<-mol_feats_df %>% select(Species, Group, REP_K2, LIG_SH2_CRK, AA_W)
A3M2_sleft_025_df
#log transform 0.5 skew right
A3M2_sright_05_df<-mol_feats_df %>% select(Species, Group, REP_Q2, REP_N2, REP_D2)
A3M2_sright_05_df
#log transform 0.5 skew left
A3M2_sleft_05_df<-mol_feats_df %>% select(Species, Group, MOD_Plk_1)
A3M2_sleft_05_df
#log transform negative

#anova for attempt 3.1 method 3.2
#normally distributed
A31M32_nd_df<-mol_feats_df %>% select(Species, Group, REP_PR, REP_SG2, MOD_PIKK_1, MOD_PKA_2, AA_H, AA_Q, AA_D, AA_E, AA_F, FCR, ED_ratio, RK_ratio, SCD, kappa., omega., aromatic_spacing., omega_aromatic.)
A31M32_nd_df
#log transform skew right
A31M32_sright_df<-mol_feats_df %>% select(Species, Group, REP_S2, REP_R2, REP_RG2, REP_SR2, REP_KAP2, REP_PTS2, DOC_WW_Pin1_4, LIG_14.3.3_CanoR_1, MOD_CK1_1, MOD_CK2_1, MOD_GSK3_1, MOD_N.GLC_1, MOD_PKA_1, MOD_ProDKin_1, R_plus_Y, AA_S, AA_P, AA_T, AA_A, AA_N, AA_G, AA_R, AA_I, AA_K, AA_L, AA_M, AA_V, AA_Y, acidic, basic, aliphatic, polar_fraction, chain_expanding, aromatic, disorder_promoting)
A31M32_sright_df
#log transform skew left
A31M32_sleft_df<-mol_feats_df %>% select(Species, Group, WF_complexity, isoelectric_point)
A31M32_sleft_df
#log transform 0.1 skew right
A31M32_sright_01_df<-mol_feats_df %>% select(Species, Group, REP_E2, DEG_APCC_KENBOX_2, DEG_Kelch_Keap1_1, DOC_ANK_TNKS_1, DOC_CYCLIN_RxL_1, DOC_MAPK_MEF2A_6, DOC_PP1_RVXF_1, DOC_PP2A_B56_1, LIG_KLC1_WD_1, LIG_LIR_Gen_1, LIG_PTB_Apo_2, LIG_PTB_Phospho_1, LIG_SH2_CRK, LIG_SH2_NCK_1, LIG_SH2_SRC, LIG_SH3_2, LIG_SUMO_SIM_par_1, MOD_CDK_SPK_2, MOD_CDK_SPxK_1, MOD_DYRK1A_RPxSP_1, MOD_NMyristoyl, MOD_PKB_1, MOD_SUMO_for_1, TRG_ER_diArg_1, TRG_NLS_MonoExtN_4, N_homorep, P_homorep, Q_homorep, S_homorep, T_homorep, SGFYSG, PG_rich, REP_RGG, AA_C)
A31M32_sright_01_df
#log transform 0.1 skew left
#log transform 0.25 skew right
A31M32_sright_025_df<-mol_feats_df %>% select(Species, Group, REP_Q2, REP_D2, REP_K2, REP_P2, CLV_C14_Caspase3.7, DOC_MAPK_gen_1, DOC_PP4_FxxP_1, LIG_SH2_GRB2like, LIG_SH2_STAP1, MOD_CDK_SPxxK_3, MOD_SUMO_rev_2, TRG_LysEnd_APsAcLL_1, PY, FRG, AA_W)
A31M32_sright_025_df
#log transform 0.25 skew left
#log transform 0.5 skew right
A31M32_sright_05_df<-mol_feats_df %>% select(Species, Group, REP_N2, REP_G2, REP_QN2, REP_FG2, MOD_Plk_1)
A31M32_sright_05_df
#log transform 0.5 skew left
#log transform negative skew right +2
A31M32_negright_df<-mol_feats_df %>% select(Species, Group, KL_hydropathy)
A31M32_negright_df
#log transform negative skew left +2.1
A31M32_negleft_df<-mol_feats_df %>% slecet(Species, Group, net_charge)

#anova for attempt 4 SC based ocntrol
#normally distributed
A4_nd_df<-mol_feats_df %>% select(Species, Group, REP_S2, REP_PR, REP_SG2, REP_SR2, REP_PTS2, DOC_WW_Pin1_4, MOD_CK1_1, MOD_GSK3_1, MOD_ProDKin_1, AA_S, AA_T, AA_D, AA_E, AA_F, AA_M, AA_V, polar_fraction, net_charge, ED_ratio, RK_ratio, SCD, kappa., omega., aromatic_spacing., omega_aromatic.)
A4_nd_df
#log transform skew right
A4_sright_df<-mol_feats_df %>% select(Species, Group, REP_R2, REP_RG2, REP_KAP2, LIG_14.3.3_CanoR_1, MOD_CK2_1, MOD_N.GLC_1, MOD_PIKK_1, MOD_PKA_1, AA_P, AA_A, AA_H, AA_Q, AA_N, AA_G, AA_R, AA_I, AA_K, AA_L, AA_Y, aliphatic, FCR)
A4_sright_df
#log transform skew left
A4_sleft_df<-mol_feats_df %>% select(Species, Group, MOD_PKA_2, R_plus_Y, acidic, basic, chain_expanding, aromatic, disorder_promoting, WF_complexity, isoelectric_point)
A4_sleft_df
#log transform 0.1 skew right
A4_sright_01_df<-mol_feats_df %>% select(Species, Group, REP_E2, DEG_APCC_KENBOX_2, DEG_Kelch_Keap1_1, DOC_ANK_TNKS_1, DOC_CYCLIN_RxL_1, DOC_MAPK_gen_1, DOC_MAPK_MEF2A_6, DOC_PP1_RVXF_1, DOC_PP2A_B56_1, LIG_KLC1_WD_1, LIG_LIR_Gen_1, LIG_PTB_Phospho_1, LIG_PTB_Apo_2, LIG_SH2_NCK_1, LIG_SH2_SRC, LIG_SH2_STAP1, LIG_SH3_2, LIG_SUMO_SIM_par_1, MOD_CDK_SPK_2, MOD_CDK_SPxK_1, MOD_DYRK1A_RPxSP_1, MOD_PKB_1, MOD_SUMO_for_1, TRG_LysEnd_APsAcLL_1, TRG_NLS_MonoExtN_4, N_homorep, P_homorep, Q_homorep, S_homorep, T_homorep, FRG, SGFYSG, PG_rich, REP_RGG, AA_C)
A4_sright_01_df
#log transform 0.1 skew left
A4_sleft_01_df<-mol_feats_df %>% select(Species, Group, LIG_SH2_CRK)
A4_sleft_01_df
#log transform 0.25 skew right
A4_sright_025_df<-mol_feats_df %>% select(Species, Group, REP_G2, REP_D2, REP_K2, REP_P2, REP_FG2, CLV_C14_Caspase3.7, DOC_PP4_FxxP_1, LIG_SH2_GRB2like, LIG_SH2_STAT5, MOD_CDK_SPxxK_3, MOD_SUMO_rev_2, TRG_ER_diArg_1, PY, AA_W)
A4_sright_025_df
#log transform 0.25 skew left
#log transform 0.5 skew right
A4_sright_05_df<-mol_feats_df %>% select(Species, Group, REP_Q2, REP_N2, REP_QN2, MOD_Plk_1)
#log transform 0.5 skew left
#log transform negative +1.5
A4_negright_df<-mol_feats_df %>% select(Species, Group, KL_hydropathy)
A4_negright_df


