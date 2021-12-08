import json
import csv

path = '/Users/brianspencer/Documents/GitHub/dataconnect-solutions/sampledatasets/'
files = ['BasicDataSet_v0.CalendarView_v0',
'BasicDataSet_v0.Event_v1',
'BasicDataSet_v0.Inbox_v1',
'BasicDataSet_v0.Message_v1',
'BasicDataSet_v0.User_v1',
'BasicDataSet_v0.Contact_v1',
'BasicDataSet_v0.MailFolder_v0',
'DocumentSharingDataset_v0_Preview',
'BasicDataSet_v0.DirectReport_v0',
'BasicDataSet_v0.MailboxSettings_v0',
'BasicDataSet_v0.SentItem_v1',
'BasicDataSet_v0.Manager_v0',
'BasicDataSet_v0.TeamChat_v1']


for file in files:
	count = 0
	out_file = open(path + "out/" + file + '.csv', 'w')
	csv_writer = csv.writer(out_file)
	with open(path + file + '.json') as f:
		try:
			for message in f:
				messageDict = json.loads(message)
				if count == 0:
					header = messageDict.keys()
					csv_writer.writerow(header)
					count += 1
				csv_writer.writerow(messageDict.values())
		except:
			continue