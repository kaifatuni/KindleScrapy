import scrapy
from ..items import KindleProductItem

class KindleBotSpider(scrapy.Spider):
    name = 'kindle-product'
    count=1
    start_urls = [
        'https://www.amazon.in/dp/B074LZG7KS'
        # "https://www.amazon.com/s?k=iphone&page=1&qid=1624792241&ref=sr_pg_2"               
        ]

    def parse(self, response):
        product=KindleProductItem()
        
        value=response.css("#detailBullets_feature_div .a-text-bold+ span::text").extract()
        col=response.css("#detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold::text").extract()
        
        #detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold
        
        
        best_seller=response.css("#detailBullets_feature_div+ .detail-bullet-list > li > .a-list-item span").extract()
        
        other_cat=response.css(".zg_hrsr .a-list-item span").extract()
        
        print('value',value)
        # no_reviews=response.css(".sg-col-12-of-20 .a-link-normal .a-size-base").css("::text").extract()
        # price=response.css(".sg-col-12-of-20 .a-price-whole::text").extract()
        # image_url=response.css("#detailBulletsWrapper_feature_div #detailBullets_feature_div .a-text-bold::text").css("::attr(src)").extract()
        product["product_value"]=value
        product["product_col"]=col
        product["best_seller"]=best_seller
        product["other_cat"]=other_cat
        yield product
    
        # KindleBotSpider.count+=1
        # nxt_page="https://www.amazon.com/s?k=heaphones&page="+str(KindleBotSpider.count)+"&qid=1624791620&ref=sr_pg_3"
        # nxt_iphone_page="https://www.amazon.com/s?k=iphone&page="+str(KindleBotSpider.count)+"&qid=1624792241&ref=sr_pg_2"
        # if KindleBotSpider.count<6:
        #     yield response.follow(nxt_page,callback=self.parse)
        #     yield response.follow(nxt_iphone_page,callback=self.parse)