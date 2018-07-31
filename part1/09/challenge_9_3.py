import csv

output_list = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
]
print(output_list)

with open("movies.txt", "w") as fail_obj:
    csv_obj = csv.writer(fail_obj, delimiter=",")
    for output_row in output_list:
        csv_obj.writerow(output_row)

print("保存しました")
