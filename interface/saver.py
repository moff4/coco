class Saver():
    output_file = None
    exclusion = set()
    pswds = set()
    output_set_size = 200

    def __init__(self, filename, exclude=None):
        if exclude:
            with open(exclude, 'r') as excl_file:
                for line in excl_file.readlines():
                    self.exclusion.add(line.replace('\n',''))
        self.output_file = open(filename, "w")

    def output(self, pswd):
        if pswd not in self.exclusion:
            if len(self.pswds) < self.output_set_size:
                self.pswds.add(pswd)
            else:
                self.output_file.write(''.join(pswd+'\n' for pswd in self.pswds))
                self.pswds.clear()

    def __del__(self):
        self.output_file.write(''.join(str(pswd) + '\n' for pswd in self.pswds))
        self.output_file.close()