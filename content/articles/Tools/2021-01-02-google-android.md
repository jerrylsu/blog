Status: published
Date: 2021-01-02 11:23:36 
Author: Jerry Su
Slug: Google-Android
Title: Google-android
Category: 
Tags: Google

[TOC]


## ADB

```
adb version

adb devices

查看所有应用列表：adb shell pm list packages
查看系统应用列表：adb shell pm list packages -s


# com.google.android.gms，com.google.android.gsf，com.google.android.partnersetup，
# com.google.android.backuptransport，com.google.android.onetimeinitializer
删除应用：adb shell pm uninstall --user 0 com.baidu.input_huawei

```

## Go谷歌安装器

注意Go谷歌安装器4.8.4只支持安卓7.0、7.1、8.0、9.0，尝试过安卓8.1总是失败！


## GMS安装器

## 不建议采用以上一键安装

优点方便，缺点默认装的谷歌三件套：谷歌框架，谷歌play服务，谷歌play商城存在与手机安卓系统不匹配，建议单独下载安装。

[https://www.apkmirror.com/](https://www.apkmirror.com/)

[apkpure.com](apkpure.com)

[https://www.olocat.cn/?p=45](https://www.olocat.cn/?p=45)

## 疑难问题

[google play登陆核验信息黑屏退出](https://www.zhihu.com/question/63714089)


```
@ 所有google内建包

@ adb shell pm list packages

@ adb shell pm list packages -s

adb shell pm uninstall --user 0 com.google.android.gms

adb shell pm uninstall --user 0 com.google.android.gsf

adb shell pm uninstall --user 0 com.google.android.backuptransport

adb shell pm uninstall --user 0 com.google.android.onetimeinitializer

adb shell pm uninstall --user 0 com.android.vending      @ google play

adb shell pm uninstall --user 0 com.google.android.gms.policy_sidecar_aps

adb shell pm uninstall --user 0 com.google.android.printservice.recommendation

adb shell pm uninstall --user 0 com.google.android.overlay.contactproviderconfig

adb shell pm uninstall --user 0 com.google.android.partnersetup

adb shell pm uninstall --user 0 com.google.android.webview

adb shell pm uninstall --user 0 com.google.android.overlay.settingsConfig

adb shell pm uninstall --user 0 com.google.android.syncadapters.contacts

adb shell pm uninstall --user 0 com.google.android.ext.services

adb shell pm uninstall --user 0 com.google.android.overlay.gmsconfig

adb shell pm uninstall --user 0 com.google.android.configupdater

adb shell pm uninstall --user 0 com.google.android.marvin.talkback

adb shell pm uninstall --user 0 com.google.android.ext.shared

adb shell pm uninstall --user 0 com.google.ar.core

adb shell pm uninstall --user 0 com.google.android.gsf.login

adb shell pm uninstall --user 0 com.google.android.overlay.settingsProvider

adb shell pm list packages

pause
```