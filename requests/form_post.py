from sulley import *
########################################################################################################################
# All POST mimetypes that I could think of/find
########################################################################################################################
# List of all blocks defined here (for easy copy/paste)
"""
sess.connect(s_get("HTML FORM POST"))
"""

########################################################################################################################
# Basic fuzz of form post payloads
########################################################################################################################

def form_post_requests(inputs_form):
    count = 0
    for form in inputs_form:
        s_initialize("HTTP VERBS POST" + str(count))
        s_static("POST " + form["action"] + " HTTP/1.1\r\n")
        s_static("Content-Type: ")
        s_string("application/x-www-form-urlencoded")
        s_static("\r\n")
        s_static("Content-Length: ")
        s_size("post blob", format="ascii", signed=True, fuzzable=True)
        s_static("\r\n")
        if s_block_start("post blob"):
            for key in form["payload"].keys()[:-1]:
                s_static(key)
                s_static("=")
                s_string(form["payload"][key])
                s_static("&")

            s_static(form["payload"].keys()[-1])
            s_static("=")
            s_string(form["payload"][form["payload"].keys()[-1]])
        s_block_end()
        s_static("\r\n\r\n")

        count = count + 1
