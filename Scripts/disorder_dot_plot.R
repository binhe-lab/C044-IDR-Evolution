#Lucretia Shumate
#2022
#This code takes IDR percentage prediction and makes a bar chart to show relation to average percent disorder

rm(list=ls())
getwd()
library(ggplot2)
library(dplyr)

disorder_data<-read.csv("disorder_prediction_data.csv", header=TRUE, stringsAsFactors=TRUE)
disorder_data
row.names(disorder_data)<-disorder_data$Species
disorder_data_df<-data.frame(disorder_data[c(1,2,5,6,8)])
disorder_data_df
ggplot(data=disorder_data_df, aes(x=Species, y=Discon_percent_disorder))+geom_bar(position="dodge", stat="identity", color=c("black"), fill=c("deeppink"))+geom_point(data=disorder_data_df, aes(x=Species, y=Avg_percent_disorder), color="black")+theme(axis.text.x=element_text(angle=90))+labs(title="Discon Percent Disorder")
ggplot(data=disorder_data_df, aes(x=Species, y=PONDR_overall_percent_disorder))+geom_bar(position="dodge", stat="identity", color=c("black"), fill=c("deeppink"))+geom_point(data=disorder_data_df, aes(x=Species, y=Avg_percent_disorder), color="black")+theme(axis.text.x=element_text(angle=90))+labs(title="PONDR Percent Disorder")
ggplot(data=disorder_data_df, aes(x=Species, y=RAPID_percent_disorder))+geom_bar(position="dodge", stat="identity", color=c("black"), fill=c("deeppink"))+geom_point(data=disorder_data_df, aes(x=Species, y=Avg_percent_disorder), color="black")+theme(axis.text.x=element_text(angle=90))+labs(title="RAPID Percent Disorder")
ggplot(data=disorder_data_df, aes(x=Species, y=Avg_percent_disorder))+geom_bar(position="dodge", stat="identity", color=c("black"), fill=c("deeppink"))+theme(axis.text.x=element_text(angle=90))+labs(title="AVG Percent Disorder", subtitle="Discon, PONDR, RAPID")

disorder_data_2<-read.csv("disorder_prediction_data_inverted.csv", header=TRUE, stringsAsFactors=FALSE)
disorder_data_2
row.names(disorder_data_2)<-disorder_data_2$Species
disorder_data_2_matrix<-data.matrix(disorder_data_2[c(1,4,5,7), c(2:23)])
disorder_data_2_matrix
par(mar=c(8,3,2,3))
barplot(disorder_data_2_matrix, beside=TRUE, main="Percent Disorder", las=2, cex.names=1, ylab="Percent Disorder (%)", ylim=c(0, 121), col=c("cyan", "deeppink", "darkorchid1", "chartreuse1"), legend.text=rownames(disorder_data_2_matrix), args.legend=list(x="top", ncol=2 ))
