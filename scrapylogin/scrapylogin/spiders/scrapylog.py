# -*- coding: utf-8 -*-
import scrapy	
from scrapy.http import Request, FormRequest
import requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class ScrapylogSpider(scrapy.Spider):
    name = 'scrapylog'
#  def __init__(self, *args, **kwargs): 
#    super(ScrapylogSpider, self).__init__(*args, **kwargs) 
#    self.start_urls = [kwargs.get('start_url')] 
#    self.log('reached----------------------')
#    yield scrapy.Request(start_urls,callback('redirecting to url-->'))

    username = 'vaibhavshukla2811@gmail.com'
    password = 'Junipers234!'
    login_url = 'https://www.linkedin.com/uas/login'
   
 	  
    rules = (Rule(LinkExtractor(allow=('')), callback="parse_item", follow= True),
    )
	
    def start_requests(self):
        yield scrapy.Request(self.login_url, self.parse_login,)
		
		
    def parse_login(self, response):
      self.logger.info( "Visited %s", response.url)
      return FormRequest.from_response(response,
            formdata={'session_key': 'vaibhavshukla2811@gmail.com', 'session_password': 'JUnipers234!'},
            callback=self.check_login_response)
			
    def check_login_response(self, response):
      if "profile" in response.body:
        self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
        self.log('Hi, this is an item page! %s' % response.url)
 	yield scrapy.Request(response.url,self.parse_items)          # website contains pdf
#        rules = (Rule(LinkExtractor(allow=('')), callback="parse_items", follow= True),
#        )
      else:
        self.log("\n\n\nFailed, Bad times :(\n\n\n")
		
  
    def parse_items(self, response):
      self.log("--------------------------------->")
      links = []
      for link in response.xpath('//a'):
            item = ScrapyloginItem()
            item["title"] = link.select("text()").extract()
            item["link"] = link.select("@href").extract()
            item["page"] = response.url   
			# extract returns a unicode list, ''.join converts it into a string
            if "pdf" in ''.join(item["link"]):
                links.append(''.join(item["link"]))
      for x in links:
        a = urlparse(x)
        filename = os.path.basename(a.path)
        r = requests.get(x)
        with open(filename, 'wb') as f:
          f.write(r.content)

