import json

import requests
from time import sleep
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
login={
        'username':"ysyyhhh",
        'password':"4564d0582f2971f5869063062ac7cbbd"
}
#100001
simply = ["1000","1001","1004","1005","1008","1012","1013","1014","1017","1019","1021","1028","1029","1032","1037","1040","1048","1056","1058","1061","1070","1076","1089","1090","1091","1092","1093","1094","1095","1096","1097","1098","1106","1108","1157","1163","1164","1170","1194","1196","1197","1201","1202","1205","1219","1234","1235","1236","1248","1266","1279","1282","1283","1302","1303","1323","1326","1330","1334","1335","1339","1390","1391","1393","1395","1397","1405","1406","1407","1408","1412","1418","1420","1465","1491","1555","1562","1563","1570","1587","1673","1678","1708","1718","1720","1785","1799","1859","1862","1877","1898","1976","1977","1985","1994","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2039","2040","2042","2043","2048","2049","2051","2053","2055","2056","2057","2060","2061","2071","2073","2075","2076","2078","2081","2083","2088","2090","2092","2093","2095","2096","2097","2098","2099","2101","2103","2106","2107","2109","2113","2114","2115","2123","2131","2132","2133","2135","2136","2137","2138","2139","2143","2148","2153","2156","2161","2162","2164","2178","2186","2192","2200","2201","2212","2304","2309","2317","2401","2500","2502","2503","2504","2519","2520","2521","2523","2524","2535","2537","2539","2547","2548","2549","2550","2551","2552","2555","2560","2561","2562","2566","2567","2568","2700","2710"]
#110001
dp = ["1003","10240","1029","1069","1074","1087","1114","1159","1160","1171","1176","1203","1231","1257","1260","1284","1421","1789","1978","2059","2084","2159","2191","2544","2571","2602","2709"]

#120001
search = ["1010","1015","1016","1026","1072","1075","1175","1180","1181","1238","1239","1240","1241","1242","1253","1254","1312","1372","1548","1597","1671","1677","1728","1800","1983","2102","2141","2553","2563","2605","2612","2614","1616","2717"]

#130001 贪心
greedy=["1009","1045","1049","1050","1051","1052","1257","1800","2037","2111","2124","2187","2391","2570"]

#140001 数学
math1 = ["1018","1065","1071","1115","1141","1162","1212","1220","1492","1593","1701","1722","1798","1840","1999","2036","2080","2086","2089","2105","2108","2134","2303","2393","2438","2529","2547","2548","2552","2554","2601","2603","2701"]

#150001 递推
ditui = ["1133","1143","1207","1249","1267","1284","1290","1297","1396","1992","1995","1996","2013","2014","2044","2045","2046","2047","2050","2064","2065","2067","2068","2070","2077","2085","2151","2154","2160","2190","2501","2512","2563","2569","2709","2716"]

#160001 string
str1 = ["1020","1039","1043","1062","1073","1075","1088","1113","1161","1200","1251","1256","1288","1321","1328","1379","1804","1860","1982","1984","2017","2024","2025","2026","2027","2043","2052","2054","2072","2074","2087","2131","2137","2140","2163","2203","2206","2352","2500","2549","2564","2565","2567","2572","2609","2607","2707","2708","2719","2721","2723"]

#170001 bignum
bignum = ["1002","1042","1133","1250","1297","1715","1753","1865","2100"]

#180001 zha
zha = ["1022","1027","1030","1035","1128","1165","1209","1210","1215","1222","1228","1229","1230","1237","1259","1276","1286","1337","1342","1361","1370","1506","1577","1597","1702","1716","1727","1868","1870","1896","1981","1986","1987","1988","1997","1998","1999","2058","2062","2089","2090","2094","2104","2116","2117","2135","2175","2183","2184","2197","2303","2368","2370","2374","2511","2522","2527","2600","2615","2703","2711","2714","2715","2725"]

