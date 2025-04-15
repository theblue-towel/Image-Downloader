import os
import tensorflow as tf

class Verifier:
    
     def __init__(self):

          self.purged = 0

     def delete_corrupted_images(self, directory):
          for dirpath, _, filenames in os.walk(directory):
               for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                         try:
                              img = tf.io.read_file(file_path)
                              img = tf.image.decode_image(img)
                         except Exception:
                              print(f"Deleting corrupted image: {file_path}")
                              os.remove(file_path)