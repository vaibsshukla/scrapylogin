
BOT_NAME = 'scrapylogin'

SPIDER_MODULES = ['scrapylogin.spiders']
NEWSPIDER_MODULE = 'scrapylogin.spiders'


ROBOTSTXT_OBEY = False

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
