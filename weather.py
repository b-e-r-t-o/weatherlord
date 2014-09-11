import optparse, urllib2, json

def main():
	u = optparse.OptionParser()
	u.add_option('--url', '-u', default="http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datacategoryid=TEMP&SKY&PRESlimit=10&offset=5")
	options, arguments = u.parse_args()
	link =  str(options.url)
	nl = '\n'
	noaa = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/'
	source = noaa + link

	req = urllib2.Request(source)
	req.add_header('Token', 'request a token') // request a token at http://www.ncdc.noaa.gov/cdo-web/token

	try:
		resp = urllib2.urlopen(req)
		content = resp.read()
		print nl + content + nl
		print source + nl 
		print link + nl 

	except urllib2.URLError:
		print 'Oops! Timeout Error! Sorry!'

if __name__ == '__main__':
	main()

