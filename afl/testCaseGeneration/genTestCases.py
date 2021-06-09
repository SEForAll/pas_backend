from shutil import copyfile
import docker
import os
import subprocess
import tarfile
from io import BytesIO

def run(codeDir, inputDir, outputDir, time):
    client = docker.from_env()
    #container = client.containers.run("aflplusplus/aflandcmake", "bash", detach=True)
    container = client.containers.run("aflplusplus/aflandcmake", "/bin/bash" , volumes={os.getcwd() + "/copyIn": {'bind':'/root/', 'mode': 'rw'}}, detach=True, tty=True)
    container.start()
    print(container.name)
    #container.exec_run
    #container.stop()
    print("Script Complete")

def populateFiles():
    return

def copyToRoot(path):
    return

if __name__ == "__main__":
    run("~/temp/push/test/code", "~/temp/push/test/inputs", "~/temp/push/test/outputs", 10)
