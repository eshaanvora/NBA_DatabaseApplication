#Eshaan Vora
#EshaanVora@gmail.com

#Module contains miscellaneous helper functions
class helper():
    #Function parses a string and converts to appropriate type
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    @staticmethod
    def data_cleaner(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()
        data = [i.strip().split(",") for i in data]
        data.pop(0)

        data_cleaned = []
        for row in data[:]:
            row = [helper.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned
