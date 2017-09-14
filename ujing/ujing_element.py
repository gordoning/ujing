# -*- coding: utf-8 -*-
__author__ = 'qianqing'

from PO import base_page
from time import sleep

class Element(base_page.Base):
    # 首页
    def select_home_or_order_or_profile(self, select):
        self.click_by_xpath("//*[@class='tabs tabs-icon-top ujing-footer']/a[%s]" % select)

    def select_scan_or_yuyue_wash(self, select):
        self.click_by_xpath("//*[@class='row responsive-sm scanAremote']/div[%s]" % select)

    # 下单，选择洗衣程序
    def select_wash_program(self, select=1):
        # 选择洗衣程序
        self.click_by_xpath("//*[@class='model-info']/div[%s]" % select)

    def place_order(self):
        self.click_by_xpath("//*[@class='placeOrder']")
        # 点击"确定"
        self.click_by_xpath("//*[@class='no-bg modal slide-in-up ng-enter active ng-enter-active']/div/button")

    # 选择支付
    def pay_alipay(self):
        # 选择"支付宝"
        self.click_by_xpath("//*[@class='item item-radio ng-not-empty ng-valid pay-alipay']")
        # 点击"确认支付"
        self.click_by_xpath("//button[@ng-click='pc.onPay()']", 5)
        self.wd.implicitly_wait(10)
        self.switch_to_nativeApp()
        self.click_by_name('立即付款')
        self.wd.implicitly_wait(10)
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_1')
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_1')
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_8')
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_1')
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_1')
        self.click_by_id('com.alipay.android.phone.safepaybase:id/key_num_8')
        sleep(7)
        self.switch_to_webView()

    def select_program_cancel_or_cleaning_or_start(self, el=3):
        # "启动",没有筒自洁选择2，有筒自洁选择3,取消订单选择1
        self.click_by_xpath("//*[@class='order-status']/div[3]/div[%s]" % el)
        # "确定取消"
        if el == 1:
            self.switch_to_nativeApp()
            self.click_by_name("确定")
        else:
            # "确认启动"
            self.click_by_xpath("//*[@class='modal-backdrop active']/div[2]/ion-modal-view/div/button", 10)

    def end_program(self):
        # "结束订单"
        self.click_by_xpath("//*[@class='btn-end']")
        self.switch_to_nativeApp()
        self.click_by_name('确定', 10)

    # 测试用例
    def yuyue_wash(self):
        self.switch_to_webView()
        self.select_home_or_order_or_profile(1)
        self.select_scan_or_yuyue_wash(2)
        self.select_wash_program(1)
        self.place_order()
        self.pay_alipay()
        self.select_program_cancel_or_cleaning_or_start(3)
        self.end_program()







