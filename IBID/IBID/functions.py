import re

def get_ip_fields(Model):
	fieldList=[]
	ipList=[]
	fields=Model._meta.get_fields()
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		if i.concrete:
			m=ip_pattern.match(i.name)
			if m:
				ip_field=m.group(0)
				ipList.append(ip_field)
	return ipList