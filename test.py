import os
from time import strftime

modTimesinceEpoc = os.path.getmtime('model_cv.h5')
# Convert seconds since epoch to readable timestamp
modificationTime = strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
print("Last Modified Time : ", modificationTime )