#190001 博弈
by = ["1077","1404","1517","1524","1525","1527","1536","1564","1729","1730","1846","1847","1848","1849","1850","2147","2149","2176","2177","2188"]

#200001 母函数
mfuction = ["1085","1171","1398","2079","2082","2110","2152","2189","2566"]

#210001 哈希
hash1 = ["1264","1280","1425","1496","1800","2522","2600"]
mafengwoSession = requests.session()
backendurl = "http://10.11.50.231:8080/api/login/"
responseRes = mafengwoSession.post(backendurl,data=login)
print(responseRes)
print(responseRes.text)


def getpro(problemid,ppid):

    def substr(start_str, end, html):
        start = html.find(start_str)
        if start >= 0:
            start += len(start_str)
            end = html.find(end, start)
            if end >= 0:
                aaa = html[start:end].strip()
                if aaa == "" or aaa is None:
                    aaa = "No data."
                return aaa
        raise "Error"

    userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    header = {
        'User-Agent': userAgent,
    }


    Url = "http://acm.hdu.edu.cn/showproblem.php?pid="+problemid

    responseRes = requests.get(Url, headers=header)

    resstr = f"text = {responseRes.text}"

    try:
        titstr = substr("='color:#1A5CC8'>","</h1><font><b>",resstr)
    except:
        print(ppid+" error")
        return 1

    try:
        timestr = substr("Time Limit","(Java",resstr)
        timestr = substr("/"," MS",timestr)
    except:
        print(ppid+" error")
        return 1

    try:
        memstr = substr("Memory L","(Java",resstr)
        memstr = substr("/"," K",memstr)
        memstr = str(int(int(memstr)/1024))
    except:
        print(ppid+" error")
        return 1

    try:
        desstr = substr("Description</div> <div class=panel_content>","</div><div class=panel_bottom>",resstr)
    except:
        desstr = "No data."

    try:  
        instr = substr("Input</div> <div class=panel_content>","</div><div class=panel_bottom>",resstr)
    except:
        instr = "No data."
        
    try:
        outstr = substr("Output</div> <div class=panel_content>","</div><div class=panel_bottom>",resstr)
    except:
        outstr = "No data."
    try:
        sinstr = substr("ier,monospace;\">","</div></pre></div><div",resstr)
    except:
        sinstr = "No data."

    try:
        soutstr = substr("Sample Output</div>","</pre></div><div",resstr)
        soutstr = substr("monospace;\">","</div>",soutstr)
    except:
        soutstr = "No data."

    prodata = {
        'problem':ppid,
        'oj':"HDU",
        'title':'HDU - '+str(problemid)+' '+titstr,
        'des':desstr,
        'input':instr,
        'output':outstr,
        'sinput':sinstr,
        'soutput':soutstr,
        'source':str(problemid),
        'time':timestr,
        'memory':memstr,
    }
    prodatas = {
        'problem':ppid,
        'oj':"HDU",
        'title':'HDU - '+str(problemid)+' '+titstr,
        'tag':'哈希',
        'level':1,
    }
    # print("???")
    print(prodata)
    
    backendurl = "http://10.11.50.231:8080/api/problem/"
    responseRes = mafengwoSession.post(backendurl,data=prodata)
    if int(responseRes.status_code/100) != 2:
        print(responseRes.text)
        # return 1
        exit(0)

    print(prodatas)
    backendurl = "http://10.11.50.231:8080/api/problemdata/"
    responseRes = mafengwoSession.post(backendurl,data=prodatas)
    if int(responseRes.status_code/100) != 2:
        print(responseRes.text)
        # return 1
        exit(0)
    print('HDU - '+str(problemid)+' '+titstr)
    return 0


totid = 210001
for i in range(0,len(hash1) ):
    if(getpro(hash1[i], str(totid)) == 0):
        totid += 1

#运行前一定要改标签！！！！！
# totid = 0
# for i in range(4):
#     totid += getpro(str(i+6727),str(i+5763-totid))

# getpro(str(1083),str(189))
