"""
示例爬虫

从指定网站爬取数据
"""

import scrapy


class ExampleSpider(scrapy.Spider):
    """示例爬虫类"""
    
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        """
        解析响应
        
        Args:
            response: Scrapy Response 对象
            
        Yields:
            抓取的数据项
        """
        # 提取标题
        title = response.css("h1::text").get()
        
        # 提取链接
        links = response.css("a::attr(href)").getall()
        
        # 返回数据
        yield {
            "url": response.url,
            "title": title,
            "links_count": len(links),
        }
        
        # 跟进链接（可选）
        # for link in links:
        #     yield response.follow(link, callback=self.parse)

    def closed(self, reason):
        """爬虫关闭时调用"""
        self.logger.info(f"爬虫关闭: {reason}")

