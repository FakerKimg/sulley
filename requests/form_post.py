from sulley import *
########################################################################################################################
# All POST mimetypes that I could think of/find
########################################################################################################################
# List of all blocks defined here (for easy copy/paste)
"""
sess.connect(s_get("HTML FORM POST"))
"""

def s_file_group(name, data_file):
    group = []

    data_file.seek(0)
    for line in data_file:
        if line.startswith('#'):
            continue

        group.append(line)

    s_group(name, group)

    return


########################################################################################################################
# Basic fuzz of form post payloads
########################################################################################################################

def form_post_requests(inputs_form, data_file):
    count = 0
    for form in inputs_form:
        s_initialize("HTTP VERBS POST" + str(count))
        s_static("POST " + form["action"] + " HTTP/1.1\r\n")
        s_static("Content-Type: ")
        s_static("application/x-www-form-urlencoded")
        #s_string("application/x-www-form-urlencoded")
        s_static("\r\n")
        s_static("Host: ")
        s_static("www.hhserver.com\r\n")
        s_static("Content-Length: ")
        s_size("post blob", format="ascii", signed=True, fuzzable=False)
        #s_size("post blob", format="ascii", signed=True, fuzzable=True)
        s_static("\r\n\r\n")
        if s_block_start("post blob"):
            for key in form["payload"].keys()[:-1]:
                s_static(key)
                #s_static('=' + form["payload"][key] + '&')
                s_static("=")
                #s_string(form["payload"][key])
                #s_delim("&")
                s_file_group("group_" + key, data_file)
                if s_block_start(name="block_" + key, group="group_" + key):
                    s_static('&')
                s_block_end()

            s_static(form["payload"].keys()[-1])
            s_static("=")
            #s_string(form["payload"][form["payload"].keys()[-1]])
            s_file_group("group_" + form["payload"].keys()[-1], data_file)
            if s_block_start(name = "block_" + form["payload"].keys()[-1], group = "group_" + form["payload"].keys()[-1]):
                s_static("")
            s_block_end()

        s_block_end()
        #s_static("\r\n\r\n")

        count = count + 1

