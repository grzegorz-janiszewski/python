import subprocess

out = subprocess.Popen(["ls", "-ll"], stdout=subprocess.PIPE)
print(out.communicate()[0])
