class Saver():
    output_file = None
    exclusion = []

    def __init__(self, filename, exclude=None):
        if exclude:
            with open(exclude, 'r') as excl_file:
                for line in excl_file.readlines():
                    self.exclusion.append(line.replace('\n',''))
        self.output_file = open(filename, "w")

    def output(self, pswd):
        if pswd not in self.exclusion:
            self.output_file.write(pswd+'\n')

    def __del__(self):
        self.output_file.close()