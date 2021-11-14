import pandas as pd
import os

# paths
base_dir = "/home/phalc/records"
interested_file = "output_1_xe_dung_yen.csv"
interested_file_path = os.path.join(base_dir, interested_file)
plot_folder_path = os.path.join(base_dir, interested_file.replace(".csv", ""))

# create folder
try:
    os.mkdir(plot_folder_path)
except OSError as error: 
    print(error)      

# read file
df = pd.read_csv(interested_file_path)

# get some basic features of data
unique_values_bus = df["Bus"].unique()
df_bus = df[df["Bus"]==0]
unique_values_msg_id = df_bus["MessageID"].unique()

# loop through all messages by ids
df_list_of_msgs_by_id = []
for msg_id in unique_values_msg_id:
    df_of_msgs_of_this_id = df_bus[df_bus["MessageID"]==msg_id].reset_index(drop=True)
    df_list_of_msgs_by_id.append(df_of_msgs_of_this_id)

# for each id, plot the messages as time series
import matplotlib.pyplot as plt
for df_of_msgs_of_this_id in df_list_of_msgs_by_id:
    df_of_msgs_of_this_id_int = df_of_msgs_of_this_id["Message"].apply(int, base=16)
    this_msg_id = df_of_msgs_of_this_id["MessageID"][0]
    fig=plt.figure()
    fig.suptitle(this_msg_id, fontsize=20)
    df_of_msgs_of_this_id_int.plot(kind="line", x="index", y="value")
    plt.xlabel("time", fontsize=18)
    plt.ylabel("value", fontsize=16)
    fig.savefig(f"{plot_folder_path}/{this_msg_id}.jpg")

    