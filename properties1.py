import pandas as pd 
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

#height_mode = statistics.mode(height_list)
#weight_mode = statistics.mode(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

h_f_std_start,h_f_std_end = height_mean - height_std_deviation,height_mean + height_std_deviation
h_s_std_start,h_s_std_end = height_mean - (2*height_std_deviation),height_mean + (2*height_std_deviation)
h_t_std_start,h_t_std_end = height_mean - (3*height_std_deviation),height_mean + (3*height_std_deviation)

w_f_std_start,w_f_std_end = weight_mean - weight_std_deviation,weight_mean + weight_std_deviation
w_s_std_start,w_s_std_end = weight_mean - (2*weight_std_deviation),weight_mean + (2*weight_std_deviation)
w_t_std_start,w_t_std_end = weight_mean - (3*weight_std_deviation),weight_mean + (3*weight_std_deviation)

h_listData_f_std = [result for result in height_list if result > h_f_std_start and result < h_f_std_end]
h_listData_s_std = [result for result in height_list if result > h_s_std_start and result < h_s_std_end]
h_listData_t_std = [result for result in height_list if result > h_t_std_start and result < h_t_std_end]
w_listData_f_std = [result for result in weight_list if result > w_f_std_start and result < w_f_std_end]
w_listData_s_std = [result for result in weight_list if result > w_s_std_start and result < w_s_std_end]
w_listData_t_std = [result for result in weight_list if result > w_t_std_start and result < w_t_std_end]

print("{}% of data for height lies within first standard deviation".format(len(h_listData_f_std)*100.0/len(height_list)))
print("{}% of data for height lies within second standard deviation".format(len(h_listData_s_std)*100.0/len(height_list)))
print("{}% of data for height lies within third standard deviation".format(len(h_listData_t_std)*100.0/len(height_list)))
print("{}% of data for weight lies within first standard deviation".format(len(w_listData_f_std)*100.0/len(weight_list)))
print("{}% of data for weight lies within second standard deviation".format(len(w_listData_s_std)*100.0/len(weight_list)))
print("{}% of data for weight lies within third standard deviation".format(len(w_listData_t_std)*100.0/len(weight_list)))