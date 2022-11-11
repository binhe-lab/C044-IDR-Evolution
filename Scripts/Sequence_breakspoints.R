#Lucretia Shumate
#2022
#This code makes a segment plot to show the IDR sequence. Start at 0, end at end of bHLH segment.

rm(list=ls())
getwd()
library(ggplot2)
library(RColorBrewer)
library(pastecs)
library(dplyr)

#sequences<-data.frame(Species=c('Nm_castellii', 'C_glabrata', 'N_bracarensis', 'N_delphensis', 'N_nivariensis', 'N_bacillisporus', 'Nk_castellii', 'K_lactis', 'L_kluyveri', 'Z_parabailii', 'L_waltii', 'S_eubayanus', 'S_pastorianus', 'S_arboricola', 'S_kudriavzevii', 'S_paradoxus', 'E_neolycopersici', 'S_cerevisiae', 'D_hansenii', 'C_subhashii', 'C_albicans', 'Y_lipolytica'), length_seq=c(391, 533, 488, 464, 475, 541, 522, 691, 482, 435, 479, 331, 312, 320, 324, 314, 161, 312, 498, 560, 659, 716))
#sequences
#sequence_order<-sequences
#sequence_order$Species<-factor(sequence_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
#sequence_order

#Input data file
sequence_breaks<-read.csv("Sequence_breakpoints.csv", header=TRUE, stringsAsFactors=FALSE)
sequence_breaks

#Data frame of basic helix loop helix domain
bHLH_df<-data.frame(subset(sequence_breaks, Type=='bHLH'))
bHLH_df
bHLH_df_order<-bHLH_df
bHLH_df_order$Species<-factor(bHLH_df_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
bHLH_df_order

#Data frame of IDR sequence #1
IDR1_df<-data.frame(subset(sequence_breaks, Type=='IDR1'))
IDR1_df
IDR1_df_order<-IDR1_df
IDR1_df_order$Species<-factor(IDR1_df_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
IDR1_df_order

#Data frame of IDR sequence #2
IDR2_df<-data.frame(subset(sequence_breaks, Type=='IDR2'))
IDR2_df
IDR2_df_order<-IDR2_df
IDR2_df_order$Species<-factor(IDR2_df_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
IDR2_df_order

#Data frame of IDR sequence #3
IDR3_df<-data.frame(subset(sequence_breaks, Type=='IDR3'))
IDR3_df
IDR3_df_order<-IDR3_df
IDR3_df_order$Species<-factor(IDR3_df_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
IDR3_df_order

#Data frame of the segment break points
Segments_df<-data.frame(subset(sequence_breaks, Type=='Seg'))
Segments_df
Segments_df_order<-Segments_df
Segments_df_order$Species<-factor(Segments_df_order$Species, levels=c('Y_lipolytica', 'C_albicans', 'C_subhashii', 'D_hansenii', 'S_cerevisiae', 'E_neolycopersici', 'S_paradoxus', 'S_kudriavzevii', 'S_arboricola', 'S_pastorianus', 'S_eubayanus', 'L_waltii', 'Z_parabailii', 'L_kluyveri', 'K_lactis', 'Nk_castellii', 'N_bacillisporus', 'N_nivariensis', 'N_delphensis', 'N_bracarensis', 'C_glabrata', 'Nm_castellii'))
Segments_df_order

#Graph of sequence length
barchart_seq<-ggplot(bHLH_df_order, aes(Full_length, Species))+geom_bar(data=bHLH_df_order, position="dodge", stat="identity", color=c("black"), fill=c("white"))
barchart_seq
#Line plot of bHLH domain
bHLH_breaks<-ggplot(bHLH_df_order, aes(X, Species))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+ggtitle("bHLH of Pho4 Homologs")+xlab("Sequence length")
bHLH_breaks
#Overlay of sequence bars an bHLH domain
#barchart_seq1<-ggplot(bHLH_df_order, aes(Full_length, Species))+geom_bar(data=bHLH_df_order, position="dodge", stat="identity", color=c("black"), fill=c("white"))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))#+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+scale_y_discrete()
#barchart_seq1

#Overlay of IDR1 and bHLH with Sequence
IDR1_breaks<-ggplot(IDR1_df_order, aes(X, Species))+geom_segment(data=IDR1_df_order, aes(xend=Xend, yend=Species), size=7, color=c(IDR1_df_order$Col))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+ggtitle("IDR1 of Pho4 Homologs")+xlab("Sequence length")
IDR1_breaks
#barchart_IDR1<-ggplot(IDR1_df_order, aes(Full_length, Species))+geom_bar(data=IDR1_df_order, position="dodge", stat="identity", color=c("black"), fill=c("white"))+geom_segment(data=IDR1_df_order, aes(xend=Xend, yend=Species), size=7, color=c(IDR1_df_order$Col))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+scale_y_discrete()
#barchart_IDR1

#Overlay of IDR2 and bHLH with Sequence
IDR2_breaks<-ggplot(IDR2_df_order, aes(X, Species))+geom_segment(data=IDR2_df_order, aes(xend=Xend, yend=Species), size=7, color=c(IDR2_df_order$Col))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+ggtitle("IDR2 of Pho4 Homologs")+xlab("Sequence length")
IDR2_breaks

#Overlay of IDR3 and bHLH with sequence
IDR3_breaks<-ggplot(IDR3_df_order, aes(X, Species))+geom_segment(data=IDR3_df_order, aes(xend=Xend, yend=Species), size=7, color=c(IDR3_df_order$Col))+geom_segment(data=bHLH_df_order, aes(xend=Xend, yend=Species), size=7, color=c(bHLH_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+ggtitle("IDR3 of Pho4 Homologs")+xlab("Sequence length")
IDR3_breaks

#Segment marks, note segment 1 starts at AA1 and segment 5 contains the bHLH
Segment_breaks<-ggplot(Segments_df_order, aes(X, Species))+geom_segment(data=Segments_df_order, aes(xend=Xend, yend=Species), size=7, color=c(Segments_df_order$Col))+scale_x_continuous(breaks=seq(from=0, to=730, by=50))+ggtitle("Segments of Pho4 Homologs")+xlab("Sequence length")
Segment_breaks



