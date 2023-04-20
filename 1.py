import time
import sys
original_stdout = sys.stdout # Save a reference to the original standard output

f = open('/codebuild/output/log', 'w')
sys.stdout = f # Change the standard output to the file we created.

for i in range(1,100):
  print(i)
  time.sleep(3)
sys.stdout = original_stdout # Reset the standard output to its original value

print('======================')
