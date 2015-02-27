import sys
import MySQLdb as mdb



print "\n Connecting to laptops database .....\n"
con = mdb.connect('localhost','laptopUser','laptopUser','laptops')
print "\n connection established \n"
cur = con.cursor()


with open("/home/cdot/Documents/CDOT-SATWL/clinventory/clinventory/static/%s" % (sys.argv[1]),'rb') as f:
	while 1:
		line=f.readline()
		if not line:
			break
		else:
			if line[:3]=='<tr':
				count=0
				while line[:2] != '</':
					line=f.readline()
					if line[:3]=='<td':
						count=count+1
						if count==2:
							empid=line[15:19]
							
						if count==3:
							index=line.find('&nbsp;&nbsp;')
							name=line[15:index]
							name=name.strip()

						if count==9:
							index=line.find('</td')
							emailid=line[15:index]

				q="INSERT INTO satwlInfo (name, empID, emailID) VALUES ('%s','%s','%s')" % ( name,empid,emailid)
				cur.execute(q)


con.commit()
cur.close()
con.close()

print "\n connection closed"

						


		





