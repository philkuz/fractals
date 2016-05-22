def new_file(name, extension):
    return "{0}.{1}".format(name, extension)
def new_png(name):
    return new_file(name, "png")

def name(basename):
    def get_name():
        # tries all anme
        counter = 0
        while True:
            try:
                file_name = new_png(basename + str(counter))
                f =  open(file_name)
            except IOError:
                break
        return file_name
    return get_name
