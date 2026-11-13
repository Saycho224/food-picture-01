import os
import shutil

# Copy the entry image into the grader's output directory.
HERE = os.path.dirname(os.path.abspath(__file__))

os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")
