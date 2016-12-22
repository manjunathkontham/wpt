import requests
import time
import re

timestr = time.strftime("%Y%m%d-%H%M%S")
r = requests.post('http://www.webpagetest.org/runtest.php?url=my.xfinity.com%2F%3Fmyxfn%3Dtrue&runs=1&f=xml&k=A.6a1a4e141439bfda5e6647be8fac4e26')
result_XML=r.text

m = re.search('<jsonUrl>.*</jsonUrl>',result_XML)
jsonUrl=m.group(0).strip('<jsonUrl>').strip('</jsonUrl>')
print(jsonUrl)

m = re.search('<userUrl>.*</userUrl>',result_XML)
userUrl=m.group(0).strip('<userUrl>').strip('</userUrl>')
print(userUrl)
 
r = requests.post(jsonUrl)
jsonresult=r.text
r = re.compile('\"statusText\":\"(.*?)\"')
m = r.search(jsonresult)
statusText=m.group(1)
print(statusText)

while statusText!='Test Complete':

	time.sleep(30)
	r = requests.post(jsonUrl)
	jsonresult=r.text
	r = re.compile('\"statusText\":\"(.*?)\"')
	m = r.search(jsonresult)
	statusText=m.group(1)
	print(statusText)

m = re.search('\"average\":.*\"avgRun\":1}}',jsonresult)
trimmed_result=m.group(0)

m=re.search('\"firstView\":{.*\"avgRun\":1},',trimmed_result)
first_view=m.group(0)

m=re.search('\"repeatView\":{.*\"avgRun\":1}}',trimmed_result)
repeat_view=m.group(0)

r = re.compile('\"loadTime\":(.*?),')
m = r.search(first_view)
load_time=m.group(1)

r = re.compile('\"TTFB\":(.*?),')
m=r.search(first_view)
first_byte=m.group(1)

r = re.compile('\"render\":(.*?),')
m=r.search(first_view)
start_render=m.group(1)

r = re.compile('\"userTime\":(.*?),')
m=r.search(first_view)
user_time=m.group(1)

r = re.compile('\"visualComplete\":(.*?),')
m=r.search(first_view)
visually_complete=m.group(1)

r = re.compile('\"SpeedIndex\":(.*?),')
m=r.search(first_view)
speed_index=m.group(1)

r = re.compile('\"domElements\":(.*?),')
m=r.search(first_view)
DOM_elements=m.group(1)

r = re.compile('\"docTime\":(.*?),')
m=r.search(first_view)
doc_complete_time=m.group(1)

r = re.compile('\"requestsDoc\":(.*?),')
m=r.search(first_view)
doc_complete_requests=m.group(1)

r = re.compile('\"bytesInDoc\":(.*?),')
m=r.search(first_view)
doc_complete_bytes_In=m.group(1)

r = re.compile('\"fullyLoaded\":(.*?),')
m=r.search(first_view)
fully_loaded_time=m.group(1)

r = re.compile('\"requestsFull\":(.*?),')
m=r.search(first_view)
fully_loaded_requests=m.group(1)

r = re.compile('\"bytesIn\":(.*?),')
m=r.search(first_view)
fully_loaded_bytes_In=m.group(1)


Output="WPT_First&Repeat_View"
file_name_to_use=Output+timestr+".txt"

output_file = open(Output+timestr+".txt", "w")

output_file.write("Results URL for Reference:  "+userUrl+"\nJson Results URL for Reference: "+jsonUrl+"\n\n----------------------- First View Numbers -----------------------\nLoad time-->"+load_time+"\nfirst_byte-->"+first_byte+"\nstart_render-->"+start_render+"\nuser_time-->"+user_time+"\nvisually_complete-->"+visually_complete+"\nspeed_index-->"+speed_index+"\nDOM_elements-->"+DOM_elements+"\ndoc_complete_time-->"+doc_complete_time+"\ndoc_complete_requests-->"+doc_complete_requests+"\ndoc_complete_bytes_In-->"+doc_complete_bytes_In+"\nfully_loaded_time-->"+fully_loaded_time+"\nfully_loaded_requests-->"+fully_loaded_requests+"\nfully_loaded_bytes_In-->"+fully_loaded_bytes_In+"\n-----------------------------------------------------------------\n")
output_file.close()

r = re.compile('\"loadTime\":(.*?),')
m = r.search(repeat_view)
load_time=m.group(1)

r = re.compile('\"TTFB\":(.*?),')
m=r.search(repeat_view)
first_byte=m.group(1)

r = re.compile('\"render\":(.*?),')
m=r.search(repeat_view)
start_render=m.group(1)

r = re.compile('\"userTime\":(.*?),')
m=r.search(repeat_view)
user_time=m.group(1)

r = re.compile('\"visualComplete\":(.*?),')
m=r.search(repeat_view)
visually_complete=m.group(1)

r = re.compile('\"SpeedIndex\":(.*?),')
m=r.search(repeat_view)
speed_index=m.group(1)

r = re.compile('\"domElements\":(.*?),')
m=r.search(repeat_view)
DOM_elements=m.group(1)

r = re.compile('\"docTime\":(.*?),')
m=r.search(repeat_view)
doc_complete_time=m.group(1)

r = re.compile('\"requestsDoc\":(.*?),')
m=r.search(repeat_view)
doc_complete_requests=m.group(1)

r = re.compile('\"bytesInDoc\":(.*?),')
m=r.search(repeat_view)
doc_complete_bytes_In=m.group(1)

r = re.compile('\"fullyLoaded\":(.*?),')
m=r.search(repeat_view)
fully_loaded_time=m.group(1)

r = re.compile('\"requestsFull\":(.*?),')
m=r.search(repeat_view)
fully_loaded_requests=m.group(1)

r = re.compile('\"bytesIn\":(.*?),')
m=r.search(repeat_view)
fully_loaded_bytes_In=m.group(1)


output_file = open(file_name_to_use, "a")
output_file.write("------------------------ Repeat View Numbers --------------------\nLoad time-->"+load_time+"\nfirst_byte-->"+first_byte+"\nstart_render-->"+start_render+"\nuser_time-->"+user_time+"\nvisually_complete-->"+visually_complete+"\nspeed_index-->"+speed_index+"\nDOM_elements-->"+DOM_elements+"\ndoc_complete_time-->"+doc_complete_time+"\ndoc_complete_requests-->"+doc_complete_requests+"\ndoc_complete_bytes_In-->"+doc_complete_bytes_In+"\nfully_loaded_time-->"+fully_loaded_time+"\nfully_loaded_requests-->"+fully_loaded_requests+"\nfully_loaded_bytes_In-->"+fully_loaded_bytes_In+"\n------------------------------------------------------------------")

output_file.close()