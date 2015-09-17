

key = "tel"
order = 3
logfile = open("./" + key + "_log_file", "r")
resultfile = open("./" + key + "_result_file", "w")
sent = False

for l in logfile:
    msg = l.strip()

    if sent:
        resultfile.write(msg.split("Deal with")[order].split("\\n")[-2].split("<br>")[0] + "\n")
        #print msg.split("Deal with")[order].split("\\n")[-2].split("<br>")[0]
        sent = False

    if "Packet sent" not in msg:
        continue

    resultfile.write(msg.split(key + "=")[-1].split("&")[0] + " : ")
    #print msg.split(key + "=")[-1].split("&")[0]

    sent = True






