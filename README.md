
# WhatsApp Chat Processor

Upload your WhatsApp group chat history text file and it will list the frequency of the most common words used by your group and who talks the most!

## How The Idea Came to Be
After taking a course in Natural Language Processing, I was curious to see what kind of words me and my friends used the most in our WhatsApp group chat. I know each group chat has their own style of writing and words they use often, so I was curious as to what words my group used most frequently, and the results were of course no surprise.

Created in Python, using the NTLK library and pandas to parse and tokenize the words. Deployed using Flask on reverse proxy with NGINX on a Google Compute Engine.

## Getting Started
First export the WhatsApp text history by opening the group chat on your phone.  
Tap > More > Export chat. Tap Without media. 

### [Here is the ink to check it out](http://35.197.84.142)

**Note:** It may take awhile to process the text since it's a large text file

**Disclaimer:** The uploaded text files are processed for the purpose of this application and are not stored or retained on any servers.

Or if you have trust issues, like myself, you can:
## Get Started Locally




```
git clone https://github.com/WiL11o6/whatsapp-process
```
Navigate to where it's cloned, make sure you have Python on your computer
```
cd .\whatsapp-process\
python app.py
```
Open up your browser of choice and navigate to http://localhost:8080

# 🚀 About Me
Hi, I'm Wilson,  
And I'm aspiring to be a software engineer creating one project a time.


