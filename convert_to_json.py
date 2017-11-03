import csv
import json

csvfile = open('aptc.csv', 'r')
jsonfile = open('small_aptc.json', 'w')

fieldnames = ("county_fips_code","state_name","no_aptc","yes_aptc","total_plan_selections")
reader = csv.DictReader( csvfile, fieldnames)
good_rows = []
ct = 0
for idx,row in enumerate(reader):
	if idx ==0:
		continue
	if ct < 30:
		if row['yes_aptc'] not in ['NaN','.'] and row['total_plan_selections'] not in ['NaN','.']:
			print(row)
			good_rows.append(row)

	ct+=1

out = json.dumps(good_rows)
jsonfile.write(out)
