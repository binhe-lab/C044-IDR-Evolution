rm(list=ls())
getwd()
library(dplyr)
library(e1071)
library(moments)


data<-read.csv("IDR_molecular_features_data_Full_sequence.csv", header=TRUE, stringsAsFactors=TRUE)
data
data1<-read.csv("IDR_molecular_features_data_Attempt3_09_20_M1.csv", header=TRUE, stringsAsFactors = TRUE)
data1
data2<-read.csv("IDR_molecular_features_data_Attempt3_09_20_M2.csv", header=TRUE, stringsAsFactors = TRUE)
data2
data3<-read.csv("IDR_molecular_features_data_Attempt3.1_10_10_M3.2.csv", header=TRUE, stringsAsFactors = TRUE)
data3
data4<-read.csv("IDR_molecular_features_data_Attempt4_10_10.csv", header=TRUE, stringsAsFactors = TRUE)
data4
mol_feats_df<-data.frame(data[1:21,], stringsAsFactors = FALSE)
mol_feats_df
mol_feats_df1<-data.frame(data1[1:21,], stringsAsFactors = FALSE)
mol_feats_df1
mol_feats_df2<-data.frame(data2[1:21,], stringsAsFactors = FALSE)
mol_feats_df2
mol_feats_df3<-data.frame(data3[1:21,], stringsAsFactors = FALSE)
mol_feats_df3
mol_feats_df4<-data.frame(data4[1:21,], stringsAsFactors = FALSE)
mol_feats_df4

#Shapiro testing 
#Full sequence control
shapiro.test(mol_feats_df$REP_Q2)

Shapiro_wilks_results<-lapply(mol_feats_df[,3:22], shapiro.test)
Shapiro_wilks_results
#fails: 23
Shapiro_wilks_results1<-lapply(mol_feats_df[,24:28], shapiro.test)
Shapiro_wilks_results1
#fails 29
Shapiro_wilks_results2<-lapply(mol_feats_df[,30:34], shapiro.test)
Shapiro_wilks_results2
#fails 35
shapiro.test(mol_feats_df$LIG_CtBP_PxDLS_1)
#fails37-41
Shapiro_wilks_results3<-lapply(mol_feats_df[,42:43], shapiro.test)
Shapiro_wilks_results3
#fails 44
shapiro.test(mol_feats_df$LIG_PCNA_PIPBox_1)
#fails 46-48
Shapiro_wilks_results4<-lapply(mol_feats_df[,49:50], shapiro.test)
Shapiro_wilks_results4
#fails 51
Shapiro_wilks_results5<-lapply(mol_feats_df[,52:58], shapiro.test)
Shapiro_wilks_results5
#fails 59
shapiro.test(mol_feats_df$LIG_SUMO_SIM_par_1)
#fails 61
Shapiro_wilks_results6<-lapply(mol_feats_df[,62:69], shapiro.test)
Shapiro_wilks_results6
#fails 70
Shapiro_wilks_results7<-lapply(mol_feats_df[,71:79], shapiro.test)
Shapiro_wilks_results7
#fails 80
Shapiro_wilks_results8<-lapply(mol_feats_df[,81:83], shapiro.test)
Shapiro_wilks_results8
#fails 84-85
shapiro.test(mol_feats_df$D_homorep)
#fails 87-93
Shapiro_wilks_results9<-lapply(mol_feats_df[,94:96], shapiro.test)
Shapiro_wilks_results9
#fails 97
Shapiro_wilks_results10<-lapply(mol_feats_df[,98:99], shapiro.test)
Shapiro_wilks_results10
#fails 100-102
Shapiro_wilks_results11<-lapply(mol_feats_df[,103:106], shapiro.test)
Shapiro_wilks_results11
#fails 107-108
Shapiro_wilks_results12<-lapply(mol_feats_df[,109:148], shapiro.test)
Shapiro_wilks_results12
shapiro.test(as.numeric(mol_feats_df[,149]) )
#end file

#Attempt 3 Method 1
shapiro.test(mol_feats_df1$REP_Q2)

