import requests,bs4,sys,subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--p_n")
parser.add_argument("--f")
parser.add_argument("--c_n")
args = parser.parse_args()
print(args)
abcd = args.p_n  
contest_name = args.c_n
exed_file=args.f

#該当ページにアクセスしてhtml取得
print(contest_name)
res = requests.get('https://atcoder.jp/contests/'+contest_name+'/tasks/'+contest_name+'_'+abcd)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")


#問題を取得
example=list()
for i in soup.select('pre'):
    if(i.string!=None):
        example.append(i.string)


#問題があっているか１問ずつ確認
for i in range(0,len(example)//4):
    print(i)
    with open("tmp","a") as f:
        f.write(example[i*2].rstrip('\r\n').replace('\r',''))
    
    subprocess.call("python %s < %s >ans"%(exed_file,"tmp"),shell=True)
    with open("ans","r")as f:
        ans=f.read().rstrip('\r\n')
        print(example[i*2+1].rstrip('\r\n').replace('\r','')==ans)
        print(ans)
        print(example[i*2+1].rstrip('\r\n'))
    subprocess.call("rm ans tmp",shell=True)
    print()
