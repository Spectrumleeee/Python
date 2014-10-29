# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:11:49 2013

@author: Administrator
"""
import time,math,os,re,urllib,urllib2,cookielib 
from BeautifulSoup import BeautifulSoup 
import time     
""" 自动抓取百度图片 """
class BaiduImage:     
    """     
    image_links     图片URL链接     
    image_dir       图片存放文件夹     
    current_page    当前页面地址     
    next_page       下一页面地址     
    image_count     已下载图片数量     
    """
     
    image_links = []     
    image_dir = 'test'    
    current_page = ''     
    next_page = ''     
    image_count = 0
    page_count = 1
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                  'Accept':'text/html;q=0.9,*/*;q=0.8',
                  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                  'Accept-Encoding':'gzip',
                  'Connection':'close',
                  'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
                  }
    req_timeout = 5
    


    def __init__(self):
        self.cj =cookielib.LWPCookieJar()
        try:
            self.cj.revert('baiduimage.cookie')
        except:
            None
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        self.opener.addheaders = [
            ("User-agent", "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.1) Gecko/20090704 Firefox/3.5"),
            ("Accept", "*/*")]
            
    """ 得到当前页面中图片的链接地址 """    
    def get_image_links(self):
        try:
            html = self.opener.open(self.current_page).read()
        except Exception,e:
            self.write_log(e)
            return
    
        soup = BeautifulSoup(html)
        self.image_links = []
#        for link in soup.findAll('a',{'href':re.compile('^./img')}):
        linkList = soup.findAll('a',{'href':re.compile('^./img')})
        if linkList!=None:
            for link in linkList:
                if 'src=http://' in str(link):
                    l = re.findall(r'src=(http://.*)',link['href'])[0]
                    self.image_links.append(l)
                
    """ 得到下一页地址 """     
    def get_next_page(self):
        html = self.opener.open(self.current_page).read()
        soup = BeautifulSoup(html)
        spans = soup.findAll('span')
        for span in spans:
            span_html = str(span)
            if '下一页' in span_html:
                self.current_page = str('http://wap.baidu.com')+str(BeautifulSoup   
                 
(span_html).find('a')['href'])
                self.page_count += 1
                print self.page_count
                self.write_log('Going next page...')
                return
    
        self.write_log('This is the latest page')
        self.next_page = ''
        return False
        
    """ 下载self.image_links中的图片 """    
    def download(self):
        if not self.image_links:
            return False
    
        self.write_log('Current page - %s' %self.current_page)
        for link in self.image_links:
#            try:
#                req = urllib2.Request(link,None,self.req_header)
#                resp = urllib2.urlopen(req,None,self.req_timeout)
#            except Exception,e:
#                self.write_log('Connect error:%s' %e)
#                return
            self.write_log('Downloading... - %s' %link)
            file_name = ""
            fomart = './\\'
            for num in range(7,len(link)-4):
                if link[num] in fomart:
                    file_name += '_'
                else:
                    file_name += link[num]
            file_name += '.jpg'
           # file_name = str(int(time.time()))+'.jpg'
            savename = os.path.join(self.image_dir,file_name)
            print savename
            try:
                req = urllib2.Request(link,None,self.req_header)
                resp = urllib2.urlopen(req,None,self.req_timeout)
                data = resp.read()
                file=open(savename,'w+b')
                file.write(data)
                file.close()
            except IOError:
                print "download error!"+ link
            self.image_count += 1
#            time.sleep(0.1)       
    def write_log(self,text):
#        os.system('cls')
        print text
        textName = self.image_dir+'/log.txt'
        log = open(textName,'a')
        log.write(text)
        log.write('\n')
        log.close()
    
    """ 给出wap起始页开始下载 """    
    def run(self,start_page):
        path = ""
        new_path = os.path.join(path, self.image_dir)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        self.current_page = start_page
        while True:
            # 获取后下载首页图片
            self.get_image_links()
            self.download()
            if self.get_next_page()!=False:
                self.write_log('Image total:%d' %self.image_count)
#                time.sleep(0.1)
            else:
                return

app = BaiduImage() 
app.run(start_page='http://wap.baidu.com/ssid=0/from=0/bd_page_type=1/uid=8DFFADB99DFC96F8BFAAFD08AB27BC3C/pu=sz%40224_220%2Cta%40middle___3_537/img?word=%E8%BD%A6&tn_3=bdwis&tn_9=bdwiw&dw=w240&bs=176_208&pos=0&pinf=0_6_0_%40bdwis_%40%E8%A1%97%E9%81%93_%40176_208_%40w240&st_3=103341&st_9=1033B4&vit_3=tj1&vit_9=tj2&sp=&mid=w240&ct_3=%E6%90%9C%E5%9B%BE%E7%89%87')
#http://wap.baidu.com/img