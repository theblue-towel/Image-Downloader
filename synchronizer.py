from scraper import Scraper
import asyncio, threading

async def async_find_images(scraper, x_search, y_search, x_type, y_type):

     # Assuming s.findImages is an async function
     await scraper.findImages(x_search, y_search, x_type, y_type)

def run_async_in_thread(scraper, x_search, y_search, x_type, y_type):
     # Create a new event loop for this thread
     loop = asyncio.new_event_loop()
     asyncio.set_event_loop(loop)

     loop.run_until_complete(async_find_images(scraper, x_search, y_search, x_type, y_type))
     loop.close()

class Sync():

     def __init__(self):
          pass

     def makeImages(self,  x_search, y_search, x_type, y_type):
          print("Initializing threads")
          s = Scraper()

          threads = []

          # Start threads
          for i in range(10):
               thread = threading.Thread(target=run_async_in_thread, args=(s, x_search, y_search, x_type, y_type))
               threads.append(thread)
               thread.start()

          # Wait for threads to finish
          for thread in threads:
               thread.join()