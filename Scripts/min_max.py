import csv
#list_l=[[2, 3, 4, 5], [3, 5, 7, 8], [7, 6, 8, 4]]
#with open('Test_min_max.csv', 'w') as file:
    #writer=csv.writer(file)
#Note input file should only have 100 protein inputs. Unfortunately terminal cannot handle more.
input_file=input("Enter name of input file: ")
print(input_file)

with open(input_file, 'r') as f:
    #lines=f.read()
    #print(lines)
    line_L=[]
    for line in f:
        line_L.append(line.strip())
        
print(line_L)
features=line_L[0].strip('\t')
split_line_L=[]
for i in range(1,len(line_L)):
    split_line_L.append(line_L[i].split('\t'))
print(split_line_L)


        
'''
split_line_L=[['apple', '2', '3', '4'], ['grape', '5', '6', '7'], ['orange', '8', '9', '10'],['cherry', '11', '12', '13']]
'''
def int_calculator(list_l):
    int_calc=[]
    minimum=[]
    maximum=[]
    i=0
    for i in range(len(list_l[i])+1):
        if i<len(list_l):
            j=0
            for j in range(len(list_l[i])+1):
                #print(range(len(list_l[i])))
                if j<=83:
                    j+=1
                elif 83<j<len(list_l[i]):
                    if list_l[i][j]=='-':
                        j+=1
                    elif list_l[i][j]=='NA':
                        j+=1
                    else:
                        int_calc.append([float(list_l[i][j]), features[j]])                    
                    #int_calc.append(float(list_l[i][j]))
                elif j==len(list_l[i]):
                    minimum.append(['min', list_l[i][0], min(int_calc)]) 
                    maximum.append(['max', list_l[i][0], max(int_calc)])
                    #print( 'min', min(int_calc))
                    int_calc.clear()
                    
        elif i==len(list_l): 
            with open(output_file, 'a') as file:
                writer=csv.writer(file) 
                header=['data type', 'protein code', 'molecular feature z score']
                writer.writerow(header)
                writer.writerows(minimum)
                writer.writerows(maximum)
            return (minimum, maximum)
 
output_file=input("Enter name of output file: ")
print(output_file)
print(int_calculator(split_line_L))
        
