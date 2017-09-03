movies = ["QQ","AA",1992,50,["ABC","CCD",[811123,"OK"]]]


def print_list(name,indent=False,Level=0):
    for each_lis in name:
        if isinstance(name,list):
            print_list(each_lis,indent,Level+1)
        else:
            if indent:
                for each_tab in range(Level):
                    print("\t",end='')
            print(each_lis)