import math
import csv

#a1=[['sc', ' ', '2.1', 'nan', '5.7', '0', '5', '9'], ['cg', ' ', '2.5', '7', '5.7', '0', '5', '15'], ['kl', ' ', '2', '5', '7', '0', '6', '12']]
#a2=[['sc', ' ', '2', '4', '4', '0', '0', '10.2'], ['cg', ' ', '2.8', '4', '4', '0', '0', '17.2'], ['kl', ' ', '3', '4', '8', '0', '3', '13']]
#average=[2.1999999999999997, 6.0, 6.133333333333333, 0.0, 5.333333333333333, 12.0]
#print(Avg(a1))
#print(Stdev(a1, average))

#species1_avg=[2.1999999999999997, 6.0, 6.133333333333333, 0.0, 5.333333333333333, 12.0]
#species2_avg=[2.6, 4.0, 5.333333333333333, 0.0, 1.0, 13.466666666666667]
#species1_stdev=[0.21602468994692867, 1.0, 0.6128258770283411, 0.0, 0.4714045207910317, 2.449489742783178]
#species2_stdev=[0.5887840577551899, 2.0, 2.048305532764962, 0.0, 4.558264777059114, 3.2290349435499555]
#species1_var=[0.06999999999999999, 2.0, 0.5633333333333332, 0.0, 0.33333333333333337, 9.0]
#species2_var=[0.27999999999999997, 0.0, 5.333333333333333, 0.0, 3.0, 12.413333333333332]
#print(Z_statistic(species1_avg, species1_stdev, species2_avg, species2_stdev))

def file_input(input_file):
    with open(input_file, 'r') as f:
        line_L=[]
        for line in f:
            line_L.append(line.strip())
    split_line_L=[]
    header=line_L[0].split(',')
    for i in range(1,len(line_L)):
        split_line_L.append(line_L[i].split('\t'))
    #print(split_line_L)
    sheet=[]
    for i in range(len(split_line_L)):
        for j in range(len(split_line_L[i])):
            sheet.append(split_line_L[i][j].split(','))
    print(sheet) 
    return sheet

def Avg(Group1):
    AVG=[]
    avg_temp=[]
    i=0
    for j in range(2, len(Group1[i])):
        for i in range(len(Group1)):
            if Group1[i][j]=='-':
                i+=1
            elif Group1[i][j]=='nan':
                i+=1
            else:
                avg_temp.append(float(Group1[i][j]))
                i+=1
                j+=0
        #print(avg_temp)
        if len(avg_temp)>0:
            AVG.append(sum(avg_temp)/len(avg_temp))
            avg_temp.clear()
        else:
            AVG.append(0)
            avg_temp.clear()            
        #print("AVG: ", AVG)
    return AVG
    
def Stdev(Group1, avg):
    StDev=[]
    stdev_temp=[]
    count=0
    i=0
    for j in range(2, len(Group1[i])):
        for i in range(len(Group1)):
            if Group1[i][j]=='-':
                i+=1
            elif Group1[i][j]=='nan':
                i+=1
            else:
                stdev_temp.append(float(Group1[i][j]))
                count+=1
                i+=1
                j+=0
        #print(stdev_temp)
        m=j-2
        summation=0
        for k in range(len(stdev_temp)):
            summation+=((float(stdev_temp[k])-float(avg[m]))**2)
            #print("avg", avg[m])
        if len(stdev_temp)>0:
            StDev.append([math.sqrt(summation/len(stdev_temp)), count])
            stdev_temp.clear()
            count=0
            m=+1
        else:
            StDev.append([0, count])
            stdev_temp.clear()
            count=0
            m+=1
        #print("St. Dev: ", StDev)
    return StDev  

def Var(Group1, avg):
    VAR=[]
    var_temp=[]
    count=0
    i=0
    for j in range(2, len(Group1[i])):
        for i in range(len(Group1)):
            if Group1[i][j]=='-':
                i+=1
            elif Group1[i][j]=='nan':
                i+=1
            else:
                var_temp.append(float(Group1[i][j]))
                count+=1
                i+=1
                j+=0
        print(var_temp)
        m=j-2
        summation=0
        for k in range(len(var_temp)):
            summation+=((float(var_temp[k])-float(avg[m]))**2)
            #print("avg", avg[m])
        if len(var_temp)>0:
            VAR.append([summation/(count-1), count])
            var_temp.clear()
            count=0
            m=+1
        else: 
            VAR.append([0, count])
            var_temp.clear()
            count=0
            m+=1
        #print("St. Dev: ", StDev)
    return VAR

def Z_statistic(S1_A, S1_S, S2_A, S2_S):
    Z_STAT=[]
    for i in range(len(S1_A)):
        if S1_S[i][0]==0.0 and S2_S[i][0]==0.0:
            Z_STAT.append('Zero')
            i+=1
        elif S1_S[i][1]==0.0 or S2_S[i][1]==0.0:
            Z_STAT.append("ONE")
            i+=1
        else:
            Z_top=float(S1_A[i])-float(S2_A[i])
            Dis1=((float(S1_S[i][0]))/math.sqrt(S1_S[i][1]))**2
            Dis2=((float(S2_S[i][0]))/math.sqrt(S2_S[i][1]))**2
            Z_bottom=math.sqrt(Dis1+Dis2)
            Z_statistic=Z_top/Z_bottom
            Z_STAT.append(Z_statistic)
    return Z_STAT

def welch_t_test(X1, X2, V1, V2):
    welch=[]
    results=[]
    database=[12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.16, 2.145, 2.131, 2.12, 2.11, 2.101, 2.093, 2.086, 2.08, 2.074, 2.069, 2.064, 2.06, 2.056, 2.052, 2.048, 2.045, 2.042, 2, 1.98, 1.962, 1.96]
    for i in range(len(X1)):
        if V1[i][0]==0.0 and V2[i][0]==0.0:
            welch.append("ZERO")
            i+=1
        elif V1[i][1]==0.0 or V2[i][1]==0.0:
            welch.append("ONE")
            i+=1
        else:
            test_stat=(X1[i]-X2[i])/math.sqrt((V1[i][0]/V1[i][1])+(V2[i][0]/V2[i][1]))
            d_freedom=(((V1[i][0]/V1[i][1])+(V2[i][0]/V2[i][1]))**2)/((((V1[i][0]/V1[i][1])**2)/(V1[i][1]-1))+(((V2[i][0]/V2[i][1])**2)/(V2[i][1]-1)))
            welch.append([test_stat, d_freedom])
    print(welch)
    for i in range(len(welch)):
        if welch[i]=='ZERO':
            results.append("ZERO")
            i+=1
        elif welch[i]=='ONE':
            results.append("ONE")
        else:
            if welch[i][1]<=30:
                if abs(welch[i][0])>=database[int(welch[i][1])-1]:
                    results.append("Reject null")
                else:
                    results.append("Fail")
            elif 30<welch[i][1]<=60:
                if abs(welch[i][0])>=database[-4]:
                    results.append("Reject null")
                else:
                    results.append("Fail")
            elif 60<welch[i][1]<=120:
                if abs(welch[i][0])>=database[-3]:
                    results.append("Reject null")
                else:
                    results.append("Fail")
            elif 120<welch[i][1]<=1000:
                if abs(welch[i][0])>=database[-2]:
                    results.append("Reject null")
                else:
                    results.append("Fail")
            else:
                if abs(welch[i][0])>=database[-1]:
                    results.append("Reject null")
                else:
                    results.append("Fail")            
    return results
    
