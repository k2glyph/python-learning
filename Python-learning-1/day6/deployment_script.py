import sys
import git
import os
# 
def git_pull():
    g = git.cmd.Git("test")
    g.checkout(".")
    g.pull()
# 
def replace_content_of_file(filename):
    with open(f"{filename}", "r") as f:
        text= f.read().replace('\n', '').replace('\t', '').replace('content-text', "\n")
    with open(f"{filename}", 'w') as output:
        output.write(text)
# 
def main():
    arr = sys.argv[1].split(',')
    git_pull()
    os.chdir("test")
    print(f"Current Directory is: {os.getcwd()}")
    for i in range(len(arr)):
        filename=arr[i]
        print(f"------------------Starting on {filename}------------------------")
        replace_content_of_file(filename)
        print(f"------------------Completed on {filename}------------------------")

main()