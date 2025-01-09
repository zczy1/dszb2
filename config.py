ip_version_priority = "ipv6"

source_urls = [
"http://175.178.251.183:6689/aktvlive.txt",
    "https://live.fanmingming.cn/tv/m3u/ipv6.m3u",
    "https://raw.githubusercontent.com/yuanzl77/IPTV/main/直播/央视频道.txt",
    "https://live.zhoujie218.top/tv/iptv6.txt",
    "https://live.zhoujie218.top/tv/iptv4.txt",
    "https://www.mytvsuper.xyz/m3u/Live.m3u",
    "http://ww.weidonglong.com/dsj.txt",
    "http://xhztv.top/zbc.txt",
    "https://raw.githubusercontent.com/qingwen07/awesome-iptv/main/tvbox_live_all.txt",
    "https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
    "http://home.jundie.top:81/Cat/tv/live.txt",
    "https://raw.githubusercontent.com/vbskycn/iptv/master/tv/hd.txt",
    "https://cdn.jsdelivr.net/gh/YueChan/live@main/IPTV.m3u",
    "https://raw.githubusercontent.com/cymz6/AutoIPTV-Hotel/main/lives.txt",
    "https://raw.githubusercontent.com/PizazzGY/TVBox_warehouse/main/live.txt",
    "https://fm1077.serv00.net/SmartTV.m3u",
    "https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/suxuang/myIPTV/main/ipv6.m3u",
    "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/Guovin/iptv-api/gd/output/result.m3u",
    "https://lu.wqwqwq.sbs/tv.m3u",
    "https://github.com/SPX372928/MyIPTV/blob/master/%E9%BB%91%E9%BE%99%E6%B1%9FPLTV%E7%A7%BB%E5%8A%A8CDN%E7%89%88.txt",
    "https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u",
    "https://raw.githubusercontent.com/YueChan/Live/refs/heads/main/APTV.m3u",
    "https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u",
    "https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
    "https://raw.githubusercontent.com/joevess/IPTV/main/m3u/iptv.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPV6.m3u",
    "https://github.com/YanG-1989/m3u/blob/main/Gather.m3u",
    "https://iptv.b2og.com/txt/fmml_ipv6.txt",
    "https://live.zbds.top/tv/iptv6.txt",
    "https://live.zbds.top/tv/iptv4.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/joevess/IPTV/main/home.m3u8",
    "https://aktv.top/live.txt",
    "http://175.178.251.183:6689/live.txt",
    "https://m3u.ibert.me/txt/fmml_dv6.txt",
    "https://m3u.ibert.me/txt/o_cn.txt",
    "https://m3u.ibert.me/txt/j_iptv.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/xzw832/cmys/main/S_CCTV.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/xzw832/cmys/main/S_weishi.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/asdjkl6/tv/tv/.m3u/整套直播源/测试/整套直播源/l.txt",
    "https://ghgo.xyz/raw.githubusercontent.com/asdjkl6/tv/tv/.m3u/整套直播源/测试/整套直播源/kk.txt",
    "https://ghproxy.net/https://raw.githubusercontent.com/ssili126/tv/main/itvlist.m3u",
    "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt",
    "https://raw.githubusercontent.com/zczy1/dszb/refs/heads/main/iptv.txt",
    "https://raw.githubusercontent.com/big-mouth-cn/tv/main/iptv-ok.m3u",
    "https://raw.githubusercontent.com/chuzjie/wuihui/refs/heads/main/new.txt",
    "https://raw.githubusercontent.com/zczy1/ipzhibo/refs/heads/master/output/result.txt"
    
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

announcements = [
    {
        "channel": "公告",
        "entries": [
            {"name": "本次", "url": "https://liuliuliu.tv/api/channels/1997/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "直播", "url": "https://liuliuliu.tv/api/channels/233/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "更新日期", "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E4%B8%BB%E8%A7%92.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": None, "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E8%B5%B7%E9%A3%8E%E4%BA%86.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml",
    "https://epg.112114.xyz/pp.xml"
]