if __name__ == "__main__":
    #Control files
    Full_sequence_file="IDR_molecular_features_data_Full_sequence.csv"
    Full_sequence_data=file_input(Full_sequence_file)
    Attempt_4_file="IDR_molecular_features_data_Attempt4_10_10.csv"
    Attempt_4_data=file_input(Attempt_4_file)
    
    #Whole IDR Sequence files
    Attempt1_file="IDR_molecular_features_data_Attempt1_08_28.csv"
    Attempt1_data=file_input(Attempt1_file)
    Attempt2_file="IDR_molecular_features_data.csv"
    Attempt2_data=file_input(Attempt2_file)
    Attempt3_M1_file="IDR_molecular_features_data_Attempt3_09_20_M1.csv"
    Attempt3_M1_data=file_input(Attempt3_M1_file)
    Attempt3_M2_file="IDR_molecular_features_data_Attempt3_09_20_M2.csv"
    Attempt3_M2_data=file_input(Attempt3_M2_file)
    Attempt3_M3_file="IDR_molecular_features_data_Attempt3_09_20_M3.csv"
    Attempt3_M3_data=file_input(Attempt3_M3_file)
    Attempt3_1_M3_1_file="IDR_molecular_features_data_Attempt3.1_10_10_M3.1.csv"
    Attempt3_1_M3_1_data=file_input(Attempt3_1_M3_1_file)
    Attempt3_1_M3_2_file="IDR_molecular_features_data_Attempt3.1_10_10_M3.2.csv"
    Attempt3_1_M3_2_data=file_input(Attempt3_1_M3_2_file)
    
    #Pho4 Segment files
    Attempt3_M4_1_file="IDR_molecular_features_data_Attempt3_09_20_M4.1.csv"
    Attempt3_M4_1_data=file_input(Attempt3_M4_1_file)
    Attempt3_1_M4_2_file="IDR_molecular_features_data_Attempt3.1_10_10_M4.2.csv"
    Attempt3_1_M4_2_data=file_input(Attempt3_1_M4_2_file)
    Attempt3_1_M4_3_file="IDR_molecular_features_data_Attempt3.1_10_10_M4.3.csv"
    Attempt3_1_M4_3_data=file_input(Attempt3_1_M4_3_file)
    Attempt3_M4_4_file="IDR_molecular_features_data_Attempt3_09_20_M4.4.csv"
    Attempt3_M4_4_data=file_input(Attempt3_M4_4_file)
    Attempt3_1_M4_5_file="IDR_molecular_features_data_Attempt3.1_10_10_M4.5.csv"
    Attempt3_1_M4_5_data=file_input(Attempt3_1_M4_5_file)
    Attempt3_1_M4_5_1_file="IDR_molecular_features_data_Attempt3.1_10_10_M4.5.1.csv"
    Attempt3_1_M4_5_1_data=file_input(Attempt3_1_M4_5_1_file)
    
    # Sepecies numbering: S. cerevisiae [0], C. albicans [1], C. glabrata [2], C. subhashii [3], D. hansenii [4], K. lactis [5], L. kluyveri [6], L. waltii [7], N. bacillisporus [8], N. bracarensis [9], N. delphensis [10], N. nivariensis [11], Nk. castellii [12], Nm. castellii [13], S. arboricola [14], S. eubayanus [15], S. kudriavzevii [16], S. paradoxus [17]. S. pastorianus [18], Y. lipolytica [19], Z. parabailii [20]
    #Pho2 dependent: S. cerevisiae, C. albicans [], C. subhashii, D. hansenii, K. lactis, L. kluyveri, L. waltii, N. bacillisporus, Nk. castellii, Nm. castellii, S. arboricola, S. eubayanus, S. kudriavzevii, S. paradoxus, S. pastorianus, Y. lipolytica, Z. parabailii 
    #Pho2 independent: C. albicans, C. glabrata, N. bracarensis, N. delphensis, N. nivariensis
    
    #C. glabrata vs S. cerevisiae. a1, a2, a3 m1, a3 m2, a3 m3, a3.1 m3.1, a3.1 m3.2
    C_glabrata=[Attempt1_data[2], Attempt2_data[2], Attempt3_M1_data[2], Attempt3_M2_data[2], Attempt3_M3_data[2],Attempt3_1_M3_1_data[2], Attempt3_1_M3_2_data[2]]
    S_cerevisiae=[Attempt1_data[0], Attempt2_data[0], Attempt3_M1_data[0], Attempt3_M2_data[0], Attempt3_M3_data[0],Attempt3_1_M3_1_data[0], Attempt3_1_M3_2_data[0]]
    C_glabrata_avg=Avg(C_glabrata)
    C_glabrata_stdev=Stdev(C_glabrata, C_glabrata_avg)
    C_glabrata_var=Var(C_glabrata, C_glabrata_avg)
    S_cerevisiae_avg=Avg(S_cerevisiae)
    S_cerevisiae_stdev=Stdev(S_cerevisiae, S_cerevisiae_avg)
    S_cerevisiae_var=Var(S_cerevisiae, S_cerevisiae_avg)
    print("The Z statisitics for all full IDR sequence attempts between C. glabrata and S. cerevisiae is: ", Z_statistic(C_glabrata_avg, C_glabrata_stdev, S_cerevisiae_avg, S_cerevisiae_stdev))
    print("The Welch's t test results for all full IDR sequence attempts between C. glabrata and S. cerevisiae are: ", welch_t_test(C_glabrata_avg, S_cerevisiae_avg, C_glabrata_var, S_cerevisiae_var))
    
    #C. glabrata vs S. cerevisiae more precise. A3m1, a3m2, a3.1 m3.2
    C_glabrata_precise=[Attempt3_M1_data[2], Attempt3_M2_data[2], Attempt3_1_M3_2_data[2]]
    S_cerevisiae_precise=[Attempt3_M1_data[0], Attempt3_M2_data[0], Attempt3_1_M3_2_data[0]]
    C_glabrata_avg_p=Avg(C_glabrata_precise)
    C_glabrata_stdev_p=Stdev(C_glabrata_precise, C_glabrata_avg_p)
    C_glabrata_var_p=Var(C_glabrata_precise, C_glabrata_avg_p)
    S_cerevisiae_avg_p=Avg(S_cerevisiae_precise)
    S_cerevisiae_stdev_p=Stdev(S_cerevisiae_precise, S_cerevisiae_avg_p)
    S_cerevisiae_var_p=Var(S_cerevisiae_precise, S_cerevisiae_avg_p)
    print("The Z statistics for a precise full IDR sequence between C. glabrata and S. cerevisiae is: ", Z_statistic(C_glabrata_avg_p, C_glabrata_stdev_p, S_cerevisiae_avg_p, S_cerevisiae_stdev_p))
    print("The Welch's t test results for a precise full IDR sequence between C. glabrata and S. cerevisiae are: ", welch_t_test(C_glabrata_avg_p, S_cerevisiae_avg_p, C_glabrata_var_p, S_cerevisiae_var_p)) 
    
    #Pho2 independent vs Pho2 dependent a1, a2, a3 m1, a3 m2, a3 m3, a3.1 m3.1, a3.1 m3.2
    independent=[Attempt1_data[1], Attempt1_data[2], Attempt1_data[9], Attempt1_data[10], Attempt1_data[11], Attempt2_data[1], Attempt2_data[2], Attempt2_data[9], Attempt2_data[10], Attempt2_data[11], Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11], Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11], Attempt3_M3_data[1], Attempt3_M3_data[2], Attempt3_M3_data[9], Attempt3_M3_data[10], Attempt3_M3_data[11], Attempt3_1_M3_1_data[1], Attempt3_1_M3_1_data[2], Attempt3_1_M3_1_data[9], Attempt3_1_M3_1_data[10], Attempt3_1_M3_1_data[11], Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    dependent=[Attempt1_data[0], Attempt1_data[3], Attempt1_data[4], Attempt1_data[5], Attempt1_data[6], Attempt1_data[7], Attempt1_data[8], Attempt1_data[12], Attempt1_data[13], Attempt1_data[14], Attempt1_data[15], Attempt1_data[16], Attempt1_data[17], Attempt1_data[18], Attempt1_data[19], Attempt1_data[20], Attempt2_data[0], Attempt2_data[3], Attempt2_data[4], Attempt2_data[5], Attempt2_data[6], Attempt2_data[7], Attempt2_data[8], Attempt2_data[12], Attempt2_data[13], Attempt2_data[14], Attempt2_data[15], Attempt2_data[16], Attempt2_data[17], Attempt2_data[18], Attempt2_data[19], Attempt2_data[20], Attempt3_M1_data[0], Attempt3_M1_data[3], Attempt3_M1_data[4], Attempt3_M1_data[5], Attempt3_M1_data[6], Attempt3_M1_data[7], Attempt3_M1_data[8], Attempt3_M1_data[12], Attempt3_M1_data[13], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18], Attempt3_M1_data[19], Attempt3_M1_data[20], Attempt3_M2_data[0], Attempt3_M2_data[3], Attempt3_M2_data[4], Attempt3_M2_data[5], Attempt3_M2_data[6], Attempt3_M2_data[7], Attempt3_M2_data[8], Attempt3_M2_data[12], Attempt3_M2_data[13], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18], Attempt3_M2_data[19], Attempt3_M2_data[20], Attempt3_M3_data[0], Attempt3_M3_data[3], Attempt3_M3_data[4], Attempt3_M3_data[5], Attempt3_M3_data[6], Attempt3_M3_data[7], Attempt3_M3_data[8], Attempt3_M3_data[12], Attempt3_M3_data[13], Attempt3_M3_data[14], Attempt3_M3_data[15], Attempt3_M3_data[16], Attempt3_M3_data[17], Attempt3_M3_data[18], Attempt3_M3_data[19], Attempt3_M3_data[20], Attempt3_1_M3_1_data[0], Attempt3_1_M3_1_data[3], Attempt3_1_M3_1_data[4], Attempt3_1_M3_1_data[5], Attempt3_1_M3_1_data[6], Attempt3_1_M3_1_data[7], Attempt3_1_M3_1_data[8], Attempt3_1_M3_1_data[12], Attempt3_1_M3_1_data[13], Attempt3_1_M3_1_data[14], Attempt3_1_M3_1_data[15], Attempt3_1_M3_1_data[16], Attempt3_1_M3_1_data[17], Attempt3_1_M3_1_data[18], Attempt3_1_M3_1_data[19], Attempt3_1_M3_1_data[20], Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[3], Attempt3_1_M3_2_data[4], Attempt3_1_M3_2_data[5], Attempt3_1_M3_2_data[6], Attempt3_1_M3_2_data[7], Attempt3_1_M3_2_data[8], Attempt3_1_M3_2_data[12], Attempt3_1_M3_2_data[13], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18], Attempt3_1_M3_2_data[19], Attempt3_1_M3_2_data[20]]
    dependent_avg=Avg(dependent)
    dependent_stdev=Stdev(dependent, dependent_avg)
    dependent_var=Var(dependent, dependent_avg)
    independent_avg=Avg(independent)
    independent_stdev=Stdev(independent, independent_avg)
    independent_var=Var(independent, independent_avg)
    print("The Z statistics for all full IDR sequence attempts between the Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_avg, independent_stdev, dependent_avg, dependent_stdev)) 
    print("The Welch's t test results for all full IDR sequence attempts between the Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_avg, dependent_avg, independent_var, dependent_var))
    
    #Pho2 independent vs Pho2 dependent A3m1, a3m2, a3.1 m3.2
    independent_precise=[Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11], Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11], Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    dependent_precise=[Attempt3_M1_data[0], Attempt3_M1_data[3], Attempt3_M1_data[4], Attempt3_M1_data[5], Attempt3_M1_data[6], Attempt3_M1_data[7], Attempt3_M1_data[8], Attempt3_M1_data[12], Attempt3_M1_data[13], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18], Attempt3_M1_data[19], Attempt3_M1_data[20], Attempt3_M2_data[0], Attempt3_M2_data[3], Attempt3_M2_data[4], Attempt3_M2_data[5], Attempt3_M2_data[6], Attempt3_M2_data[7], Attempt3_M2_data[8], Attempt3_M2_data[12], Attempt3_M2_data[13], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18], Attempt3_M2_data[19], Attempt3_M2_data[20], Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[3], Attempt3_1_M3_2_data[4], Attempt3_1_M3_2_data[5], Attempt3_1_M3_2_data[6], Attempt3_1_M3_2_data[7], Attempt3_1_M3_2_data[8], Attempt3_1_M3_2_data[12], Attempt3_1_M3_2_data[13], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18], Attempt3_1_M3_2_data[19], Attempt3_1_M3_2_data[20]]
    dependent_avg_p=Avg(dependent_precise)
    dependent_stdev_p=Stdev(dependent_precise, dependent_avg_p)
    dependent_var_p=Var(dependent_precise, dependent_avg_p)
    independent_avg_p=Avg(independent_precise)
    independent_stdev_p=Stdev(independent_precise, independent_avg_p)
    independent_var_p=Var(independent_precise, independent_avg_p)
    print("The Z statistics for a presice full IDR sequence between the Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_avg_p, independent_stdev_p, dependent_avg_p, dependent_stdev_p))
    print("The Welch's t test results for a precise full IDR sequence between the Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_avg_p, dependent_avg_p, independent_var_p, dependent_var_p))  
    
    #Pho2 independent vs Pho2 dependent control full sequence
    independent_full=[Full_sequence_data[1], Full_sequence_data[2], Full_sequence_data[9], Full_sequence_data[10], Full_sequence_data[11]]
    dependent_full=[Full_sequence_data[0], Full_sequence_data[3], Full_sequence_data[4], Full_sequence_data[5], Full_sequence_data[6], Full_sequence_data[7], Full_sequence_data[8], Full_sequence_data[12], Full_sequence_data[13], Full_sequence_data[14], Full_sequence_data[15], Full_sequence_data[16], Full_sequence_data[17], Full_sequence_data[18], Full_sequence_data[19], Full_sequence_data[20]]
    dependent_full_avg=Avg(dependent_full)
    dependent_full_stdev=Stdev(dependent_full, dependent_full_avg)
    dependent_full_var=Var(dependent_full, dependent_full_avg)
    independent_full_avg=Avg(independent_full)
    independent_full_stdev=Stdev(independent_full, independent_full_avg)
    independent_full_var=Var(independent_full, independent_full_avg)
    print("The Z statistics for the full sequence control between the Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_full_avg, independent_full_stdev, dependent_full_avg, dependent_full_stdev))
    print("The Welch's t test results for the full sequence control between the Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_full_avg, dependent_full_avg, independent_full_var, dependent_full_var))
    
    #Pho2 independent vs Pho2 dependent control SC based IDR region Attempt 4
    independent_a4=[Attempt_4_data[1], Attempt_4_data[2], Attempt_4_data[9], Attempt_4_data[10], Attempt_4_data[11]]
    dependent_a4=[Attempt_4_data[0], Attempt_4_data[3], Attempt_4_data[4], Attempt_4_data[5], Attempt_4_data[6], Attempt_4_data[7], Attempt_4_data[8], Attempt_4_data[12], Attempt_4_data[13], Attempt_4_data[14], Attempt_4_data[15], Attempt_4_data[16], Attempt_4_data[17], Attempt_4_data[18], Attempt_4_data[19], Attempt_4_data[20]]
    dependent_a4_avg=Avg(dependent_a4)
    dependent_a4_stdev=Stdev(dependent_a4, dependent_a4_avg)
    dependent_a4_var=Var(dependent_a4, dependent_a4_avg)
    independent_a4_avg=Avg(independent_a4)
    independent_a4_stdev=Stdev(independent_a4, independent_a4_avg)
    independent_a4_var=Var(independent_a4, independent_a4_avg)
    print("The Z statistics for the IDR region based on S. cerevisiae control between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a4_avg, independent_a4_stdev, dependent_a4_avg, dependent_a4_stdev))
    print("The Welch's t test results for the IDR region based on S. cerevisiae control between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a4_avg, dependent_a4_avg, independent_a4_var, dependent_a4_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 1
    independent_a1=[Attempt1_data[1], Attempt1_data[2], Attempt1_data[9], Attempt1_data[10], Attempt1_data[11]]
    dependent_a1=[Attempt1_data[0], Attempt1_data[3], Attempt1_data[4], Attempt1_data[5], Attempt1_data[6], Attempt1_data[7], Attempt1_data[8], Attempt1_data[12], Attempt1_data[13], Attempt1_data[14], Attempt1_data[15], Attempt1_data[16], Attempt1_data[17], Attempt1_data[18], Attempt1_data[19], Attempt1_data[20]]
    dependent_a1_avg=Avg(dependent_a1)
    dependent_a1_stdev=Stdev(dependent_a1, dependent_a1_avg)
    dependent_a1_var=Var(dependent_a1, dependent_a1_avg)
    independent_a1_avg=Avg(independent_a1)
    independent_a1_stdev=Stdev(independent_a1, independent_a1_avg)
    independent_a1_var=Var(independent_a1, independent_a1_avg)
    print("The Z statistics for the IDR sequence attempt 1 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a1_avg, independent_a1_stdev, dependent_a1_avg, dependent_a1_stdev))
    print("The Welch's t test results for the IDR sequence attempt 1 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a1_avg, dependent_a1_avg, independent_a1_var, dependent_a1_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 2
    independent_a2=[Attempt2_data[1], Attempt2_data[2], Attempt2_data[9], Attempt2_data[10], Attempt2_data[11]]
    dependent_a2=[Attempt2_data[0], Attempt2_data[3], Attempt2_data[4], Attempt2_data[5], Attempt2_data[6], Attempt2_data[7], Attempt2_data[8], Attempt2_data[12], Attempt2_data[13], Attempt2_data[14], Attempt2_data[15], Attempt2_data[16], Attempt2_data[17], Attempt2_data[18], Attempt2_data[19], Attempt2_data[20]]
    dependent_a2_avg=Avg(dependent_a2)
    dependent_a2_stdev=Stdev(dependent_a2, dependent_a2_avg)
    dependent_a2_var=Var(dependent_a2, dependent_a2_avg)
    independent_a2_avg=Avg(independent_a2)
    independent_a2_stdev=Stdev(independent_a2, independent_a2_avg)
    independent_a2_var=Var(independent_a2, independent_a2_avg)
    print("The Z statistics for the IDR sequence attempt 2 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a2_avg, independent_a2_stdev, dependent_a2_avg, dependent_a2_stdev))
    print("The Welch's t test results for the IDR sequence attempt 2 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a2_avg, dependent_a2_avg, independent_a2_var, dependent_a2_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3 Method 1
    independent_a3_m1=[Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11]]
    dependent_a3_m1=[Attempt3_M1_data[0], Attempt3_M1_data[3], Attempt3_M1_data[4], Attempt3_M1_data[5], Attempt3_M1_data[6], Attempt3_M1_data[7], Attempt3_M1_data[8], Attempt3_M1_data[12], Attempt3_M1_data[13], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18], Attempt3_M1_data[19], Attempt3_M1_data[20]]
    dependent_a3_m1_avg=Avg(dependent_a3_m1)
    dependent_a3_m1_stdev=Stdev(dependent_a3_m1, dependent_a3_m1_avg)
    dependent_a3_m1_var=Var(dependent_a3_m1, dependent_a3_m1_avg)
    independent_a3_m1_avg=Avg(independent_a3_m1)
    independent_a3_m1_stdev=Stdev(independent_a3_m1, independent_a3_m1_avg)
    independent_a3_m1_var=Var(independent_a3_m1, independent_a3_m1_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 1 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a3_m1_avg, independent_a3_m1_stdev, dependent_a3_m1_avg, dependent_a3_m1_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3 method 1 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a3_m1_avg, dependent_a3_m1_avg, independent_a3_m1_var, dependent_a3_m1_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3 Method 2
    independent_a3_m2=[Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11]]
    dependent_a3_m2=[Attempt3_M2_data[0], Attempt3_M2_data[3], Attempt3_M2_data[4], Attempt3_M2_data[5], Attempt3_M2_data[6], Attempt3_M2_data[7], Attempt3_M2_data[8], Attempt3_M2_data[12], Attempt3_M2_data[13], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18], Attempt3_M2_data[19], Attempt3_M2_data[20]]
    dependent_a3_m2_avg=Avg(dependent_a3_m2)
    dependent_a3_m2_stdev=Stdev(dependent_a3_m2, dependent_a3_m2_avg)
    dependent_a3_m2_var=Var(dependent_a3_m2, dependent_a3_m2_avg)
    independent_a3_m2_avg=Avg(independent_a3_m2)
    independent_a3_m2_stdev=Stdev(independent_a3_m2, independent_a3_m2_avg)
    independent_a3_m2_var=Var(independent_a3_m2, independent_a3_m2_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 2 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a3_m2_avg, independent_a3_m2_stdev, dependent_a3_m2_avg, dependent_a3_m2_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3 method 2 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a3_m2_avg, dependent_a3_m2_avg, independent_a3_m2_var, dependent_a3_m2_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3 Method 3
    independent_a3_m3=[Attempt3_M3_data[1], Attempt3_M3_data[2], Attempt3_M3_data[9], Attempt3_M3_data[10], Attempt3_M3_data[11]]
    dependent_a3_m3=[Attempt3_M3_data[0], Attempt3_M3_data[3], Attempt3_M3_data[4], Attempt3_M3_data[5], Attempt3_M3_data[6], Attempt3_M3_data[7], Attempt3_M3_data[8], Attempt3_M3_data[12], Attempt3_M3_data[13], Attempt3_M3_data[14], Attempt3_M3_data[15], Attempt3_M3_data[16], Attempt3_M3_data[17], Attempt3_M3_data[18], Attempt3_M3_data[19], Attempt3_M3_data[20]]
    dependent_a3_m3_avg=Avg(dependent_a3_m3)
    dependent_a3_m3_stdev=Stdev(dependent_a3_m3, dependent_a3_m3_avg)
    dependent_a3_m3_var=Var(dependent_a3_m3, dependent_a3_m3_avg)
    independent_a3_m3_avg=Avg(independent_a3_m3)
    independent_a3_m3_stdev=Stdev(independent_a3_m3, independent_a3_m3_avg)
    independent_a3_m3_var=Var(independent_a3_m3, independent_a3_m3_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 3 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a3_m3_avg, independent_a3_m3_stdev, dependent_a3_m3_avg, dependent_a3_m3_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3 method 3 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a3_m3_avg, dependent_a3_m3_avg, independent_a3_m3_var, dependent_a3_m3_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3.1 Method 3.1
    independent_a31_m31=[Attempt3_1_M3_1_data[1], Attempt3_1_M3_1_data[2], Attempt3_1_M3_1_data[9], Attempt3_1_M3_1_data[10], Attempt3_1_M3_1_data[11]]
    dependent_a31_m31=[Attempt3_1_M3_1_data[0], Attempt3_1_M3_1_data[3], Attempt3_1_M3_1_data[4], Attempt3_1_M3_1_data[5], Attempt3_1_M3_1_data[6], Attempt3_1_M3_1_data[7], Attempt3_1_M3_1_data[8], Attempt3_1_M3_1_data[12], Attempt3_1_M3_1_data[13], Attempt3_1_M3_1_data[14], Attempt3_1_M3_1_data[15], Attempt3_1_M3_1_data[16], Attempt3_1_M3_1_data[17], Attempt3_1_M3_1_data[18], Attempt3_1_M3_1_data[19], Attempt3_1_M3_1_data[20]]
    dependent_a31_m31_avg=Avg(dependent_a31_m31)
    dependent_a31_m31_stdev=Stdev(dependent_a31_m31, dependent_a31_m31_avg)
    dependent_a31_m31_var=Var(dependent_a31_m31, dependent_a31_m31_avg)
    independent_a31_m31_avg=Avg(independent_a31_m31)
    independent_a31_m31_stdev=Stdev(independent_a31_m31, independent_a31_m31_avg)
    independent_a31_m31_var=Var(independent_a31_m31, independent_a31_m31_avg)
    print("The Z statistics for the IDR sequence attempt 3.1 method 3.1 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m31_avg, independent_a31_m31_stdev, dependent_a31_m31_avg, dependent_a31_m31_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3.1 method 3.1 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m31_avg, dependent_a31_m31_avg, independent_a31_m31_var, dependent_a31_m31_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3.1 Method 3.2
    independent_a31_m32=[Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    dependent_a31_m32=[Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[3], Attempt3_1_M3_2_data[4], Attempt3_1_M3_2_data[5], Attempt3_1_M3_2_data[6], Attempt3_1_M3_2_data[7], Attempt3_1_M3_2_data[8], Attempt3_1_M3_2_data[12], Attempt3_1_M3_2_data[13], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18], Attempt3_1_M3_2_data[19], Attempt3_1_M3_2_data[20]]
    dependent_a31_m32_avg=Avg(dependent_a31_m32)
    dependent_a31_m32_stdev=Stdev(dependent_a31_m32, dependent_a31_m32_avg)
    dependent_a31_m32_var=Var(dependent_a31_m32, dependent_a31_m32_avg)
    independent_a31_m32_avg=Avg(independent_a31_m32)
    independent_a31_m32_stdev=Stdev(independent_a31_m32, independent_a31_m32_avg)
    independent_a31_m32_var=Var(independent_a31_m32, independent_a31_m32_avg)
    print("The Z statistic for the IDR sequence attempt 3.1 method 3.2 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m32_avg, independent_a31_m32_stdev, dependent_a31_m32_avg, dependent_a31_m32_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3.1 method 3.2 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m32_avg, dependent_a31_m32_avg, independent_a31_m32_var, dependent_a31_m32_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3 Method 4.1
    independent_a3_m41=[Attempt3_M4_1_data[1], Attempt3_M4_1_data[2], Attempt3_M4_1_data[9], Attempt3_M4_1_data[10], Attempt3_M4_1_data[11]]
    dependent_a3_m41=[Attempt3_M4_1_data[0], Attempt3_M4_1_data[3], Attempt3_M4_1_data[4], Attempt3_M4_1_data[5], Attempt3_M4_1_data[6], Attempt3_M4_1_data[7], Attempt3_M4_1_data[8], Attempt3_M4_1_data[12], Attempt3_M4_1_data[13], Attempt3_M4_1_data[14], Attempt3_M4_1_data[15], Attempt3_M4_1_data[16], Attempt3_M4_1_data[17], Attempt3_M4_1_data[18], Attempt3_M4_1_data[19], Attempt3_M4_1_data[20]]
    dependent_a3_m41_avg=Avg(dependent_a3_m41)
    dependent_a3_m41_stdev=Stdev(dependent_a3_m41, dependent_a3_m41_avg)
    dependent_a3_m41_var=Var(dependent_a3_m41, dependent_a3_m41_avg)
    independent_a3_m41_avg=Avg(independent_a3_m41)
    independent_a3_m41_stdev=Stdev(independent_a3_m41, independent_a3_m41_avg)
    independent_a3_m41_var=Var(independent_a3_m41, independent_a3_m41_avg)
    print("The Z statistics for the Pho4 segment #1 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a3_m41_avg, independent_a3_m41_stdev, dependent_a3_m41_avg, dependent_a3_m41_stdev))
    print("The Welch's t test results for the Pho4 segment #1 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a3_m41_avg, dependent_a3_m41_avg, independent_a3_m41_var, dependent_a3_m41_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3.1 Method 4.2
    independent_a31_m42=[Attempt3_1_M4_2_data[1], Attempt3_1_M4_2_data[2], Attempt3_1_M4_2_data[9], Attempt3_1_M4_2_data[10], Attempt3_1_M4_2_data[11]]
    dependent_a31_m42=[Attempt3_1_M4_2_data[0], Attempt3_1_M4_2_data[3], Attempt3_1_M4_2_data[4], Attempt3_1_M4_2_data[5], Attempt3_1_M4_2_data[6], Attempt3_1_M4_2_data[7], Attempt3_1_M4_2_data[8], Attempt3_1_M4_2_data[12], Attempt3_1_M4_2_data[13], Attempt3_1_M4_2_data[14], Attempt3_1_M4_2_data[15], Attempt3_1_M4_2_data[16], Attempt3_1_M4_2_data[17], Attempt3_1_M4_2_data[18], Attempt3_1_M4_2_data[19], Attempt3_1_M4_2_data[20]]
    dependent_a31_m42_avg=Avg(dependent_a31_m42)
    dependent_a31_m42_stdev=Stdev(dependent_a31_m42, dependent_a31_m42_avg)
    dependent_a31_m42_var=Var(dependent_a31_m42, dependent_a31_m42_avg)
    independent_a31_m42_avg=Avg(independent_a31_m42)
    independent_a31_m42_stdev=Stdev(independent_a31_m42, independent_a31_m42_avg)
    independent_a31_m42_var=Var(independent_a31_m42, independent_a31_m42_avg)
    print("The Z statistics for the Pho4 segment #2 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m42_avg, independent_a31_m42_stdev, dependent_a31_m42_avg, dependent_a31_m42_stdev))
    print("The Welch's t test results for the Pho4 segment #2 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m42_avg, dependent_a31_m42_avg, independent_a31_m42_var, dependent_a31_m42_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3.1 Method 4.3
    independent_a31_m43=[Attempt3_1_M4_3_data[1], Attempt3_1_M4_3_data[2], Attempt3_1_M4_3_data[9], Attempt3_1_M4_3_data[10], Attempt3_1_M4_3_data[11]]
    dependent_a31_m43=[Attempt3_1_M4_3_data[0], Attempt3_1_M4_3_data[3], Attempt3_1_M4_3_data[4], Attempt3_1_M4_3_data[5], Attempt3_1_M4_3_data[6], Attempt3_1_M4_3_data[7], Attempt3_1_M4_3_data[8], Attempt3_1_M4_3_data[12], Attempt3_1_M4_3_data[13], Attempt3_1_M4_3_data[14], Attempt3_1_M4_3_data[15], Attempt3_1_M4_3_data[16], Attempt3_1_M4_3_data[17], Attempt3_1_M4_3_data[18], Attempt3_1_M4_3_data[19], Attempt3_1_M4_3_data[20]]
    dependent_a31_m43_avg=Avg(dependent_a31_m43)
    dependent_a31_m43_stdev=Stdev(dependent_a31_m43, dependent_a31_m43_avg)
    dependent_a31_m43_var=Var(dependent_a31_m43, dependent_a31_m43_avg)
    independent_a31_m43_avg=Avg(independent_a31_m43)
    independent_a31_m43_stdev=Stdev(independent_a31_m43, independent_a31_m43_avg)
    independent_a31_m43_var=Var(independent_a31_m43, independent_a31_m43_avg)
    print("The Z statistics for the Pho4 segment #3 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m43_avg, independent_a31_m43_stdev, dependent_a31_m43_avg, dependent_a31_m43_stdev))
    print("The Welch's t test results for the Pho4 segment #3 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m43_avg, dependent_a31_m43_avg, independent_a31_m43_var, dependent_a31_m43_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3 Method 4.4
    independent_a3_m44=[Attempt3_M4_4_data[1], Attempt3_M4_4_data[2], Attempt3_M4_4_data[9], Attempt3_M4_4_data[10], Attempt3_M4_4_data[11]]
    dependent_a3_m44=[Attempt3_M4_4_data[0], Attempt3_M4_4_data[3], Attempt3_M4_4_data[4], Attempt3_M4_4_data[5], Attempt3_M4_4_data[6], Attempt3_M4_4_data[7], Attempt3_M4_4_data[8], Attempt3_M4_4_data[12], Attempt3_M4_4_data[13], Attempt3_M4_4_data[14], Attempt3_M4_4_data[15], Attempt3_M4_4_data[16], Attempt3_M4_4_data[17], Attempt3_M4_4_data[18], Attempt3_M4_4_data[19], Attempt3_M4_4_data[20]]
    dependent_a3_m44_avg=Avg(dependent_a3_m44)
    dependent_a3_m44_stdev=Stdev(dependent_a3_m44, dependent_a3_m44_avg)
    dependent_a3_m44_var=Var(dependent_a3_m44, dependent_a3_m44_avg)
    independent_a3_m44_avg=Avg(independent_a3_m44)
    independent_a3_m44_stdev=Stdev(independent_a3_m44, independent_a3_m44_avg)
    independent_a3_m44_var=Var(independent_a3_m44, independent_a3_m44_avg)
    print("The Z statistics for the Pho4 segment #4 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a3_m44_avg, independent_a3_m44_stdev, dependent_a3_m44_avg, dependent_a3_m44_stdev))
    print("The Welch's t test results for the Pho4 segment #4 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a3_m44_avg, dependent_a3_m44_avg, independent_a3_m44_var, dependent_a3_m44_var))
    
    #Pho2 independent vs Pho2 dependent Attmept 3.1 Method 4.5
    independent_a31_m45=[Attempt3_1_M4_5_data[1], Attempt3_1_M4_5_data[2], Attempt3_1_M4_5_data[9], Attempt3_1_M4_5_data[10], Attempt3_1_M4_5_data[11]]
    dependent_a31_m45=[Attempt3_1_M4_5_data[0], Attempt3_1_M4_5_data[3], Attempt3_1_M4_5_data[4], Attempt3_1_M4_5_data[5], Attempt3_1_M4_5_data[6], Attempt3_1_M4_5_data[7], Attempt3_1_M4_5_data[8], Attempt3_1_M4_5_data[12], Attempt3_1_M4_5_data[13], Attempt3_1_M4_5_data[14], Attempt3_1_M4_5_data[15], Attempt3_1_M4_5_data[16], Attempt3_1_M4_5_data[17], Attempt3_1_M4_5_data[18], Attempt3_1_M4_5_data[19], Attempt3_1_M4_5_data[20]]
    dependent_a31_m45_avg=Avg(dependent_a31_m45)
    dependent_a31_m45_stdev=Stdev(dependent_a31_m45, dependent_a31_m45_avg)
    dependent_a31_m45_var=Var(dependent_a31_m45, dependent_a31_m45_avg)
    independent_a31_m45_avg=Avg(independent_a31_m45)
    independent_a31_m45_stdev=Stdev(independent_a31_m45, independent_a31_m45_avg)
    independent_a31_m45_var=Var(independent_a31_m45, independent_a31_m45_avg)
    print("The Z statistics for the Pho4 segment #5 between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m45_avg, independent_a31_m45_stdev, dependent_a31_m45_avg, dependent_a31_m45_stdev))
    print("The Welch's t test results for the Pho4 segment #5 between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m45_avg, dependent_a31_m45_avg, independent_a31_m45_var, dependent_a31_m45_var))
    
    #Pho2 independent vs Pho2 dependent Attempt 3.1 Method 4.5.1
    independent_a31_m451=[Attempt3_1_M4_5_1_data[1], Attempt3_1_M4_5_1_data[2], Attempt3_1_M4_5_1_data[9], Attempt3_1_M4_5_1_data[10], Attempt3_1_M4_5_1_data[11]]
    dependent_a31_m451=[Attempt3_1_M4_5_1_data[0], Attempt3_1_M4_5_1_data[3], Attempt3_1_M4_5_1_data[4], Attempt3_1_M4_5_1_data[5], Attempt3_1_M4_5_1_data[6], Attempt3_1_M4_5_1_data[7], Attempt3_1_M4_5_1_data[8], Attempt3_1_M4_5_1_data[12], Attempt3_1_M4_5_1_data[13], Attempt3_1_M4_5_1_data[14], Attempt3_1_M4_5_1_data[15], Attempt3_1_M4_5_1_data[16], Attempt3_1_M4_5_1_data[17], Attempt3_1_M4_5_1_data[18], Attempt3_1_M4_5_1_data[19], Attempt3_1_M4_5_1_data[20]]
    dependent_a31_m451_avg=Avg(dependent_a31_m451)
    dependent_a31_m451_stdev=Stdev(dependent_a31_m451, dependent_a31_m451_avg)
    dependent_a31_m451_var=Var(dependent_a31_m451, dependent_a31_m451_avg)
    independent_a31_m451_avg=Avg(independent_a31_m451)
    independent_a31_m451_stdev=Stdev(independent_a31_m451, independent_a31_m451_avg)
    independent_a31_m451_var=Var(independent_a31_m451, independent_a31_m451_avg)
    print("The Z statistics for the Pho4 segment #5 loop between Pho2 independent vs Pho2 dependent groups are: ", Z_statistic(independent_a31_m451_avg, independent_a31_m451_stdev, dependent_a31_m451_avg, dependent_a31_m451_stdev))
    print("The Welch's t test results for the Pho4 segment #5 loop between Pho2 independent vs Pho2 dependent groups are: ", welch_t_test(independent_a31_m451_avg, dependent_a31_m451_avg, independent_a31_m451_var, dependent_a31_m451_var))
    
    #Pho2 independent vs Saccharomyces a1, a2, a3 m1, a3 m2, a3 m3, a3.1 m3.1, a3.1 m3.2
    independent=[Attempt1_data[1], Attempt1_data[2], Attempt1_data[9], Attempt1_data[10], Attempt1_data[11], Attempt2_data[1], Attempt2_data[2], Attempt2_data[9], Attempt2_data[10], Attempt2_data[11], Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11], Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11], Attempt3_M3_data[1], Attempt3_M3_data[2], Attempt3_M3_data[9], Attempt3_M3_data[10], Attempt3_M3_data[11], Attempt3_1_M3_1_data[1], Attempt3_1_M3_1_data[2], Attempt3_1_M3_1_data[9], Attempt3_1_M3_1_data[10], Attempt3_1_M3_1_data[11], Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    saccharomyces=[Attempt1_data[0], Attempt1_data[14], Attempt1_data[15], Attempt1_data[16], Attempt1_data[17], Attempt1_data[18], Attempt2_data[0], Attempt2_data[14], Attempt2_data[15], Attempt2_data[16], Attempt2_data[17], Attempt2_data[18], Attempt3_M1_data[0], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18], Attempt3_M2_data[0], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18], Attempt3_M3_data[0], Attempt3_M3_data[14], Attempt3_M3_data[15], Attempt3_M3_data[16], Attempt3_M3_data[17], Attempt3_M3_data[18], Attempt3_1_M3_1_data[0], Attempt3_1_M3_1_data[14], Attempt3_1_M3_1_data[15], Attempt3_1_M3_1_data[16], Attempt3_1_M3_1_data[17], Attempt3_1_M3_1_data[18], Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18]]
    saccharomyces_avg=Avg(saccharomyces)
    saccharomyces_stdev=Stdev(saccharomyces, saccharomyces_avg)
    saccharomyces_var=Var(saccharomyces, saccharomyces_avg)
    independent_avg=Avg(independent)
    independent_stdev=Stdev(independent, independent_avg) 
    independent_var=Var(independent, independent_avg)
    print("The Z statistics for all full IDR sequence attempts between the Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_avg, independent_stdev, saccharomyces_avg, saccharomyces_stdev))
    print("The Welch's t test results for all full IDR sequence attempts between the Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_avg, saccharomyces_avg, independent_var, saccharomyces_var))
    
    #Pho2 independent vs Saccharomyces A3m1, a3m2, a3.1 m3.2
    independent_precise=[Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11], Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11], Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    saccharomyces_precise=[Attempt3_M1_data[0], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18], Attempt3_M2_data[0], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18], Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18]]
    saccharomyces_avg_p=Avg(saccharomyces_precise)
    saccharomyces_stdev_p=Stdev(saccharomyces_precise, saccharomyces_avg_p)
    saccharomyces_var_p=Var(saccharomyces_precise, saccharomyces_avg_p)
    independent_avg_p=Avg(independent_precise)
    independent_stdev_p=Stdev(independent_precise, independent_avg_p)
    independent_var_p=Var(independent_precise, independent_avg_p)
    print("The Z statistics for a presice full IDR sequence between the Pho2 independent vs Saccharomyces gorups are: ", Z_statistic(independent_avg_p, independent_stdev_p, saccharomyces_avg_p, saccharomyces_stdev_p))
    print("The Welch's t test results for a precise full IDR sequence between the Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_avg_p, saccharomyces_avg_p, independent_var_p, saccharomyces_var_p))
    
    #Pho2 independent vs Saccharomyces control full sequence
    independent_full=[Full_sequence_data[1], Full_sequence_data[2], Full_sequence_data[9], Full_sequence_data[10], Full_sequence_data[11]]
    saccharomyces_full=[Full_sequence_data[0], Full_sequence_data[14], Full_sequence_data[15], Full_sequence_data[16], Full_sequence_data[17], Full_sequence_data[18]]
    saccharomyces_full_avg=Avg(saccharomyces_full)
    saccharomyces_full_stdev=Stdev(saccharomyces_full, saccharomyces_full_avg)
    saccharomyces_full_var=Var(saccharomyces_full, saccharomyces_full_avg)
    independent_full_avg=Avg(independent_full)
    independent_full_stdev=Stdev(independent_full, independent_full_avg)
    independent_full_var=Var(independent_full, independent_full_avg)
    print("The Z statistics for the full sequence control between the Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_full_avg, independent_full_stdev, saccharomyces_full_avg, saccharomyces_full_stdev))
    print("The Welch's t test results for the full sequence control between the Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_full_avg, saccharomyces_full_avg, independent_full_var, saccharomyces_full_var))
    
    #Pho2 independent vs Saccharomyces control SC based IDR region Attempt 4
    independent_a4=[Attempt_4_data[1], Attempt_4_data[2], Attempt_4_data[9], Attempt_4_data[10], Attempt_4_data[11]]
    saccharomyces_a4=[Attempt_4_data[0], Attempt_4_data[14], Attempt_4_data[15], Attempt_4_data[16], Attempt_4_data[17], Attempt_4_data[18]]
    saccharomyces_a4_avg=Avg(saccharomyces_a4)
    saccharomyces_a4_stdev=Stdev(saccharomyces_a4, saccharomyces_a4_avg)
    saccharomyces_a4_var=Var(saccharomyces_a4, saccharomyces_a4_avg)
    independent_a4_avg=Avg(independent_a4)
    independent_a4_stdev=Stdev(independent_a4, independent_a4_avg)
    independent_a4_var=Var(independent_a4, independent_a4_avg)
    print("The Z statistics for the IDR region based on S. cerevisiae control between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a4_avg, independent_a4_stdev, saccharomyces_a4_avg, saccharomyces_a4_stdev))
    print("The Welch's t test results for the IDR region based on S. cerevisiae control between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a4_avg, saccharomyces_a4_avg, independent_a4_var, saccharomyces_a4_var))
    
    #Pho2 independent vs Saccharomyces Attempt 1
    independent_a1=[Attempt1_data[1], Attempt1_data[2], Attempt1_data[9], Attempt1_data[10], Attempt1_data[11]]
    saccharomyces_a1=[Attempt1_data[0], Attempt1_data[14], Attempt1_data[15], Attempt1_data[16], Attempt1_data[17], Attempt1_data[18]]
    saccharomyces_a1_avg=Avg(saccharomyces_a1)
    saccharomyces_a1_stdev=Stdev(saccharomyces_a1, saccharomyces_a1_avg)
    saccharomyces_a1_var=Var(saccharomyces_a1, saccharomyces_a1_avg)
    independent_a1_avg=Avg(independent_a1)
    independent_a1_stdev=Stdev(independent_a1, independent_a1_avg)
    independent_a1_var=Var(independent_a1, independent_a1_avg)
    print("The Z statistics for the IDR sequence attempt 1 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a1_avg, independent_a1_stdev, saccharomyces_a1_avg, saccharomyces_a1_stdev))
    print("The Welch's t test results for the IDR sequence attempt 1 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a1_avg, saccharomyces_a1_avg, independent_a1_var, saccharomyces_a1_var))
    
    #Pho2 independent vs Saccharomyces Attempt 2
    independent_a2=[Attempt2_data[1], Attempt2_data[2], Attempt2_data[9], Attempt2_data[10], Attempt2_data[11]]
    saccharomyces_a2=[Attempt2_data[0], Attempt2_data[14], Attempt2_data[15], Attempt2_data[16], Attempt2_data[17], Attempt2_data[18]]
    saccharomyces_a2_avg=Avg(saccharomyces_a2)
    saccharomyces_a2_stdev=Stdev(saccharomyces_a2, saccharomyces_a2_avg)
    saccharomyces_a2_var=Var(saccharomyces_a2, saccharomyces_a2_avg)
    independent_a2_avg=Avg(independent_a2)
    independent_a2_stdev=Stdev(independent_a2, independent_a2_avg)
    independent_a2_var=Var(independent_a2, independent_a2_avg)
    print("The Z statistics for the IDR sequence attempt 2 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a2_avg, independent_a2_stdev, saccharomyces_a2_avg, saccharomyces_a2_stdev))
    print("The Welch's t test results for the IDR sequence attempt 2 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a2_avg, saccharomyces_a2_avg, independent_a2_var, saccharomyces_a2_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3 Method 1
    independent_a3_m1=[Attempt3_M1_data[1], Attempt3_M1_data[2], Attempt3_M1_data[9], Attempt3_M1_data[10], Attempt3_M1_data[11]]
    saccharomyces_a3_m1=[Attempt3_M1_data[0], Attempt3_M1_data[14], Attempt3_M1_data[15], Attempt3_M1_data[16], Attempt3_M1_data[17], Attempt3_M1_data[18]]
    saccharomyces_a3_m1_avg=Avg(saccharomyces_a3_m1)
    saccharomyces_a3_m1_stdev=Stdev(saccharomyces_a3_m1, saccharomyces_a3_m1_avg)
    saccharomyces_a3_m1_var=Var(saccharomyces_a3_m1, saccharomyces_a3_m1_avg)
    independent_a3_m1_avg=Avg(independent_a3_m1)
    independent_a3_m1_stdev=Stdev(independent_a3_m1, independent_a3_m1_avg)
    independent_a3_m1_var=Var(independent_a3_m1, independent_a3_m1_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 1 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a3_m1_avg, independent_a3_m1_stdev, saccharomyces_a3_m1_avg, saccharomyces_a3_m1_stdev)) 
    print("The Welch's t test results for the IDR sequence attempt 3 method 1 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a3_m1_avg, saccharomyces_a3_m1_avg, independent_a3_m1_var, saccharomyces_a3_m1_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3 Method 2
    independent_a3_m2=[Attempt3_M2_data[1], Attempt3_M2_data[2], Attempt3_M2_data[9], Attempt3_M2_data[10], Attempt3_M2_data[11]]
    saccharomyces_a3_m2=[Attempt3_M2_data[0], Attempt3_M2_data[14], Attempt3_M2_data[15], Attempt3_M2_data[16], Attempt3_M2_data[17], Attempt3_M2_data[18]]
    saccharomyces_a3_m2_avg=Avg(saccharomyces_a3_m2)
    saccharomyces_a3_m2_stdev=Stdev(saccharomyces_a3_m2, saccharomyces_a3_m2_avg)
    saccharomyces_a3_m2_var=Var(saccharomyces_a3_m2, saccharomyces_a3_m2_avg)
    independent_a3_m2_avg=Avg(independent_a3_m2)
    independent_a3_m2_stdev=Stdev(independent_a3_m2, independent_a3_m2_avg)
    independent_a3_m2_var=Var(independent_a3_m2, independent_a3_m2_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 2 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a3_m2_avg, independent_a3_m2_stdev, saccharomyces_a3_m2_avg, saccharomyces_a3_m2_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3 method 2 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a3_m2_avg, saccharomyces_a3_m2_avg, independent_a3_m2_var, saccharomyces_a3_m2_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3 Method 3
    independent_a3_m3=[Attempt3_M3_data[1], Attempt3_M3_data[2], Attempt3_M3_data[9], Attempt3_M3_data[10], Attempt3_M3_data[11]]
    saccharomyces_a3_m3=[Attempt3_M3_data[0], Attempt3_M3_data[14], Attempt3_M3_data[15], Attempt3_M3_data[16], Attempt3_M3_data[17], Attempt3_M3_data[18]]
    saccharomyces_a3_m3_avg=Avg(saccharomyces_a3_m3)
    saccharomyces_a3_m3_stdev=Stdev(saccharomyces_a3_m3, saccharomyces_a3_m3_avg)
    saccharomyces_a3_m3_var=Var(saccharomyces_a3_m3, saccharomyces_a3_m3_avg)
    independent_a3_m3_avg=Avg(independent_a3_m3)
    independent_a3_m3_stdev=Stdev(independent_a3_m3, independent_a3_m3_avg)
    independent_a3_m3_var=Var(independent_a3_m3, independent_a3_m3_avg)
    print("The Z statistics for the IDR sequence attempt 3 method 3 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a3_m3_avg, independent_a3_m3_stdev, saccharomyces_a3_m3_avg, saccharomyces_a3_m3_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3 method 3 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a3_m3_avg, saccharomyces_a3_m3_avg, independent_a3_m3_var, saccharomyces_a3_m3_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 3.1
    independent_a31_m31=[Attempt3_1_M3_1_data[1], Attempt3_1_M3_1_data[2], Attempt3_1_M3_1_data[9], Attempt3_1_M3_1_data[10], Attempt3_1_M3_1_data[11]]
    saccharomyces_a31_m31=[Attempt3_1_M3_1_data[0], Attempt3_1_M3_1_data[14], Attempt3_1_M3_1_data[15], Attempt3_1_M3_1_data[16], Attempt3_1_M3_1_data[17], Attempt3_1_M3_1_data[18]]
    saccharomyces_a31_m31_avg=Avg(saccharomyces_a31_m31)
    saccharomyces_a31_m31_stdev=Stdev(saccharomyces_a31_m31, saccharomyces_a31_m31_avg)
    saccharomyces_a31_m31_var=Var(saccharomyces_a31_m31, saccharomyces_a31_m31_avg)
    independent_a31_m31_avg=Avg(independent_a31_m31)
    independent_a31_m31_stdev=Stdev(independent_a31_m31, independent_a31_m31_avg)
    independent_a31_m31_var=Var(independent_a31_m31, independent_a31_m31_avg)
    print("The Z statistics for the IDR sequence attempt 3.1 method 3.1 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m31_avg, independent_a31_m31_stdev, saccharomyces_a31_m31_avg, saccharomyces_a31_m31_stdev))
    print("The Welch's t test results for the IDR sequence attempt 3.1 method 3.1 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m31_avg, saccharomyces_a31_m31_avg, independent_a31_m31_var, saccharomyces_a31_m31_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 3.2
    independent_a31_m32=[Attempt3_1_M3_2_data[1], Attempt3_1_M3_2_data[2], Attempt3_1_M3_2_data[9], Attempt3_1_M3_2_data[10], Attempt3_1_M3_2_data[11]]
    saccharomyces_a31_m32=[Attempt3_1_M3_2_data[0], Attempt3_1_M3_2_data[14], Attempt3_1_M3_2_data[15], Attempt3_1_M3_2_data[16], Attempt3_1_M3_2_data[17], Attempt3_1_M3_2_data[18]]
    saccharomyces_a31_m32_avg=Avg(saccharomyces_a31_m32)
    saccharomyces_a31_m32_stdev=Stdev(saccharomyces_a31_m32, saccharomyces_a31_m32_avg)
    saccharomyces_a31_m32_var=Var(saccharomyces_a31_m32, saccharomyces_a31_m32_avg)
    independent_a31_m32_avg=Avg(independent_a31_m32)
    independent_a31_m32_stdev=Stdev(independent_a31_m32, independent_a31_m32_avg)
    independent_a31_m32_var=Var(independent_a31_m32, independent_a31_m32_avg)
    print("The Z statistic for the IDR sequence attempt 3.1 method 3.2 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m32_avg, independent_a31_m32_stdev, saccharomyces_a31_m32_avg, saccharomyces_a31_m32_stdev)) 
    print("The Welch's t test results for the IDR sequence attempt 3.1 method 3.2 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m32_avg, saccharomyces_a31_m32_avg, independent_a31_m32_var, saccharomyces_a31_m32_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3 Method 4.1
    independent_a3_m41=[Attempt3_M4_1_data[1], Attempt3_M4_1_data[2], Attempt3_M4_1_data[9], Attempt3_M4_1_data[10], Attempt3_M4_1_data[11]]
    saccharomyces_a3_m41=[Attempt3_M4_1_data[0], Attempt3_M4_1_data[14], Attempt3_M4_1_data[15], Attempt3_M4_1_data[16], Attempt3_M4_1_data[17], Attempt3_M4_1_data[18]]
    saccharomyces_a3_m41_avg=Avg(saccharomyces_a3_m41)
    saccharomyces_a3_m41_stdev=Stdev(saccharomyces_a3_m41, saccharomyces_a3_m41_avg)
    saccharomyces_a3_m41_var=Var(saccharomyces_a3_m41, saccharomyces_a3_m41_avg)
    independent_a3_m41_avg=Avg(independent_a3_m41)
    independent_a3_m41_stdev=Stdev(independent_a3_m41, independent_a3_m41_avg)
    independent_a3_m41_var=Var(independent_a3_m41, independent_a3_m41_avg)
    print("The Z statistics for the Pho4 segment #1 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a3_m41_avg, independent_a3_m41_stdev, saccharomyces_a3_m41_avg, saccharomyces_a3_m41_stdev))
    print("The Welch's t test results for the Pho4 segment #1 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a3_m41_avg, saccharomyces_a3_m41_avg, independent_a3_m41_var, saccharomyces_a3_m41_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 4.2
    independent_a31_m42=[Attempt3_1_M4_2_data[1], Attempt3_1_M4_2_data[2], Attempt3_1_M4_2_data[9], Attempt3_1_M4_2_data[10], Attempt3_1_M4_2_data[11]]
    saccharomyces_a31_m42=[Attempt3_1_M4_2_data[0], Attempt3_1_M4_2_data[14], Attempt3_1_M4_2_data[15], Attempt3_1_M4_2_data[16], Attempt3_1_M4_2_data[17], Attempt3_1_M4_2_data[18]]
    saccharomyces_a31_m42_avg=Avg(saccharomyces_a31_m42)
    saccharomyces_a31_m42_stdev=Stdev(saccharomyces_a31_m42, saccharomyces_a31_m42_avg)
    saccharomyces_a31_m42_var=Var(saccharomyces_a31_m42, saccharomyces_a31_m42_avg)
    independent_a31_m42_avg=Avg(independent_a31_m42)
    independent_a31_m42_stdev=Stdev(independent_a31_m42, independent_a31_m42_avg)
    independent_a31_m42_var=Var(independent_a31_m42, independent_a31_m42_avg)
    print("The Z statistics for the Pho4 segment #2 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m42_avg, independent_a31_m42_stdev, saccharomyces_a31_m42_avg, saccharomyces_a31_m42_stdev))
    print("The Welch's t test results for the Pho4 segment #2 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m42_avg, saccharomyces_a31_m42_avg, independent_a31_m42_var, saccharomyces_a31_m42_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 4.3
    independent_a31_m43=[Attempt3_1_M4_3_data[1], Attempt3_1_M4_3_data[2], Attempt3_1_M4_3_data[9], Attempt3_1_M4_3_data[10], Attempt3_1_M4_3_data[11]]
    saccharomyces_a31_m43=[Attempt3_1_M4_3_data[0], Attempt3_1_M4_3_data[14], Attempt3_1_M4_3_data[15], Attempt3_1_M4_3_data[16], Attempt3_1_M4_3_data[17], Attempt3_1_M4_3_data[18]]
    saccharomyces_a31_m43_avg=Avg(saccharomyces_a31_m43)
    saccharomyces_a31_m43_stdev=Stdev(saccharomyces_a31_m43, saccharomyces_a31_m43_avg)
    saccharomyces_a31_m43_var=Var(saccharomyces_a31_m43, saccharomyces_a31_m43_avg)
    independent_a31_m43_avg=Avg(independent_a31_m43)
    independent_a31_m43_stdev=Stdev(independent_a31_m43, independent_a31_m43_avg)
    independent_a31_m43_var=Var(independent_a31_m43, independent_a31_m43_avg)
    print("The Z statistics for the Pho4 segment #3 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m43_avg, independent_a31_m43_stdev, saccharomyces_a31_m43_avg, saccharomyces_a31_m43_stdev))
    print("The Welch's t test results for the Pho4 segment #3 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m43_avg, saccharomyces_a31_m43_avg, independent_a31_m43_var, saccharomyces_a31_m43_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3 Method 4.4
    independent_a3_m44=[Attempt3_M4_4_data[1], Attempt3_M4_4_data[2], Attempt3_M4_4_data[9], Attempt3_M4_4_data[10], Attempt3_M4_4_data[11]]
    saccharomyces_a3_m44=[Attempt3_M4_4_data[0], Attempt3_M4_4_data[14], Attempt3_M4_4_data[15], Attempt3_M4_4_data[16], Attempt3_M4_4_data[17], Attempt3_M4_4_data[18]]
    saccharomyces_a3_m44_avg=Avg(saccharomyces_a3_m44)
    saccharomyces_a3_m44_stdev=Stdev(saccharomyces_a3_m44, saccharomyces_a3_m44_avg)
    saccharomyces_a3_m44_var=Var(saccharomyces_a3_m44, saccharomyces_a3_m44_avg)
    independent_a3_m44_avg=Avg(independent_a3_m44)
    independent_a3_m44_stdev=Stdev(independent_a3_m44, independent_a3_m44_avg)
    independent_a3_m44_var=Var(independent_a3_m44, independent_a3_m44_avg)
    print(saccharomyces_a3_m44_avg)
    print("S avg", len(saccharomyces_a3_m44_avg))
    print(saccharomyces_a3_m44_stdev)
    print("S stdev", len(saccharomyces_a3_m44_stdev))
    print(saccharomyces_a3_m44_var)
    print("S var", len(saccharomyces_a3_m44_var))
    print(" G avg", len(independent_a3_m44_avg))
    print("G var", len(independent_a3_m44_var))
    print("The Z statistics for the Pho4 segment #4 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a3_m44_avg, independent_a3_m44_stdev, saccharomyces_a3_m44_avg, saccharomyces_a3_m44_stdev))
    print("The Welch's t test results for the Pho4 segment #4 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a3_m44_avg, saccharomyces_a3_m44_avg, independent_a3_m44_var, saccharomyces_a3_m44_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 4.5
    independent_a31_m45=[Attempt3_1_M4_5_data[1], Attempt3_1_M4_5_data[2], Attempt3_1_M4_5_data[9], Attempt3_1_M4_5_data[10], Attempt3_1_M4_5_data[11]]
    saccharomyces_a31_m45=[Attempt3_1_M4_5_data[0], Attempt3_1_M4_5_data[14], Attempt3_1_M4_5_data[15], Attempt3_1_M4_5_data[16], Attempt3_1_M4_5_data[17], Attempt3_1_M4_5_data[18]]
    saccharomyces_a31_m45_avg=Avg(saccharomyces_a31_m45)
    saccharomyces_a31_m45_stdev=Stdev(saccharomyces_a31_m45, saccharomyces_a31_m45_avg)
    saccharomyces_a31_m45_var=Var(saccharomyces_a31_m45, saccharomyces_a31_m45_avg)
    independent_a31_m45_avg=Avg(independent_a31_m45)
    independent_a31_m45_stdev=Stdev(independent_a31_m45, independent_a31_m45_avg)
    independent_a31_m45_var=Var(independent_a31_m45, independent_a31_m45_avg)
    print("The Z statistics for the Pho4 segment #5 between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m45_avg, independent_a31_m45_stdev, saccharomyces_a31_m45_avg, saccharomyces_a31_m45_stdev))
    print("The Welch's t test results for the Pho4 segment #5 between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m45_avg, saccharomyces_a31_m45_avg, independent_a31_m45_var, saccharomyces_a31_m45_var))
    
    #Pho2 independent vs Saccharomyces Attempt 3.1 Method 4.5.1
    independent_a31_m451=[Attempt3_1_M4_5_1_data[1], Attempt3_1_M4_5_1_data[2], Attempt3_1_M4_5_1_data[9], Attempt3_1_M4_5_1_data[10], Attempt3_1_M4_5_1_data[11]]
    saccharomyces_a31_m451=[Attempt3_1_M4_5_1_data[0], Attempt3_1_M4_5_1_data[14], Attempt3_1_M4_5_1_data[15], Attempt3_1_M4_5_1_data[16], Attempt3_1_M4_5_1_data[17], Attempt3_1_M4_5_1_data[18]]
    saccharomyces_a31_m451_avg=Avg(saccharomyces_a31_m451)
    saccharomyces_a31_m451_stdev=Stdev(saccharomyces_a31_m451, saccharomyces_a31_m451_avg)
    saccharomyces_a31_m451_var=Var(saccharomyces_a31_m451, saccharomyces_a31_m451_avg)
    independent_a31_m451_avg=Avg(independent_a31_m451)
    independent_a31_m451_stdev=Stdev(independent_a31_m451, independent_a31_m451_avg)
    independent_a31_m451_var=Var(independent_a31_m451, independent_a31_m451_avg)
    print("The Z statistics for the Pho4 segment #5 loop between Pho2 independent vs Saccharomyces groups are: ", Z_statistic(independent_a31_m451_avg, independent_a31_m451_stdev, saccharomyces_a31_m451_avg, saccharomyces_a31_m451_stdev)) 
    print("The Welch's t test results for the Pho4 segment #5 loop between Pho2 independent vs Saccharomyces groups are: ", welch_t_test(independent_a31_m451_avg, saccharomyces_a31_m451_avg, independent_a31_m451_var, saccharomyces_a31_m451_var))
    
    with open("Z_test_results1.csv", "a") as file:
        writer=csv.writer(file)
        writer.writerow(Z_statistic(C_glabrata_avg, C_glabrata_stdev, S_cerevisiae_avg, S_cerevisiae_stdev))
        writer.writerow(Z_statistic(C_glabrata_avg_p, C_glabrata_stdev_p, S_cerevisiae_avg_p, S_cerevisiae_stdev_p))
        writer.writerow(Z_statistic(independent_avg, independent_stdev, dependent_avg, dependent_stdev))
        writer.writerow(Z_statistic(independent_avg, independent_stdev, saccharomyces_avg, saccharomyces_stdev))
        writer.writerow(Z_statistic(independent_avg_p, independent_stdev_p, dependent_avg_p, dependent_stdev_p))
        writer.writerow(Z_statistic(independent_avg_p, independent_stdev_p, saccharomyces_avg_p, saccharomyces_stdev_p))
        writer.writerow(Z_statistic(independent_full_avg, independent_full_stdev, dependent_full_avg, dependent_full_stdev))
        writer.writerow(Z_statistic(independent_full_avg, independent_full_stdev, saccharomyces_full_avg, saccharomyces_full_stdev))
        writer.writerow(Z_statistic(independent_a4_avg, independent_a4_stdev, dependent_a4_avg, dependent_a4_stdev))
        writer.writerow(Z_statistic(independent_a4_avg, independent_a4_stdev, saccharomyces_a4_avg, saccharomyces_a4_stdev))
        writer.writerow(Z_statistic(independent_a1_avg, independent_a1_stdev, dependent_a1_avg, dependent_a1_stdev))
        writer.writerow(Z_statistic(independent_a1_avg, independent_a1_stdev, saccharomyces_a1_avg, saccharomyces_a1_stdev))
        writer.writerow(Z_statistic(independent_a2_avg, independent_a2_stdev, dependent_a2_avg, dependent_a2_stdev))
        writer.writerow(Z_statistic(independent_a2_avg, independent_a2_stdev, saccharomyces_a2_avg, saccharomyces_a2_stdev))
        writer.writerow(Z_statistic(independent_a3_m1_avg, independent_a3_m1_stdev, dependent_a3_m1_avg, dependent_a3_m1_stdev))
        writer.writerow(Z_statistic(independent_a3_m1_avg, independent_a3_m1_stdev, saccharomyces_a3_m1_avg, saccharomyces_a3_m1_stdev))
        writer.writerow(Z_statistic(independent_a3_m2_avg, independent_a3_m2_stdev, dependent_a3_m2_avg, dependent_a3_m2_stdev))
        writer.writerow(Z_statistic(independent_a3_m2_avg, independent_a3_m2_stdev, saccharomyces_a3_m2_avg, saccharomyces_a3_m2_stdev))
        writer.writerow(Z_statistic(independent_a3_m3_avg, independent_a3_m3_stdev, dependent_a3_m3_avg, dependent_a3_m3_stdev))
        writer.writerow(Z_statistic(independent_a3_m3_avg, independent_a3_m3_stdev, saccharomyces_a3_m3_avg, saccharomyces_a3_m3_stdev))
        writer.writerow(Z_statistic(independent_a31_m31_avg, independent_a31_m31_stdev, dependent_a31_m31_avg, dependent_a31_m31_stdev))
        writer.writerow(Z_statistic(independent_a31_m31_avg, independent_a31_m31_stdev, saccharomyces_a31_m31_avg, saccharomyces_a31_m31_stdev))
        writer.writerow(Z_statistic(independent_a31_m32_avg, independent_a31_m32_stdev, dependent_a31_m32_avg, dependent_a31_m32_stdev))
        writer.writerow(Z_statistic(independent_a31_m32_avg, independent_a31_m32_stdev, saccharomyces_a31_m32_avg, saccharomyces_a31_m32_stdev))
        writer.writerow(Z_statistic(independent_a3_m41_avg, independent_a3_m41_stdev, dependent_a3_m41_avg, dependent_a3_m41_stdev))
        writer.writerow(Z_statistic(independent_a3_m41_avg, independent_a3_m41_stdev, saccharomyces_a3_m41_avg, saccharomyces_a3_m41_stdev))
        writer.writerow(Z_statistic(independent_a31_m42_avg, independent_a31_m42_stdev, dependent_a31_m42_avg, dependent_a31_m42_stdev))
        writer.writerow(Z_statistic(independent_a31_m42_avg, independent_a31_m42_stdev, saccharomyces_a31_m42_avg, saccharomyces_a31_m42_stdev))
        writer.writerow(Z_statistic(independent_a31_m43_avg, independent_a31_m43_stdev, dependent_a31_m43_avg, dependent_a31_m43_stdev))
        writer.writerow(Z_statistic(independent_a31_m43_avg, independent_a31_m43_stdev, saccharomyces_a31_m43_avg, saccharomyces_a31_m43_stdev))
        writer.writerow(Z_statistic(independent_a3_m44_avg, independent_a3_m44_stdev, dependent_a3_m44_avg, dependent_a3_m44_stdev))
        writer.writerow(Z_statistic(independent_a3_m44_avg, independent_a3_m44_stdev, saccharomyces_a3_m44_avg, saccharomyces_a3_m44_stdev))
        writer.writerow(Z_statistic(independent_a31_m45_avg, independent_a31_m45_stdev, dependent_a31_m45_avg, dependent_a31_m45_stdev))
        writer.writerow(Z_statistic(independent_a31_m45_avg, independent_a31_m45_stdev, saccharomyces_a31_m45_avg, saccharomyces_a31_m45_stdev))
        writer.writerow(Z_statistic(independent_a31_m451_avg, independent_a31_m451_stdev, dependent_a31_m451_avg, dependent_a31_m451_stdev))
        writer.writerow(Z_statistic(independent_a31_m451_avg, independent_a31_m451_stdev, saccharomyces_a31_m451_avg, saccharomyces_a31_m451_stdev))
        
        writer.writerow(welch_t_test(C_glabrata_avg, S_cerevisiae_avg, C_glabrata_var, S_cerevisiae_var))
        writer.writerow(welch_t_test(C_glabrata_avg_p, S_cerevisiae_avg_p, C_glabrata_var_p, S_cerevisiae_var_p))
        writer.writerow(welch_t_test(independent_avg, dependent_avg, independent_var, dependent_var))
        writer.writerow(welch_t_test(independent_avg, saccharomyces_avg, independent_var, saccharomyces_var))
        writer.writerow(welch_t_test(independent_avg_p, dependent_avg_p, independent_var_p, dependent_var_p))
        writer.writerow(welch_t_test(independent_avg_p, saccharomyces_avg_p, independent_var_p, saccharomyces_var_p))
        writer.writerow(welch_t_test(independent_full_avg, dependent_full_avg, independent_full_var, dependent_full_var))
        writer.writerow(welch_t_test(independent_full_avg, saccharomyces_full_avg, independent_full_var, saccharomyces_full_var))
        writer.writerow(welch_t_test(independent_a4_avg, dependent_a4_avg, independent_a4_var, dependent_a4_var))
        writer.writerow(welch_t_test(independent_a4_avg, saccharomyces_a4_avg, independent_a4_var, saccharomyces_a4_var))
        writer.writerow(welch_t_test(independent_a1_avg, dependent_a1_avg, independent_a1_var, dependent_a1_var))
        writer.writerow(welch_t_test(independent_a1_avg, saccharomyces_a1_avg, independent_a1_var, saccharomyces_a1_var))
        writer.writerow(welch_t_test(independent_a2_avg, dependent_a2_avg, independent_a2_var, dependent_a2_var))
        writer.writerow(welch_t_test(independent_a2_avg, saccharomyces_a2_avg, independent_a2_var, saccharomyces_a2_var))
        writer.writerow(welch_t_test(independent_a3_m1_avg, dependent_a3_m1_avg, independent_a3_m1_var, dependent_a3_m1_var))
        writer.writerow(welch_t_test(independent_a3_m1_avg, saccharomyces_a3_m1_avg, independent_a3_m1_var, saccharomyces_a3_m1_var))
        writer.writerow(welch_t_test(independent_a3_m2_avg, dependent_a3_m2_avg, independent_a3_m2_var, dependent_a3_m2_var))
        writer.writerow(welch_t_test(independent_a3_m2_avg, saccharomyces_a3_m2_avg, independent_a3_m2_var, saccharomyces_a3_m2_var))
        writer.writerow(welch_t_test(independent_a3_m3_avg, dependent_a3_m3_avg, independent_a3_m3_var, dependent_a3_m3_var))
        writer.writerow(welch_t_test(independent_a3_m3_avg, saccharomyces_a3_m3_avg, independent_a3_m3_var, saccharomyces_a3_m3_var))
        writer.writerow(welch_t_test(independent_a31_m31_avg, dependent_a31_m31_avg, independent_a31_m31_var, dependent_a31_m31_var))
        writer.writerow(welch_t_test(independent_a31_m31_avg, saccharomyces_a31_m31_avg, independent_a31_m31_var, saccharomyces_a31_m31_var))
        writer.writerow(welch_t_test(independent_a31_m32_avg, dependent_a31_m32_avg, independent_a31_m32_var, dependent_a31_m32_var))
        writer.writerow(welch_t_test(independent_a31_m32_avg, saccharomyces_a31_m32_avg, independent_a31_m32_var, saccharomyces_a31_m32_var))
        writer.writerow(welch_t_test(independent_a3_m41_avg, dependent_a3_m41_avg, independent_a3_m41_var, dependent_a3_m41_var))
        writer.writerow(welch_t_test(independent_a3_m41_avg, saccharomyces_a3_m41_avg, independent_a3_m41_var, saccharomyces_a3_m41_var))
        writer.writerow(welch_t_test(independent_a31_m42_avg, dependent_a31_m42_avg, independent_a31_m42_var, dependent_a31_m42_var))
        writer.writerow(welch_t_test(independent_a31_m42_avg, saccharomyces_a31_m42_avg, independent_a31_m42_var, saccharomyces_a31_m42_var))
        writer.writerow(welch_t_test(independent_a31_m43_avg, dependent_a31_m43_avg, independent_a31_m43_var, dependent_a31_m43_var))
        writer.writerow(welch_t_test(independent_a31_m43_avg, saccharomyces_a31_m43_avg, independent_a31_m43_var, saccharomyces_a31_m43_var))
        writer.writerow(welch_t_test(independent_a3_m44_avg, dependent_a3_m44_avg, independent_a3_m44_var, dependent_a3_m44_var))
        writer.writerow(welch_t_test(independent_a3_m44_avg, saccharomyces_a3_m44_avg, independent_a3_m44_var, saccharomyces_a3_m44_var))
        writer.writerow(welch_t_test(independent_a31_m45_avg, dependent_a31_m45_avg, independent_a31_m45_var, dependent_a31_m45_var))
        writer.writerow(welch_t_test(independent_a31_m45_avg, saccharomyces_a31_m45_avg, independent_a31_m45_var, saccharomyces_a31_m45_var))
        writer.writerow(welch_t_test(independent_a31_m451_avg, dependent_a31_m451_avg, independent_a31_m451_var, dependent_a31_m451_var))
        writer.writerow(welch_t_test(independent_a31_m451_avg, saccharomyces_a31_m451_avg, independent_a31_m451_var, saccharomyces_a31_m451_var))
        
        
    

    