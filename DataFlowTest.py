    def process(self, something):
        clear_data = []
        with open(self.input_path) as fin:
            for line in fin:
                data = json.loads(line)
                product = data.get('product')
            ss=fin.read()
            data = json.loads(ss)
            product = data.get('product')
