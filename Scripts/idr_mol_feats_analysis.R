#Lucretia Shumate
#2022
#This file takes the z scores of all homologs of an IDR sequence molecular features calculation and makes a heat map.

rm(list=ls())
getwd()
library(ggplot2)
library(pastecs)
library(RColorBrewer)
#library(dplyr)
#Heat maps for data from full sequence
Z_score_full_sequence<-read.csv("Z_score_full_sequence.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_full_sequence
row.names(Z_score_full_sequence)<-Z_score_full_sequence$Species
Z_score_full_sequence_matrix<-data.matrix(Z_score_full_sequence)
Z_score_full_sequence_matrix
#par(mar=c(15,10,1,15))
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_full_sequence_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Full Sequence", xlab="Molecular features", ylab="Species")

Z_full_sequence_comp<-Z_score_full_sequence_matrix[c(1,3),]
Z_full_sequence_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_full_sequence_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Full Sequence", xlab="Molecular features", ylab="Species")

#Heat maps for data form Attempt 1 08/28
Z_score_attempt1<-read.csv("Z_score_Attempt1_08_28.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt1
row.names(Z_score_attempt1)<-Z_score_attempt1$Species
Z_score_attempt1_matrix<-data.matrix(Z_score_attempt1)
Z_score_attempt1_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt1_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="IDR Predicted Residues", xlab="Molecular features", ylab="Species")

Z_comp_M1<-Z_score_attempt1_matrix[c(1,3),]
Z_comp_M1
dev.new(width=100, height=100, unit="in")
heatmap(Z_comp_M1[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="IDR Predicted Residues", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt2 09/09
Z_score_all_IDRs<-read.csv("Z_scores_all_IDRs.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_all_IDRs
row.names(Z_score_all_IDRs)<-Z_score_all_IDRs$Species
Z_score_all_IDRs_matrix<-data.matrix(Z_score_all_IDRs)
Z_score_all_IDRs_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_all_IDRs_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without Conserved SSE", xlab="Molecular features", ylab="Species")

Z_comp_M2<-Z_score_all_IDRs_matrix[c(1,3),]
Z_comp_M2
dev.new(width=100, height=100, unit="in")
heatmap(Z_comp_M2[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without Conserved SSE", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3 M1 09/20
Z_score_attempt3_M1<-read.csv("Z_score_Attempt3_09_20_M1.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_M1
row.names(Z_score_attempt3_M1)<-Z_score_attempt3_M1$Species
Z_score_attempt3_M1_matrix<-data.matrix(Z_score_attempt3_M1)
Z_score_attempt3_M1_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_M1_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without N terminal helix and C terminal bHLH", xlab="Molecular features", ylab="Species")

Z_attempt3_M1_comp<-Z_score_attempt3_M1_matrix[c(1,3),]
Z_attempt3_M1_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_M1_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without N terminal helix and C terminal bHLH", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3 M2 09/20
Z_score_attempt3_M2<-read.csv("Z_score_Attempt3_09_20_M2.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_M2
row.names(Z_score_attempt3_M2)<-Z_score_attempt3_M2$Species
Z_score_attempt3_M2_matrix<-data.matrix(Z_score_attempt3_M2)
Z_score_attempt3_M2_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_M2_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without C Terminal bHLH", xlab="Molecular features", ylab="Species")

Z_attempt3_M2_comp<-Z_score_attempt3_M2_matrix[c(1,3),]
Z_attempt3_M2_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_M2_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Without C Terminal bHLH", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3 M3 09/20
Z_score_attempt3_M3<-read.csv("Z_score_Attempt3_09_20_M3.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_M3
row.names(Z_score_attempt3_M3)<-Z_score_attempt3_M3$Species
Z_score_attempt3_M3_matrix<-data.matrix(Z_score_attempt3_M3)
Z_score_attempt3_M3_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_M3_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: Individual", xlab="Molecular features", ylab="Species")

Z_attempt3_M3_comp<-Z_score_attempt3_M3_matrix[c(1,3),]
Z_attempt3_M3_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_M3_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: Individual", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3 M4.1 09/20
Z_score_attempt3_M4_1<-read.csv("Z_score_Attempt3_09_20_M4.1.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_M4_1
row.names(Z_score_attempt3_M4_1)<-Z_score_attempt3_M4_1$Species
Z_score_attempt3_M4_1_matrix<-data.matrix(Z_score_attempt3_M4_1)
Z_score_attempt3_M4_1_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_M4_1_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 1", xlab="Molecular features", ylab="Species")

Z_attempt3_M4_1_comp<-Z_score_attempt3_M4_1_matrix[c(1,3),]
Z_attempt3_M4_1_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_M4_1_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 1", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3 M4.4 09/20
Z_score_attempt3_M4_4<-read.csv("Z_score_Attempt3_09_20_M4.4.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_M4_4
row.names(Z_score_attempt3_M4_4)<-Z_score_attempt3_M4_4$Species
Z_score_attempt3_M4_4_matrix<-data.matrix(Z_score_attempt3_M4_4)
Z_score_attempt3_M4_4_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_M4_4_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 4", xlab="Molecular features", ylab="Species")

Z_attempt3_M4_4_comp<-Z_score_attempt3_M4_4_matrix[c(1,3),]
Z_attempt3_M4_4_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_M4_4_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 4", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M3.1 10/10
Z_score_attempt3_1_M3_1<-read.csv("Z_score_Attempt_3.1_10_10_M3.1.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M3_1
row.names(Z_score_attempt3_1_M3_1)<-Z_score_attempt3_1_M3_1$Species
Z_score_attempt3_1_M3_1_matrix<-data.matrix(Z_score_attempt3_1_M3_1)
Z_score_attempt3_1_M3_1_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M3_1_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="PONDR longest IDR: Homology", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M3_1_comp<-Z_score_attempt3_1_M3_1_matrix[c(1,3),]
Z_attempt3_1_M3_1_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M3_1_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="PONDR Longest IDR: Homology", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M3.2 10/10
Z_score_attempt3_1_M3_2<-read.csv("Z_score_Attempt3.1_10_10_M3.2.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M3_2
row.names(Z_score_attempt3_1_M3_2)<-Z_score_attempt3_1_M3_2$Species
Z_score_attempt3_1_M3_2_matrix<-data.matrix(Z_score_attempt3_1_M3_2)
Z_score_attempt3_1_M3_2_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M3_2_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: Homology", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M3_2_comp<-Z_score_attempt3_1_M3_2_matrix[c(1,3),]
Z_attempt3_1_M3_2_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M3_2_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: Homology", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M4.2 10/10
Z_score_attempt3_1_M4_2<-read.csv("Z_score_Attempt3.1_10_10_M4.2.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M4_2
row.names(Z_score_attempt3_1_M4_2)<-Z_score_attempt3_1_M4_2$Species
Z_score_attempt3_1_M4_2_matrix<-data.matrix(Z_score_attempt3_1_M4_2)
Z_score_attempt3_1_M4_2_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M4_2_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 2", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M4_2_comp<-Z_score_attempt3_1_M4_2_matrix[c(1,3),]
Z_attempt3_1_M4_2_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M4_2_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 2", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M4.3 10/10
Z_score_attempt3_1_M4_3<-read.csv("Z_score_Attempt3.1_10_10_M4.3.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M4_3
row.names(Z_score_attempt3_1_M4_3)<-Z_score_attempt3_1_M4_3$Species
Z_score_attempt3_1_M4_3_matrix<-data.matrix(Z_score_attempt3_1_M4_3)
Z_score_attempt3_1_M4_3_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M4_3_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 3", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M4_3_comp<-Z_score_attempt3_1_M4_3_matrix[c(1,3),]
Z_attempt3_1_M4_3_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M4_3_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 3", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M4.5 10/10
Z_score_attempt3_1_M4_5<-read.csv("Z_score_Attempt3.1_10_10_M4.5.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M4_5
row.names(Z_score_attempt3_1_M4_5)<-Z_score_attempt3_1_M4_5$Species
Z_score_attempt3_1_M4_5_matrix<-data.matrix(Z_score_attempt3_1_M4_5)
Z_score_attempt3_1_M4_5_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M4_5_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 5", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M4_5_comp<-Z_score_attempt3_1_M4_5_matrix[c(1,3),]
Z_attempt3_1_M4_5_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M4_5_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Segment 5", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt3.1 M4.5.1 10/10
Z_score_attempt3_1_M4_5_1<-read.csv("Z_score_Attempt3.1_10_10_M4.5.1.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt3_1_M4_5_1
row.names(Z_score_attempt3_1_M4_5_1)<-Z_score_attempt3_1_M4_5_1$Species
Z_score_attempt3_1_M4_5_1_matrix<-data.matrix(Z_score_attempt3_1_M4_5_1)
Z_score_attempt3_1_M4_5_1_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt3_1_M4_5_1_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Loop bHLH", xlab="Molecular features", ylab="Species")

Z_attempt3_1_M4_5_1_comp<-Z_score_attempt3_1_M4_5_1_matrix[c(1,3),]
Z_attempt3_1_M4_5_1_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt3_1_M4_5_1_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Loop bHLH", xlab="Molecular features", ylab="Species")

#Heat maps for data from Attempt4 10/10
Z_score_attempt4<-read.csv("Z_score_Attempt4_10_10.csv", header=TRUE, stringsAsFactors=TRUE)
Z_score_attempt4
row.names(Z_score_attempt4)<-Z_score_attempt4$Species
Z_score_attempt4_matrix<-data.matrix(Z_score_attempt4)
Z_score_attempt4_matrix
dev.new(width=100, height=100, unit="in")
heatmap(Z_score_attempt4_matrix[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: SC Homology", xlab="Molecular features", ylab="Species")

Z_attempt4_comp<-Z_score_attempt4_matrix[c(1,3),]
Z_attempt4_comp
dev.new(width=100, height=100, unit="in")
heatmap(Z_attempt4_comp[,-1], scale="none", Colv=NA, cexCol=0.5, col=colorRampPalette(brewer.pal(8, "PuRd"))(60), main="Long IDR: SC Homology", xlab="Molecular features", ylab="Species")
