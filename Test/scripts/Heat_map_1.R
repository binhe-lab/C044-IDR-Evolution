rm(list=ls())
getwd()
library(ggplot2)
library(pastecs)
z_score_data<-read.csv("Z_score_1.csv", header=TRUE, stringsAsFactors=TRUE)
z_score_data
#heatmap(z_score_data)
row.names(z_score_data)<-z_score_data$Species
#z_score_data<-z_score_data[,1:3]
z_score_data_matrix<-data.matrix(z_score_data)
heatmap(z_score_data_matrix)