Shapiro_wilks_resultsa<-lapply(mol_feats_df1[,3:22], shapiro.test)
Shapiro_wilks_resultsa
#fails: 23
Shapiro_wilks_resultsa1<-lapply(mol_feats_df1[,24:28], shapiro.test)
Shapiro_wilks_resultsa1
#fails 29
Shapiro_wilks_resultsa2<-lapply(mol_feats_df1[,30:34], shapiro.test)
Shapiro_wilks_resultsa2
#fails 35
shapiro.test(mol_feats_df1$LIG_CtBP_PxDLS_1)
#fails37-41
Shapiro_wilks_resultsa3<-lapply(mol_feats_df1[,42:43], shapiro.test)
Shapiro_wilks_resultsa3
#fails 44-48
Shapiro_wilks_resultsa4<-lapply(mol_feats_df1[,49:50], shapiro.test)
Shapiro_wilks_resultsa4
#fails 51
Shapiro_wilks_resultsa5<-lapply(mol_feats_df1[,52:58], shapiro.test)
Shapiro_wilks_resultsa5
#fails 59
shapiro.test(mol_feats_df1$LIG_SUMO_SIM_par_1)
#fails 61
Shapiro_wilks_resultsa6<-lapply(mol_feats_df1[,62:69], shapiro.test)
Shapiro_wilks_resultsa6
#fails 70
Shapiro_wilks_resultsa7<-lapply(mol_feats_df1[,71:79], shapiro.test)
Shapiro_wilks_resultsa7
#fails 80
Shapiro_wilks_resultsa8<-lapply(mol_feats_df1[,81:83], shapiro.test)
Shapiro_wilks_resultsa8
#fails 84-85
shapiro.test(mol_feats_df1$D_homorep)
#fails 87-93
Shapiro_wilks_resultsa9<-lapply(mol_feats_df1[,94:96], shapiro.test)
Shapiro_wilks_resultsa9
#fails 97
Shapiro_wilks_resultsa10<-lapply(mol_feats_df1[,98:99], shapiro.test)
Shapiro_wilks_resultsa10
#fails 100-102
Shapiro_wilks_resultsa11<-lapply(mol_feats_df1[,103:106], shapiro.test)
Shapiro_wilks_resultsa11
#fails 107-108
Shapiro_wilks_resultsa12<-lapply(mol_feats_df1[,109:148], shapiro.test)
Shapiro_wilks_resultsa12
shapiro.test(as.numeric(mol_feats_df1[,149]) )
#end file

#Attempt 3 Method 2
shapiro.test(mol_feats_df2$REP_Q2)

Shapiro_wilks_resultsb<-lapply(mol_feats_df2[,3:22], shapiro.test)
Shapiro_wilks_resultsb
#fails: 23
Shapiro_wilks_results1b<-lapply(mol_feats_df2[,24:28], shapiro.test)
Shapiro_wilks_results1b
#fails 29
Shapiro_wilks_results2b<-lapply(mol_feats_df2[,30:34], shapiro.test)
Shapiro_wilks_results2b
#fails 35
shapiro.test(mol_feats_df2$LIG_CtBP_PxDLS_1)
#fails37-41
Shapiro_wilks_results3b<-lapply(mol_feats_df2[,42:43], shapiro.test)
Shapiro_wilks_results3b
#fails 44
shapiro.test(mol_feats_df2$LIG_PCNA_PIPBox_1)
#fails 46-48
Shapiro_wilks_results4b<-lapply(mol_feats_df2[,49:50], shapiro.test)
Shapiro_wilks_results4b
#fails 51
Shapiro_wilks_results5b<-lapply(mol_feats_df2[,52:58], shapiro.test)
Shapiro_wilks_results5b
#fails 59
shapiro.test(mol_feats_df2$LIG_SUMO_SIM_par_1)
#fails 61
Shapiro_wilks_results6b<-lapply(mol_feats_df2[,62:69], shapiro.test)
Shapiro_wilks_results6b
#fails 70
Shapiro_wilks_results7b<-lapply(mol_feats_df2[,71:79], shapiro.test)
Shapiro_wilks_results7b
#fails 80
Shapiro_wilks_results8b<-lapply(mol_feats_df2[,81:83], shapiro.test)
Shapiro_wilks_results8b
#fails 84-85
shapiro.test(mol_feats_df2$D_homorep)
#fails 87-93
Shapiro_wilks_results9b<-lapply(mol_feats_df2[,94:96], shapiro.test)
Shapiro_wilks_results9b
#fails 97
Shapiro_wilks_results10b<-lapply(mol_feats_df2[,98:99], shapiro.test)
Shapiro_wilks_results10b
#fails 100-102
Shapiro_wilks_results11b<-lapply(mol_feats_df2[,103:106], shapiro.test)
Shapiro_wilks_results11b
#fails 107-108
Shapiro_wilks_results12b<-lapply(mol_feats_df2[,109:148], shapiro.test)
Shapiro_wilks_results12b
shapiro.test(as.numeric(mol_feats_df2[,149]) )
#end file

#Attempt 3.1 Method 3.2
shapiro.test(mol_feats_df3$REP_Q2)

