import subprocess
biOne = subprocess.run("./binary", capture_output=True)
biTwo = subprocess.run("./binary", capture_output=True)
if(biOne == biTwo):
    print("A match")
else:
    print("Failed to match")
