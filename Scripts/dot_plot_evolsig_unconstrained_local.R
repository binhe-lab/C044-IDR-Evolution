rm(list=ls())
getwd()
library(ggplot2)
library(dplyr)
#library(data.table)
z_score_data<-read.csv("min_max_molecular_features_data.csv", header=TRUE, sep=",", stringsAsFactors=TRUE)
#z_score_min_data<-read.table("min_max_molecular_features_data.csv", header=TRUE, sep=",", stringsAsFactors=TRUE, colClasses =c("factor", "factor", "numeric", "NULL", "factor", "NULL", "numeric", "numeric"))
#z_score_min_data<-read.table("min_max_molecular_features_data.csv", header=TRUE, sep=",", stringsAsFactors=TRUE, colClasses=c("max", "protein code", "molecular feature z score pos"))
set.seed(0)
min_data<-data.frame(z_score_data)[,1:3]
max_data<-data.frame(z_score_data)[,5:7]
print(min_data)
print(max_data)
highlight_df <- z_score_data[z_score_data$protein.code %in% c("YFR034C_idr_3"),]
print(highlight_df)
ggplot(min_data, aes(min_data[,3])) +
  geom_dotplot(binwidth=0.2) +geom_point(data=highlight_df, aes(highlight_df[,3], y=0), color='red')+
  labs(title = "Stacked Dot Plot: Min", x = "Molecular Features Value Minimum", y = "count")
ggplot(min_data, aes(max_data[,3])) +
  geom_dotplot(binwidth=0.127) +geom_point(data=highlight_df, aes(highlight_df[,7], y=0), color='red')+
  labs(title = "Stacked Dot Plot: Max", x = "Molecular Features Value Maximum", y = "count")
summary(min_data) #2nd quartile -4.6
summary(max_data) #4th quartile  7.3
