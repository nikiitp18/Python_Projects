# All decimal 3 places
import math

# Funtion to check validity of input
def not_valid(check_list):
    for j in check_list:
        if not (isinstance(j,int) or isinstance(j,float)):
            return True
    return False           

# Function to compute mean
def mean(first_list):
    # mean Logic 
    if not_valid(first_list):
        return 0
    s=summation(first_list)
    n=len(first_list)
    mean_value = round(s/n, 6)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    if not_valid(first_list):
        return 0
    n=len(first_list)
    sort_l=sorting(first_list)
    if n%2:
        median_value = sort_l[n//2] 
    else :
        median_value = round((sort_l[n//2]+sort_l[n//2 -1])/2 , 6)  

    return median_value



# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if not_valid(first_list):
        return 0
    var = variance(first_list)
    standard_deviation_value = round(math.sqrt(var) , 6)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if not_valid(first_list):
        return 0
    m=mean(first_list)
    n=len(first_list)
    num=0
    for j in first_list:
        num+= (m-j)*(m-j)
    variance_value =  round(num/n , 6)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    n=len(first_list)
    m=len(second_list)
    if n!=m:
        return 0
    if not_valid(first_list) or not_valid(second_list):
        return 0
    ms = mse(first_list , second_list)
    rmse_value = round(math.sqrt(ms) , 6)        
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    n=len(first_list)
    m=len(second_list)
    if n!=m:
        return 0
    if not_valid(first_list) or not_valid(second_list):
        return 0   
    s=0
    for i in range(n):
        s+= ((first_list[i] -second_list[i])*(first_list[i]-second_list[i]))
    mse_value = round(s/n ,6)    
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    n=len(first_list)
    m=len(second_list)
    if n!=m:
        return 0
    if not_valid(first_list) or not_valid(second_list):
        return 0   
    s=0
    for i in range(n):
        s+= abs(first_list[i] -second_list[i])
    mae_value  = round(s/n , 6)    
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    n=len(first_list)
    m=len(second_list)
    if n!=m:
        return 0
    if not_valid(first_list) or not_valid(second_list):
        return 0
    nu = mse(first_list , second_list)
    de = variance(first_list)
    nse_value = round( 1 - nu/de , 6 )
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # pcc Logic
    n=len(first_list)
    m=len(second_list)
    if n!=m:
        return 0
    if not_valid(first_list) or not_valid(second_list):
        return 0
    s=0  
    xm = mean(first_list)
    ym = mean(second_list)  
    xsd = standard_deviation(first_list)
    ysd = standard_deviation(second_list) 
    for i in range(n):
        s +=(first_list[i]-xm)*(second_list[i]-ym)
    pcc_value = round( s/(n*(xsd*ysd))  , 6)      
    return pcc_value 


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    skewness_value =0
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    sorted_list=first_list
    n=len(first_list)
    for i in range(n):
        for j in range(i,n):
            if sorted_list[i] > sorted_list[j]:
                x=sorted_list[j]
                sorted_list[j]=sorted_list[i]
                sorted_list[i]=x
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    kurtosis_value =0
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    if not_valid(first_list):
        return 0
    summation_value=0
    for val in first_list:
        summation_value+=val
    return summation_value
