# Write a python script that will generate the SQL table T500.

# Table with name T500, (ID integer) with 500 insert statements.

with open('sql_t500.txt', 'w') as f:
	f.write('CREATE TABLE T500 (ID INTEGER);\n')
	for x in range(500):
		f.write('INSERT INTO T500 VALUES ({0}); \n'.format(x+1))

print('Python Program Completed.')