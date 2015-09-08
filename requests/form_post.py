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

def form_post_requests(forms, datas):
    form_count = 0
    for form in forms:
        s_initialize("HTTP VERBS POST" + str(form_count))
        form_count = form_count + 1
        s_static("POST " + form["action"] + " HTTP/1.1\r\n")
        s_static("Content-Type: ")
        s_static("application/x-www-form-urlencoded")
        s_static("\r\n")
        s_static("Host: ")
        s_static("www.hhserver.com\r\n")
        s_static("Content-Length: ")
        s_size("post payload", format="ascii", signed=True, fuzzable=False)
        s_static("\r\n\r\n")



        if s_block_start("post payload"):
            input_count = 0
            for _input in form["inputs"][:-1]:
                s_static(_input["name"])
                s_static("=")

                if _input["type"] in datas:
                    data_file = open(datas[_input["type"]], "r")
                    s_file_group("input_" + str(input_count), data_file)
                else:
                    data_file = open(datas["default"], "r")
                    s_file_group("input_" + str(input_count), data_file)
                    #s_string(name="input_" + count, value=_input["value"])

                input_count = input_count + 1
                s_static('&')

            _input = form["inputs"][-1]
            s_static(_input["name"])
            s_static("=")
            if _input["type"] in datas:
                data_file = open(datas[_input["type"]], "r")
                s_file_group("input_" + str(input_count), data_file)
            else:
                data_file = open(datas["default"], "r")
                s_file_group("input_" + str(input_count), data_file)
                #s_string(name="input_" + count, value=_input["value"])

            input_count = input_count + 1

        s_block_end()

        #s_static("\r\n\r\n")

