  
def extract():
    with open('images.txt', 'rt') as im:
        with open('images_rem', 'wt') as ri:
            
            # iline = im.read()
            for iline in im:
                # print(iline[72])
                if iline[0] == '<':
                    # print(iline[39:52])
                    ri.write(iline[39:52])

def req_to_toml():
    with open('requirements.txt', 'rt') as rf:
        with open('requirments_toml.txt', 'wt') as tf:
            for line in rf:
                pack = line.split(' ')
                pack = list(filter(lambda el: el !='' or el != '\n', pack))
                # pack = [el for el in pack if el !='' or el != '\n' ]
                print(pack)

if __name__ == '__main__':
    req_to_toml()