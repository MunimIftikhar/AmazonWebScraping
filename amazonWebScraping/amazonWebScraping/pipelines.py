# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import JsonItemExporter
from pathlib import Path

#save extracted data into the json file using pipelines
class AmazonwebscrapingPipeline:
    def __init__(self):
        self.data_folder = Path("amazonWebScraping/json/")
        self.json_file = self.data_folder / "data.json"
        self.file = open( self.json_file , 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
