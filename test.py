import glob
import yaml
import csv
count =0;

row=["batsman","bowler","non_striker","batsman_runs","extras","total","fielders","kind","player_out"]
with open('ipl.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
for filename in glob.glob('*.yaml'):
    count=count +1
    print(count)
    print(filename)
    stream  = open(filename,'r')
    data = yaml.load(stream)

    #print(data)
    #type(data)

    #data.keys()

    #keys are meta info innings

    # we are intrested in innings

    #print(data['innings'])
    # data['innings'] is a list and length 2 --- that is first innings and second

    # to look in firat innings
    #data['innings'][0]
    #data['innings'][0]---- is dict having keys 1st innings

    #print(data['innings']['1st innings'])

    #data['innings'][0]['1st innings']

    #to get deliveries data['innings'][0]['1st innings']['deliveries']

    #print(data['innings'][0]['1st innings']['deliveries'])


    # to get each delivery(ata['innings'][0]['1st innings']['deliveries'][0] to length)

    #print(data['innings'][0]['1st innings']['deliveries'][0])

    inn1 = data['innings'][0]['1st innings']['deliveries']
    # to print all deliveries

    for i in  inn1:
    	#print(i.values())
    	a=list(i.values())
    	for j in a:
    		b=list(j.keys())
    		batsman=j['batsman']
    		bowler=j['bowler']
    		non_striker=j['non_striker']
    		batsman_runs=j['runs']['batsman']
    		extras = j['runs']['extras']
    		total=j['runs']['total']
    		#print(j)
    		if 'wicket' in j:
    			fielders=j['wicket'].keys()
    			fielders_list = list(j['wicket'].keys())
    			#fielders=fielders['fielders']
    			if 'fielders' in fielders_list:
    				fielders = j['wicket']['fielders'][0]
    			else:
    				fielders = "null"
    			#print(fielders)
    			kind = j['wicket']['kind']
    			player_out =j['wicket']['player_out']

    		else:

    			fielders="null"
    			kind = "null"
    			player_out ="null"

    		list1=[batsman,bowler,non_striker,batsman_runs,extras,total,fielders,kind,player_out]
    		with open('ipl.csv', 'a') as csvFile:
    		    writer = csv.writer(csvFile)
    		    writer.writerow(list1)

    # for second innings
    if(len(data['innings'])==2):
        inn2 = data['innings'][1]['2nd innings']['deliveries']
        #print("###################################################")
        for i in  inn2:
        	#print(i.values())
        	a=list(i.values())
        	for j in a:
        		b=list(j.keys())
        		batsman=j['batsman']
        		bowler=j['bowler']
        		non_striker=j['non_striker']
        		batsman_runs=j['runs']['batsman']
        		extras = j['runs']['extras']
        		total=j['runs']['total']
        		#print(j)
        		if 'wicket' in j:
        			fielders=j['wicket'].keys()
        			fielders_list = list(j['wicket'].keys())
        			#fielders=fielders['fielders']
        			if 'fielders' in fielders_list:
        				fielders = j['wicket']['fielders'][0]
        			else:
        				fielders = "null"
        			#print(fielders)
        			kind = j['wicket']['kind']
        			player_out =j['wicket']['player_out']

        		else:
        			fielders="null"
        			kind = "null"
        			player_out ="null"

        		list1=[batsman,bowler,non_striker,batsman_runs,extras,total,fielders,kind,player_out]
        		with open('ipl.csv', 'a') as csvFile:
        				writer = csv.writer(csvFile)
        				writer.writerow(list1)
