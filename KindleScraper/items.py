# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import (MapCompose,
                                    Join)

from w3lib.html import remove_tags

def col_whitespace(data):
    # print('\n\ndata:', data)
    # if data != None:
    return data.split('\n')[0].strip()

def first_num_from_str(data):
    return [int(i) for i in data.replace('#', ' ').split() if i.isdigit()][0]

def nums_from_str_hash(data):
    return [int(i) for i in data.replace('#', ' ').split() if i.isdigit()]

def nums_from_str_percent(data):
    return [int(i) for i in data.replace('%', ' ').split() if i.isdigit()]

def first_num_from_str_coma(data):
    return [int(i) for i in data.replace(',', '').split() if i.isdigit()][0]

def price(data):
    # print('\n\n',data)
    data1 = data.split('\n')[0].strip()
    data2 = float(data.split('₹')[1].split()[0])
    # data3 = [int(i) for i in data2.split() if i.isdigit()][0]
    return { data1:data2 }
    
    
class KindleProductDetails(scrapy.Item):
    
    
    product_value = scrapy.Field()
    
    product_type=scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip, price)
    )
    
    product_col = scrapy.Field(
        input_processor = MapCompose(col_whitespace),
    )
    best_seller=scrapy.Field(
        input_processor = Join(),
        output_processor = MapCompose(nums_from_str_hash)
        
    )
    best_seller_rank=scrapy.Field(
        input_processor = Join(),
        output_processor = MapCompose(first_num_from_str)
    )
    other_cat=scrapy.Field()
    
    total_reviews = scrapy.Field(
        input_processor = Join(),
        output_processor = MapCompose(first_num_from_str_coma)
    )
    reviews_percent = scrapy.Field(
        input_processor = Join(),
        output_processor = MapCompose(nums_from_str_percent)
    )


class KindleProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    product_value = scrapy.Field()
    product_col=scrapy.Field()
    best_seller=scrapy.Field()
    other_cat=scrapy.Field()

class KindleScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    p_name = scrapy.Field()
    p_reviews=scrapy.Field()
    p_price=scrapy.Field()
    url=scrapy.Field()