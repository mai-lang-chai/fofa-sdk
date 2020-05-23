# -*- coding: utf-8 -*-
import fofa,argparse,os

banner = '''
    _/_/_/_/    _/_/    _/_/_/_/    _/_/    
   _/        _/    _/  _/        _/    _/   
  _/_/_/    _/    _/  _/_/_/    _/_/_/_/    
 _/        _/    _/  _/        _/    _/     
_/          _/_/    _/        _/    _/      
     by https://github.com/mai-lang-chai
        '''
print banner

def Request(m,k,p,q):
    email, key = (m,k)
    client = fofa.Client(email, key)
    global Sum
    query_str = q
    Sum = []
    for page in range(int(p)-1):
        data = client.get_data(query_str, fields="host,title" ,page=page)
        Sum.append(data)

def save(Sum,o):
    for l in Sum:
        for i in range(len(l["results"])):
            host = l["results"][i][0]
            title = l["results"][i][1]
            try:
                url = str(host)
                with open(o,'a+') as f:
                    f.write(url+"--"+title+'\n')
            except:
                pass
    print "File save as  " + os.getcwd() + "\\" + o

if __name__ == '__main__':
    parser =argparse.ArgumentParser(description="python fofa-sdk.py -m 123456@gmail.com -k e839b8781c6b60d381562823e1123456 -q /login.rsp -p 3 -o 2018-9995.txt" )
    parser.add_argument('-m', '--mail', default='', help="123456@gmail.com")
    parser.add_argument('-k', '--key', default='', help="e839b878137160d381562823e13c6e02")
    parser.add_argument('-q', '--query', default='', help="/login.rsp")
    parser.add_argument('-p', '--page', default='', help="5")
    parser.add_argument('-o', '--output', default='A.txt', help="CVE-2018-9995.txt")
    args = parser.parse_args()
    m = ''
    k = ''
    q = ''
    p = ''
    o = ''
    if args.mail:
        m = args.mail
    if args.key:
        k = args.key
    if args.query:
        q = args.query
    if args.page:
        p = args.page
    if args.output:
        o = args.output
    Request(m,k,p,q)
    save(Sum,o)