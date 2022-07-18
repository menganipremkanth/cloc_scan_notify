# cloc_scan_notify
python script to run cloc and send results to given email ID.

**This script tested on MAC and Windows 10 , it works on both. It also works with both Python 2 and Python 3 versions.

USAGE:
Python cloc_scan.py <repo/directory or file to be scanned> <output CSV file name>
  
example 1:
(base) pk:cloc_scan_notify premmengani$ python cloc_scan.py log4jscanner/ cloc_scan_output_July18th.csv
Please enter the email address to which the scan result need to be sent to:  
mengani.premkanth1@gmail.com
      29 text files.
      23 unique files.                              
      51 files ignored.
Wrote cloc_scan_output_July18th.csv
(base) pk:cloc_scan_notify premmengani$ cat cloc_scan_output_July18th.csv 
github.com/AlDanial/cloc v 1.94  T=0.12 s (187.5 files/s, 28300.7 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Go                              16            282            523           2217
Markdown                         2             44              0            131
Bourne Shell                     3             36             49            123
YAML                             2              2              0             64
-------------------------------------------------------------------------------
SUM:                            23            364            572           2535
-------------------------------------------------------------------------------
(base) pk:cloc_scan_notify premmengani$ date
Mon Jul 18 09:30:00 IST 2022
(base) pk:cloc_scan_notify premmengani$ 



![Screen Shot 2022-07-18 at 9 33 39 AM](https://user-images.githubusercontent.com/7415579/179443828-6ff8130c-2441-4453-9b94-d4855624976f.png)
![Screen Shot 2022-07-18 at 9 35 03 AM](https://user-images.githubusercontent.com/7415579/179443869-18f5e496-4280-4b58-b45a-21bfc739b782.png)




References,

1) Cloc:cloc counts blank lines, comment lines, and physical lines of source code in many programming languages.

https://github.com/AlDanial/cloc

3)What is Amazon SES?
Amazon Simple Email Service (SES) is a cloud-based email service that provides cost-effective, flexible and scalable way for businesses of all sizes to                                              keep in contact with their customers through email.
https://docs.aws.amazon.com/ses/latest/dg/Welcome.html

2)https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

3)Watch "How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More" on YouTube
https://youtu.be/JRCJ6RtE3xU

4)Watch "Send Emails with Python & Amazon SES" on YouTube
https://youtu.be/nKNqNrdUtZU

5)Watch "Python Quick Tip: Hiding Passwords and Secret Keys in Environment Variables (Windows)" on YouTube
https://youtu.be/IolxqkL7cD8
