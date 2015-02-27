import mechanize
import sys

br=mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_proxies({"http":"sat1:py7199@webcache.cdotb.ernet.in:8080"})

url = "http://eis.cdotb.ernet.in/selemp.htm"

br.open(url)

for form in br.forms():
	print form.name
	print form
	print "\n ---- end \n"

br.select_form('emp')
br.form['group']=sys.argv[1]
br.submit()

g=sys.argv[1]

f=open("%s.txt"%(g),"wb")
f.write(br.response().read())
f.close()

with open("/home/cdot/Documents/CDOT-SATWL/%s.txt" % (g),'rb') as f:
	while 1:
		line=f.readline()
		#print 'w1'
		if line[:17]=='<tr class="tdodd"':
			#print 'if1'
			while 1:
				#print 'w2'
				line=f.readline()
				if not line:
					break
				else:
					#print 'else1'
					if line[:3]=='<tr':
						#print 'if2'
						count=0
						while line[:2] != '</':
							#print 'w3'
							line=f.readline()
							if line[:3]=='<td':
								count=count+1
								if count==2:
									empid=line[15:19]
									print
									print
									print empid
									
								if count==3:
									index=line.find('&nbsp;&nbsp;')
									name=line[15:index]
									name=name.strip()
									print name

								if count==9:
									index=line.find('</td')
									emailid=line[15:index]
									print emailid

			break




