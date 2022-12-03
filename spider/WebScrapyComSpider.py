pip install beautifulsoup 4

class BlogSpider(scrapy.Spider):
    name = 'top 250 imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']
    
    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}
            
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

#strong , .secondaryInfo , .titleColumn a -> pega lista de filmes com ano e avaliação

    