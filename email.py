import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute("Drop Table if EXISTS Counts")
cur.execute("""CREATE TABLE Counts(emailtext, count INTEGER)""")

fname = input('Enter file name: ')
if (len(fname) < 1):
fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startwith('from: '):
		continue
	pieces = line.split()
	email = pieces[1]
	cur.execute('SELECT Count FROM Counts WHERE email = ?, (email))
	row = cur.fetchone()
if row is None:
		cur.execute('''INSERT INTO Counts(email, Count) Values(?, 1)''', (email))
	else:
		cur.execute('update counts SET Count = Count + 1 WHERE email = ?', (email, ))
	conn.commit()
sqlstr = 'SELECT email, Count from Counts ORDER BY Count DESC limit 10'
for row in cur.execute(sqlstr):
	print(str(row[0], row[1]))
cur.close()
