from sys import argv

file_to_parse = argv[1]
with open(file_to_parse,"r") as f: text = f.read()
reqs = text.split("\n")
bad_packages = ["PAM","Pmw","PyAudio","adium-theme-ubuntu","apt-xapian-index","command-not-found","debtagshw","defer","dirspec","duplicity","gyp","oneconf","pygobject","python-apt","python-daemon","python-dateutil","python-debian","python-gflags","python-xlib","sessioninstaller","software-center-aptd-plugins","system-service","unity-lens-photos","xdiagnose"]
new_reqs = []
for line in reqs:
    bad_package = False
    for package in bad_packages:
        if package in line: bad_package = True
    if bad_package: continue
    new_reqs.append(line)

text = "\n".join(new_reqs)
with open(file_to_parse,"w") as f: f.write(text)
