# -*- coding:utf-8 -*-
# Scrapy settings for scrmusic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrmusic'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrmusic.spiders']
NEWSPIDER_MODULE = 'scrmusic.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
#禁止cookies,防止被ban
#COOKIES_ENABLED = True
ITEM_PIPELINES = {
    'scrmusic.pipelines.ScrmusicPipeline':300
}

