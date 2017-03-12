#coding=utf-8

# 功能
# 1. 抓取苹果优惠信息
# 2. 推送


import requests
import notify

class Apple(object):
  """docstring for Apple"""
  specialdeals = \
  "http://www.apple.com/cn/"\
  "shop/browse/home/specialdeals/"

  url_mac = specialdeals + "mac"

  url_ipad = specialdeals + "ipad"
  def __init__(self, url):
    self.url = url
    self.content = "Apple"
    

  '''
  input:
  output:
    Returns true if apple has discount.
  '''
  def grapinfo(self):
    # Remeber text should encode in utf-8 because of Chinese.
    info = requests.get(self.url).text.encode("utf-8")
    if "没有可用的产品" in info\
        or "抱歉" in info:
      return False;
    return True

  def notifyme(self):
    notify.notify("苹果优惠", self.content + "优惠，请前往官网查看")

  def run(self):
    gotcha = self.grapinfo()
    if gotcha:
      self.notifyme()
    else:
      print "sorry, not this time."


class Mac(Apple):
  """docstring for Mac"""
  def __init__(self):
    super(Mac, self).__init__(Apple.url_mac);
    self.content = "MAC电脑"


class Ipad(Apple):
  """docstring for Ipad"""
  def __init__(self):
    super(Ipad, self).__init__(Apple.url_ipad);
    self.content = "ipad"


  
def main():
  Mac().run()
  Ipad().run()







if __name__ == '__main__':
  main()



