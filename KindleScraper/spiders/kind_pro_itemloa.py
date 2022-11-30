import scrapy
from ..items import KindleProductDetails

from itemloaders import ItemLoader

class KindleBotSpider(scrapy.Spider):
    name = 'kindle-product-itemloader'
    count=1
    start_urls = [
        # 'file:D:\Codes\Python\KindleScraper\product.html'
        'https://www.amazon.in/dp/B07BHG29M6'
        # "https://www.amazon.com/s?k=iphone&page=1&qid=1624792241&ref=sr_pg_2"               
        ]

    def parse(self, response):
        
        
        loader = ItemLoader(item=KindleProductDetails(), selector=response)
        
        
        loader.add_value('response', response.body)
        

        loader.add_value('requestbody', str(response.request.headers))
        loader.add_value('request', response.request)
        
        # value=response.css("#detailBullets_feature_div .a-text-bold+ span::text").extract()
        # col=response.css("#detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold::text").extract()
        
        loader.add_css('product_value' , '#detailBullets_feature_div .a-text-bold+ span::text')
        loader.add_css('product_col' , '#detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold::text')
        loader.add_css('best_seller' , '#detailBullets_feature_div+ .detail-bullet-list > li > .a-list-item span::text')
        loader.add_css('other_cat' , '.zg_hrsr a::text')
        loader.add_css('best_seller_rank', '#detailBullets_feature_div+ .detail-bullet-list > li > .a-list-item::text')

        
        loader.add_css('total_reviews' , '.averageStarRatingNumerical .a-color-secondary::text')
        loader.add_css('reviews_percent' , '.a-nowrap .a-link-normal::text')
        
        loader.add_css('product_type' , '#tmmSwatches .a-button-text')
        
        
        item = loader.load_item()
        yield item 
        
        # product=KindleProductItem()
        # product["product_value"]=value
        # product["product_col"]=col
        # product["best_seller"]=best_seller
        # product["other_cat"]=other_cat
        # yield product