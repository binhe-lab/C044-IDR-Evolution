import math

def t_welch(group1, group2):
    X1=sum(group1)/len(group1)
    X2=sum(group2)/len(group2)
    var_top1=[]
    for i in range(len(group1)):
        var_top1.append((group1[i]-X1)**2)
    var_top2=[]
    for i in range(len(group2)):
        var_top2.append((group2[i]-X2)**2)
    v1=sum(var_top1)/(len(group1)-1)
    v2=sum(var_top2)/(len(group2)-1)
    n1=len(group1)
    n2=len(group2)
    test_stat=(X1-X2)/math.sqrt((v1/n1)+(v2/n2))
    d_freedom=(((v1/n1)+(v2/n2))**2)/((((v1/n1)**2)/(n1-1))+(((v2/n2)**2)/(n2-1)))
    return (test_stat, d_freedom)

#test1=[14, 15, 15, 15, 16, 18, 22, 23, 24, 25, 25] 
#test2=[10, 12, 14, 15, 18, 22, 24, 27, 31, 33, 34, 34, 34]
#print(t_welch(test1, test2))
#(-1.5379022758390941, 18.137377998778444) 

#Glabrata clade (group1), Saccharomyces clade (group2) Discon 
Glabrata_t1_D=[71.482, 69.837, 80.172, 71.579]
Saccharomyces_t1_D=[92.812, 78.526, 86.103, 72.468, 77.07, 92.949]
print("Test 1 Discon: ", t_welch(Glabrata_t1_D, Saccharomyces_t1_D))

#Glabrata clade (group1), Saccharomyces clade (group2) PONDR 
Glabrata_t1_P=[55.16, 64.14, 61.85, 64.84]
Saccharomyces_t1_P=[70, 66.67, 65.26, 68.99, 66.24, 63.14]
print("Test 1 PONDR: ", t_welch(Glabrata_t1_P, Saccharomyces_t1_P))

#Glabrata clade (group1), Saccharomyces clade (group2) RAPID 
Glabrata_t1_R=[53.47, 46.52, 61.85, 47.37]
Saccharomyces_t1_R=[50.62, 46.79, 41.09, 41.77, 48.41, 40.71]
print("Test 1 RAPID: ", t_welch(Glabrata_t1_R, Saccharomyces_t1_R)) 

#Glabrata clade (group1), Saccharomyces clade (group2) Average 
Glabrata_t1_A=[60.04, 60.11, 67.96, 61.26]
Saccharomyces_t1_A=[71.14, 64, 64.15, 61.08, 63.91, 65.5]
print("Test 1 Average: ", t_welch(Glabrata_t1_A, Saccharomyces_t1_A))

#Glabrata clade (group1), Saccharomyces clade (group2) Length of longest disordered region 
Glabrata_t1_L=[71, 71, 89, 103]
Saccharomyces_t1_L=[87, 85, 86, 85, 81, 87]
print("Test 1 Length: ", t_welch(Glabrata_t1_L, Saccharomyces_t1_L))

#Glabrata clade (group1), Saccharomyces clade (group2) Number of disordered segments
Glabrata_t1_N=[11, 10, 9, 8]
Saccharomyces_t1_N=[8, 4, 7, 6, 4, 7]
print("Test 1 Number: ", t_welch(Glabrata_t1_N, Saccharomyces_t1_N)) 

#Glabrata clade (group1), offshoot (group2) Discon
Glabrata_t2_D=[71.482, 69.837, 80.172, 71.579]
Offshoot_t2_D=[67.837, 98.276, 72.793, 75.934, 78.288, 79.31]
print("Test 2 Discon: ", t_welch(Glabrata_t2_D, Offshoot_t2_D))

#Glabrata clade (group1), offshoot (group2) PONDR
Glabrata_t2_P=[55.16, 64.14, 61.85, 64.84]
Offshoot_t2_P=[57.67, 45.02, 72.07, 64.94, 73.28, 66.44]
print("Test 2 PONDR: ", t_welch(Glabrata_t2_P, Offshoot_t2_P))

