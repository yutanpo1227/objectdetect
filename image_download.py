from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "img"})
crawler.crawl(keyword="ロボカップジュニア　サッカー　ロボット", max_num=100)