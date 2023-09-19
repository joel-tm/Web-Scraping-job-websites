import requests 
from bs4 import BeautifulSoup 
import csv 
  
ch=1 
while ch!=0: 
             print("choose any of the following to show job availability for that 
             particular one in csv files") 
	  print("1.teacher") 
	  print("2.doctor") 
             print("3.Data scientist") 
	  print("4.exit") 
   	 ch=int(input("enter any one from above"))      
	 print("\n") 
  
	 if ch==1: 
         start_url="https://www.indeed.co.in/jobs?q=teacher&l=India" 
         page_data=requests.get(start_url) 
         #sending a http request to the site 
         
        soup=BeautifulSoup(page_data.content,"html.parser") 
       	        #getting that requested data to store in an identifier soup
  
 
'''' 
    	for i in soup:  
#for checking whether the website is scrapable, if its not this will give output - http error 403 -forbidden 


        	print(i)  	
      # This is used for checking what html tags the data we want is under ,its just for understanding


    	'''     
  
    	''' 
    	for finding out which html tags to parse through either print the identifier “soup” with a for loop as done above or go through the google developer  option-inspect element  
    	and find what all data is under each tags and subtags  and iterate through it 


    	''' 
  
         
    with open("teacher.csv","w",newline="",encoding="utf-8-sig") as f:  
	#without encoding=”utf-8-sig” or “utf-8”the code will give error
            
csv_writer=csv.writer(f) 
            csv_writer.writerow(["Title","Company","Location","summary","final_link"]) 
  
             
 for job_tag in soup.find_all("div",class_="jobsearch-SerpJobCard unifiedRow row result"): 
            	
#inside the class_=jobsearch-SerpJobCard unifiedRow row result we gave the class name that has all the data for   title,company,location,summary,link 
  
  
            	title=job_tag.find("h2",class_="title").get_text(strip=True)   
 		##get_text()- will return only the text in tags 


            company=job_tag.find("span",class_="company").get_text(strip=True)  
 ##strip()   - removes all leading and trailing spaces 


            	location = job_tag.find(class_="location").get_text(strip=True) 


            	summary = job_tag.find("div",class_="summary").get_text(strip=True) 


            	link = job_tag.find("a",href=True) 
            base_url="https://www.indeed.com" 
            final_link = base_url + link["href"] 
                 
  
           csv_writer.writerow([title,company,location,summary,final_link]) 
print(“teacher.csv created “)
print()
  
  


  elif ch==2: 
  
  	url="https://www.monster.com/jobs/search/?q=doctor" 
           source_code=requests.get(url) 
           soup=BeautifulSoup(source_code.content,"html.parser") 
      
  
    	with open("doctor.csv","w",newline="",encoding="utf-8-sig") as csv_file: 
           		 csv_writer=csv.writer(csv_file) 
            	csv_writer.writerow(["Title","Company","Location","Link_to_apply"]) 
  
  
        		for job_tag in soup.find_all("section",class_="card-content"): 
            		for summary in job_tag.find_all("div",class_="summary"):  
 #the  div tag with class_=summary tag was inside the section tag 
with class_="card-content"  
 	
   		company=summary.find("div",class_="company").get_text(strip=True) 
                	location=summary.find("div",class_="location").get_text(strip=True) 
                	title=summary.find("h2",class_="title").get_text(strip=True) 
                	links=summary.find("a") 
                       final_link=links["href"] 
  
  
                    csv_writer.writerow([title,company,location,final_link]) 
  
  	print(“moster.csv created “)
print()	
    elif ch==3: 
        start_url="https://www.simplyhired.co.in/search?q=data+scientist&l=India&job=nOROMisrT120E7HmS44yEkXKYqasUTWyw8p17kaD2KUiuHliR8y9bg" 
page_data=requests.get(start_url) 
soup=BeautifulSoup(page_data.content,"html.parser") 
  
  
          with open ("data scientist.csv","w",newline="",encoding="utf-8-sig") as csv_file: 
            csv_writer=csv.writer(csv_file) 
            csv_writer.writerow(['title','company','location','summary','final_link']) 
  
             
        	for job_tag in soup.find_all("div",class_="TwoPane-paneHolder 
TwoPane-paneHolder--left"):                 
            	for next_tag in soup.find_all("article",class_="SerpJob"):     
                	
title=next_tag.find("div",class_="jobposting-title") 


                	company=next_tag.find("span",class_="JobPosting-labelWithIcon jobposting-company").get_text(strip=True) 


                	location=next_tag.find("span",class_="JobPosting-labelWithIcon jobposting-location").get_text(strip=True) 
                	summary=next_tag.find("div",class_="SerpJob-snippetContainer").get_text(strip=True) 
                       base_url="https://www.simplyhired.co.in/" 
                	link=next_tag.find("a",href=True) 
                       link_to_apply=base_url+link["href"] 
  
                     
                    csv_writer.writerow([title,company,location,summary,final_link]) 
  
  	print(“data scientist.csv created “)
print()


    elif ch==4:   
    		break 
  
     
  
''' NOT DISPLAYING THE OUTPUT IN python IDLE BY READING THE CSV FILE AND PRINTING IT, BECAUSE THE CSV TABLE CREATED IS VERY BIG 
  AND CANNOT  FIT IN PYTHON SCREEN 
'''                     
  
  
''' 
tried scraping these websites also 
' https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&p%5B%5D=facets.brand%2
55B%255D%3DApple ' 


' https://www.whitehouse.gov/briefings-statements/   ' 


''' 
