def response_detail(response, echo=True):
    attrs = vars(response)
    details = '\n'.join("%s: %s" % item for item in attrs.items())
    if echo:
        print details
    return details


def write_response_to_file(response, filename, ext=".text"):
    file = open(filename + ext, 'w')
    file.write(response_detail(response, echo=False))
    file.flush()
    file.close()
