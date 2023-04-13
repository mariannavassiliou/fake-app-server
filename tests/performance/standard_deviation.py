import csv
import math

with open('test_results.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    duration_sum = 0
    duration_list = []
    for row in csv_reader:
        if line_count>0:
            if row["metric_name"] == "http_req_duration":
                value = float(row["metric_value"])
                duration_list.append(value)
                duration_sum += value
            line_count += 1
        line_count += 1
    mean = duration_sum/len(duration_list)
    print(f"Mean is equal to {mean}")
    for duration in duration_list:
        diff_to_mean = (duration - mean) ** 2
    std_variation = math.sqrt(diff_to_mean/len(duration_list))
    print(f"Standard deviation is equal to {std_variation}")