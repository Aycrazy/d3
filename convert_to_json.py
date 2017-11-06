import csv
import json

csvfile = open('aptc.csv', 'r')
jsonfile = open('small_aptc.json', 'w')

fieldnames = ("county_fips_code","state_name", "county","no_aptc","yes_aptc","total_plan_selections")
reader = csv.DictReader( csvfile, fieldnames)
good_rows = []
ct = 0
for idx,row in enumerate(reader):
	if idx ==0:
		continue
	if ct < 30:
		if row['yes_aptc'] not in ['NaN','.'] and row['total_plan_selections'] not in ['NaN','.']\
		and row['county'] not in ['NaN','.'] :
			row["county"] = row["county"].replace("Borough","")\
			.replace("Area","").replace("Census","")
			row["no_aptc"] = int(row["no_aptc"])
			row["yes_aptc"] = int(row["yes_aptc"])
			row["total_plan_selections"] = int(row["total_plan_selections"])
			good_rows.append(row)

			ct+=1

out = json.dumps(good_rows)
jsonfile.write(out)
