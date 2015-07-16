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
        s_group("name", values = form["payload"].keys())
        if s_block_start("post blob", group = "name"):
            s_delim("=")
            s_string("B"*100)
        s_block_end()
        s_static("\r\n\r\n")

        count = count + 1