#Glabrata clade (group1), offshoot (group2) RAPID
Glabrata_t2_R=[53.47, 46.52, 61.85, 47.37]
Offshoot_t2_R=[44.73, 43.68, 42.98, 45.64, 44.05, 61.84]
print("Test 2 RAPID: ", t_welch(Glabrata_t2_R, Offshoot_t2_R)) 

#Glabrata clade (group1), offshoot (group2) Average
Glabrata_t2_A=[60.04, 60.11, 67.96, 61.26]
Offshoot_t2_A=[56.75, 62.32, 62.62, 62.17, 65.21, 69.2]
print("Test 2 Average: ", t_welch(Glabrata_t2_A, Offshoot_t2_A)) 

#Glabrata clade (group1), offshoot (group2) Length of longest disordered region
Glabrata_t2_L=[71, 71, 89, 103]
Offshoot_t2_L=[87, 41, 135, 132, 144, 163]
print("Test 2 Length: ", t_welch(Glabrata_t2_L, Offshoot_t2_L)) 

#Glabrata clade (group1), offshoot (group2) Number of disordered segments
Glabrata_t2_N=[11, 10, 9, 8]
Offshoot_t2_N=[11, 12, 16, 10, 9, 7]
print("Test 2 Number: ", t_welch(Glabrata_t2_N, Offshoot_t2_N)) 

#Glabrata clade (group1), Outgroup (group2) Discon
Glabrata_t3_D=[71.482, 69.837, 80.172, 71.579]
Outgroup_t3_D=[84.137, 73.75, 60.698, 68.017]
print("Test 3 Discon: ", t_welch(Glabrata_t3_D, Outgroup_t3_D))

#Glabrata clade (group1), Outgroup (group2) PONDR
Glabrata_t3_P=[55.16, 64.14, 61.85, 64.84]
Outgroup_t3_P=[68.88, 69.29, 65.86, 68.99]
print("Test 3 PONDR: ", t_welch(Glabrata_t3_P, Outgroup_t3_P))

#Glabrata clade (group1), Outgroup (group2) RAPID
Glabrata_t3_R=[53.47, 46.52, 61.85, 47.37]
Outgroup_t3_R=[52.01, 50.36, 48.86, 44.27]
print("Test 3 RAPID: ", t_welch(Glabrata_t3_R, Outgroup_t3_R))

#Glabrata clade (group1), Outgroup (group2) Average
Glabrata_t3_A=[60.04, 60.11, 67.96, 61.26]
Outgroup_t3_A=[68.34, 64.47, 58.47, 60.43]
print("Test 3 Average: ", t_welch(Glabrata_t3_A, Outgroup_t3_A))

#Glabrata clade (group1), Outgroup (group2) Length longest disordered region
Glabrata_t3_L=[71, 71, 89, 103]
Outgroup_t3_L=[262, 180, 80, 183]
print("Test 3 Length: ", t_welch(Glabrata_t3_L, Outgroup_t3_L))

#Glabrata clade (group1), Outgroup (group2) Number of disordered segments
Glabrata_t3_N=[11, 10, 9, 8]
Outgroup_t3_N=[7, 7, 16, 13]
print("Test 3 Number: ", t_welch(Glabrata_t3_N, Outgroup_t3_N))

#Glabrata clade (group1), All (group2) Discon
Glabrata_t4_D=[71.482, 69.837, 80.172, 71.579]
All_t4_D=[80.307, 67.837, 98.276, 72.793, 75.934, 78.288, 79.31, 92.812, 78.526, 86.103, 72.468, 77.07, 92.949, 84.137, 73.75, 60.698, 68.017]
print("Test 4 Discon: ", t_welch(Glabrata_t4_D, All_t4_D))

#Glabrata clade (group1), All (group2) PONDR
Glabrata_t4_P=[55.16, 64.14, 61.85, 64.84]
All_t4_P=[55.24, 57.67, 45.02, 72.07, 64.94, 73.28, 66.44, 70, 66.67, 65.26, 68.99, 66.24, 63.14, 68.88, 69.29, 65.86, 68.99]
print("Test 4 PONDR: ", t_welch(Glabrata_t4_P, All_t4_P))

