# -*- coding: utf-8 -*-
__author__ = 'qianqing'

from time import sleep

class Base(object):
    def __init__(self, wd):
        self.wd = wd

    def switch_to_webView(self):
        context = self.wd.contexts
        # print context
        while True:
            if u'WEBVIEW_com.midea.vm.washer' in context:
                self.wd.switch_to.context('WEBVIEW_com.midea.vm.washer')
                sleep(2)
                # print "switch to webview success"
                break

    def switch_to_nativeApp(self):
        context = self.wd.contexts
        while True:
            if u'NATIVE_APP' in context:
                self.wd.switch_to.context('NATIVE_APP')
                sleep(2)
                # print "switch to native_app success"
                break

    def click_by_xpath(self, el, time=1):
        try:
            self.wd.implicitly_wait(20)
            self.wd.find_element_by_xpath(el).click()
            sleep(time)
        except:
            print '%s click fail' % el
            self.switch_to_nativeApp()
            self.wd.quit()

    def click_by_name(self, el, time=1):
        try:
            self.wd.implicitly_wait(20)
            self.wd.find_element_by_name(el).click()
            sleep(time)
        except:
            print '%s click fail' % el
            self.wd.quit()

    def click_by_id(self, el, time=1):
        try:
            self.wd.implicitly_wait(20)
            self.wd.find_element_by_id(el).click()
            sleep(time)
        except:
            print '%s click fail' % el
            self.wd.quit()

