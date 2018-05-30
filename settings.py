# -*- coding: utf-8 -*-

# Scrapy settings for huurwoningen project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')

BOT_NAME = 'huurwoningen'

SPIDER_MODULES = ['huurwoningen.spiders']
NEWSPIDER_MODULE = 'huurwoningen.spiders'

FEED_EXPORT_FIELDS = ['ANNONCE_LINK', 'FROM_SITE', 'ID_CLIENT', 'ANNONCE_DATE', 'ACHAT_LOC', 'MAISON_APT', 'CATEGORIE', 'NEUF_IND', 'NOM', 'ADRESSE', 'CP', 'VILLE', 'QUARTIER', 'DEPARTEMENT', 'REGION', 'PROVINCE', 'ANNONCE_TEXT', 'ETAGE', 'NB_ETAGE', 'LATITUDE', 'LONGITUDE', 'M2_TOTALE', 'SURFACE_TERRAIN', 'NB_GARAGE', 'PHOTO', 'PIECE', 'PRIX', 'PRIX_M2', 'URL_PROMO', 'PAYS_AD', 'PRO_IND', 'SELLERTYPE', 'MINI_SITE_URL', 'MINI_SITE_ID', 'AGENCE_NOM', 'AGENCE_ADRESSE', 'AGENCE_CP', 'AGENCE_VILLE', 'AGENCE_DEPARTEMENT', 'EMAIL', 'WEBSITE', 'AGENCE_TEL', 'AGENCE_TEL_2', 'AGENCE_TEL_3', 'AGENCE_TEL_4', 'AGENCE_FAX', 'AGENCE_CONTACT', 'PAYS_DEALER', 'FLUX', 'SITE_SOCIETE_URL', 'SITE_SOCIETE_ID', 'SITE_SOCIETE_NAME', 'AGENCE_RCS', 'SPIR_ID']

## More comprehensive list can be found at 
## http://techpatterns.com/forums/about304.html
#USER_AGENT_LIST = [
#    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
#    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
#    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
#]
#HTTP_PROXY = 'http://127.0.0.1:8123'
#DOWNLOADER_MIDDLEWARES = {
#     'huurwoningen.middlewares.RandomUserAgentMiddleware': 400,
#     'huurwoningen.middlewares.ProxyMiddleware': 410,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 200,
#     'huurwoningen.middlewares.RetryChangeProxyMiddleware': 600,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
#}

#USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

#DOWNLOAD_DELAY = 0.25

#DOWNLOADER_MIDDLEWARES = {
#'scrapy_splash.SplashCookiesMiddleware': 723,
#'scrapy_splash.SplashMiddleware': 725,
#'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
#'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
#'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#'scrapy_proxies.RandomProxy': 100,
#}

#SPIDER_MIDDLEWARES = {
#'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
#}

#SPLASH_URL = 'http://localhost:8050/'
#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

#PROXY_LIST = '/home/databiz33/Documents/list.txt'
#PROXY_MODE = 0

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 456]



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kamers (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'kamers.middlewares.KamersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'kamers.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'huurwoningen.pipelines.HuurwoningenPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#HTTPCACHE_IGNORE_MISSING = True