#Glabrata clade (group1), All (group2) RAPID
Glabrata_t4_R=[53.47, 46.52, 61.85, 47.37]
All_t4_R=[43.22, 44.73, 43.68, 42.98, 45.64, 44.05, 61.84, 50.62, 46.79, 41.09, 41.77, 48.41, 40.71, 52.01, 50.36, 48.86, 44.27]
print("Test 4 RAPID: ", t_welch(Glabrata_t4_R, All_t4_R))

#Glabrata clade (group1), All (group2) Average
Glabrata_t4_A=[60.04, 60.11, 67.96, 61.26]
All_t4_A=[59.59, 56.75, 62.32, 62.62, 62.17, 65.21, 69.2, 71.14, 64, 64.15, 61.08, 63.91, 65.5, 68.34, 64.47, 58.47, 60.43]
print("Test 4 Average: ", t_welch(Glabrata_t4_A, All_t4_A)) 

#Glabrata clade (group1), All (group2) Length of longest disordered region
Glabrata_t4_L=[71, 71, 89, 103]
All_t4_L=[85, 87, 41, 135, 132, 144, 163, 87, 85, 86, 85, 81, 87, 262, 180, 80, 183]
print("Test 4 Length: ", t_welch(Glabrata_t4_L, All_t4_L))

#Glabrata clade (group1), All (group2) Number of disordered segments
Glabrata_t4_N=[11, 10, 9, 8]
All_t4_N=[10, 11, 12, 16, 10, 9, 7, 8, 4, 7, 6, 4, 7, 7, 7, 16, 13]
print("Test 4 Number: ", t_welch(Glabrata_t4_N, All_t4_N))

#Saccharomyces clade (group1), Outgroup (group2) Discon
Saccharomyces_t5_D=[92.812, 78.526, 86.103, 72.468, 77.07, 92.949]
Outgroup_t5_D=[84.137, 73.75, 60.698, 68.017]
print("Test 5 Discon: ", t_welch(Saccharomyces_t5_D, Outgroup_t5_D))

#Saccharomyces clade (group1), Outgroup (group2) PONDR
Saccharomyces_t5_P=[70, 66.67, 65.26, 68.99, 66.24, 63.14]
Outgroup_t5_P=[68.88, 69.29, 65.86, 68.99]
print("Test 5 PONDR: ", t_welch(Saccharomyces_t5_P, Outgroup_t5_P))

#Saccharomyces clade (group1), Outgroup (group2) RAPID
Saccharomyces_t5_R=[50.62, 46.79, 41.09, 41.77, 48.41, 40.71]
Outgroup_t5_R=[52.01, 50.36, 48.86, 44.27]
print("Test 5 RAPID: ", t_welch(Saccharomyces_t5_R, Outgroup_t5_R))

#Saccharomyces clade (group1), Outgroup (group2) Average
Saccharomyces_t5_A=[71.14, 64, 64.15, 61.08, 63.91, 65.5]
Outgroup_t5_A=[68.34, 64.47, 58.47, 60.43]
print("Test 5 Average: ", t_welch(Saccharomyces_t5_A, Outgroup_t5_A)) 

#Saccharomyces clade (group1), Outgroup (group2) Length longest disordered region
Saccharomyces_t5_L=[87, 85, 86, 85, 81, 87]
Outgroup_t5_L=[262, 180, 80, 183]
print("Test 5 Length: ", t_welch(Saccharomyces_t5_L, Outgroup_t5_L))

#Saccharomyces clade (group1), Outgroup (group2) Number of disordered segments
Saccharomyces_t5_N=[8, 4, 7, 6, 4, 7]
Outgroup_t5_N=[7, 7, 16, 13]
print("Test 5 Number: ", t_welch(Saccharomyces_t5_N, Outgroup_t5_N))


