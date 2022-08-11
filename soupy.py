
import string, random, shutil, requests

urlPrefix="https://pbs.twimg.com/media/"
urlSuffix="?format=jpg&name=orig"

x=0
while x < 10:
    N=15
    randStr=''.join(random.choices(string.ascii_letters + string.digits, k=N))
    url=urlPrefix+randStr+urlSuffix
    print(url)
    try:
        response = requests.get( url, stream=True, timeout=1)

        if response.status_code == 200:
            print(".")

            with open("downloads\\"+randStr+'.jpg', 'wb+') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            x+=1
        del response
    except:
        pass