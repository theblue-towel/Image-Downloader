from duckduckgo_search import DDGS
import urllib.request
import os
import random
import string

def betterLen(my_list):
     counter = 0
     for element in my_list:
          counter += 1
     return counter

def shuffle_list(my_list):
    # Determine the length of the list using betterLen
    length = betterLen(my_list)
    
    # Perform the Fisher-Yates shuffle
    for i in range(length - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        
        # Swap the elements at indices i and j
        my_list[i], my_list[j] = my_list[j], my_list[i]
    
    return my_list

class Scraper:
    
     def __init__(self):

          self.names = []

     async def findImages(self, x_search, y_search, x_type, y_type):
          x_copy = x_search.copy()
          y_copy = y_search.copy()
        
        # Shuffle the copies
          x_copy = shuffle_list(shuffle_list(x_copy))
          y_copy = shuffle_list(shuffle_list(y_copy))

          if random.randint(1, 2) == 1: #change to 1 or 5
               search_terms = x_copy + y_copy
               save_dirs = [f"dataset/{x_type}"] * betterLen(x_copy) + [f"dataset/{y_type}"] * betterLen(y_copy)
          else:
               search_terms = y_copy + x_copy
               save_dirs = [f"dataset/{y_type}"] * betterLen(y_copy) + [f"dataset/{x_type}"] * betterLen(x_copy)
          errors = 0
          for term, folder in zip(search_terms, save_dirs):
               
               print(f"Creating folder: {folder}")  # Debugging
               os.makedirs(folder, exist_ok=True)

               results = DDGS().images(term, max_results=40)
               if not results:
                    print(f"No results for: {term}")
                    continue
          
               for i, img in enumerate(results):
                    try:
                         img_url = img["image"]
                         if (img_url.endswith(".jpg") or img_url.endswith(".png") or img_url.endswith(".jpeg") or img_url.endswith(".tiff")):
                              #namegen
                              notDone = True
                              possible = ''
                              while notDone:
                                   possible = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 250)))
                                   if possible not in self.names:
                                        self.names.append(possible)
                                        notDone = False

                              urllib.request.urlretrieve(img["image"], f"{folder}/{possible}.jpeg")
                    except Exception as e:
                         print(e)
                         errors += 1
          print(f'{errors} images lost')
