# scraping-javascript-pages using scrapy splash 

First download and install docker 

Setting up Splash using Docker 
First run docker desktop
Run this command to stop all running containers: docker stop $(docker ps -aq)

Then run this command :
sudo docker run -it -p 8050:8050 scrapinghub/splash --disable-private-mode
It is necessary to run it by disabling private mode so that the page renders correctly.

Now that Splash is running, you can test it in your browser:
http://localhost:8050/

http://approved.me.jaguar.com/en_qa/used/qatar - This is the website I've written this code for.

The main difference between a normal spider and this one is in its settings.py .Please refer to that file .