Shapiro_wilks_resultsc<-lapply(mol_feats_df3[,3:22], shapiro.test)
Shapiro_wilks_resultsc
#fails: 23
Shapiro_wilks_results1c<-lapply(mol_feats_df3[,24:26], shapiro.test)
Shapiro_wilks_results1c
#fails 27
shapiro.test(mol_feats_df3$DOC_MAPK_MEF2A_6)
#fails 29
Shapiro_wilks_results2c<-lapply(mol_feats_df3[,30:34], shapiro.test)
Shapiro_wilks_results2c
#fails 35-41
Shapiro_wilks_results3c<-lapply(mol_feats_df3[,42:43], shapiro.test)
Shapiro_wilks_results3c
#fails 44-48
Shapiro_wilks_results4c<-lapply(mol_feats_df3[,49:50], shapiro.test)
Shapiro_wilks_results4c
#fails 51
Shapiro_wilks_results5c<-lapply(mol_feats_df3[,52:58], shapiro.test)
Shapiro_wilks_results5c
#fails 59
shapiro.test(mol_feats_df3$LIG_SUMO_SIM_par_1)
#fails 61
Shapiro_wilks_results6c<-lapply(mol_feats_df3[,62:79], shapiro.test)
Shapiro_wilks_results6c
#Shapiro_wilks_results7c<-lapply(mol_feats_df3[,71:79], shapiro.test)
#Shapiro_wilks_results7c
#fails 80
shapiro.test(mol_feats_df3$TRG_LysEnd_APsAcLL_1)
#fails 82
shapiro.test(mol_feats_df3$TRG_NLS_MonoExtN_4)
#fails 84-93
Shapiro_wilks_results9c<-lapply(mol_feats_df3[,94:96], shapiro.test)
Shapiro_wilks_results9c
#fails 97
Shapiro_wilks_results10c<-lapply(mol_feats_df3[,98:99], shapiro.test)
Shapiro_wilks_results10c
#fails 100-102
Shapiro_wilks_results11c<-lapply(mol_feats_df3[,103:106], shapiro.test)
Shapiro_wilks_results11c
#fails 107-108
Shapiro_wilks_results12c<-lapply(mol_feats_df3[,109:148], shapiro.test)
Shapiro_wilks_results12c
shapiro.test(as.numeric(mol_feats_df3[,149]) )
#end file

#SC based control
shapiro.test(mol_feats_df4$REP_Q2)

Shapiro_wilks_resultsd<-lapply(mol_feats_df4[,3:22], shapiro.test)
Shapiro_wilks_resultsd
#fails: 23
Shapiro_wilks_results1d<-lapply(mol_feats_df4[,24:26], shapiro.test)
Shapiro_wilks_results1d
#fails 27
shapiro.test(mol_feats_df4$DOC_MAPK_MEF2A_6)
#fails 29
Shapiro_wilks_results2d<-lapply(mol_feats_df4[,30:34], shapiro.test)
Shapiro_wilks_results2d
#fails 35-41
Shapiro_wilks_results3d<-lapply(mol_feats_df4[,42:43], shapiro.test)
Shapiro_wilks_results3d
#fails 44-45
shapiro.test(mol_feats_df4$LIG_PDZ_Class_1)
#fails 47-48
Shapiro_wilks_results4d<-lapply(mol_feats_df4[,49:50], shapiro.test)
Shapiro_wilks_results4d
#fails 51
Shapiro_wilks_results5d<-lapply(mol_feats_df4[,52:58], shapiro.test)
Shapiro_wilks_results5d
#fails 59
shapiro.test(mol_feats_df4$LIG_SUMO_SIM_par_1)
#fails 61
Shapiro_wilks_results6d<-lapply(mol_feats_df4[,62:69], shapiro.test)
Shapiro_wilks_results6d
#fails 70
Shapiro_wilks_results7d<-lapply(mol_feats_df4[,71:79], shapiro.test)
Shapiro_wilks_results7d
#fails 80
shapiro.test(mol_feats_df4$TRG_LysEnd_APsAcLL_1)
#fails 82
shapiro.test(mol_feats_df4$TRG_NLS_MonoExtN_4)
#fails 84-93
Shapiro_wilks_results9d<-lapply(mol_feats_df4[,94:96], shapiro.test)
Shapiro_wilks_results9d
#fails 97
Shapiro_wilks_results10d<-lapply(mol_feats_df4[,98:99], shapiro.test)
Shapiro_wilks_results10d
#fails 100-102
Shapiro_wilks_results11d<-lapply(mol_feats_df4[,103:106], shapiro.test)
Shapiro_wilks_results11d
#fails 107-108
Shapiro_wilks_results12d<-lapply(mol_feats_df4[,109:148], shapiro.test)
Shapiro_wilks_results12d
shapiro.test(as.numeric(mol_feats_df4[,149]) )
#end file

#Skew testing
#Full sequence control
skewness(mol_feats_df$REP_Q2, na.rm=TRUE)

skew_results<-lapply(mol_feats_df[,3:148], skewness)
skew_results

skewness(as.numeric(mol_feats_df[,149]))

#Attempt 3 Method 1
skewness(mol_feats_df1$REP_Q2, na.rm=TRUE)

skew_results1<-lapply(mol_feats_df1[,3:148], skewness)
skew_results1

skewness(as.numeric(mol_feats_df1[,149]))

#Attempt 3 Method 2
skewness(mol_feats_df2$REP_Q2, na.rm=TRUE)

skew_results2<-lapply(mol_feats_df2[,3:148], skewness)
skew_results2

skewness(as.numeric(mol_feats_df2[,149]))

#Attempt 3.1 Method 3.2
skewness(mol_feats_df3$REP_Q2, na.rm=TRUE)

skew_results3<-lapply(mol_feats_df3[,3:148], skewness)
skew_results3

skewness(as.numeric(mol_feats_df3[,149]))

#SC based control 
skewness(mol_feats_df4$REP_Q2, na.rm=TRUE)

skew_results4<-lapply(mol_feats_df4[,3:148], skewness)
skew_results4

skewness(as.numeric(mol_feats_df4[,149]))





