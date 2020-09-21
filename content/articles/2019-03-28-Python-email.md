Status: published
Date: 2019-03-28 02:56:02
Author: Jerry Su
Slug: Python-email
Title: Python email
Category: 
Tags: Python

[TOC]

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置登录及服务器信息
mail_host = 'smtp.163.com'
mail_user = 'jerrylsu'
mail_pass = input('输入授权码102：')  # 授权码， 非密码
sender = 'jerrylsu@163.com'
receivers = ['sa517301@mail.ustc.edu.cn']

#设置eamil信息
#添加一个MIMEmultipart类，处理正文及附件
message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'title'
#推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
with open('Python-logging.md','r') as f:
    content = f.read()
#设置html格式参数
part1 = MIMEText(content,'html','utf-8')
#将内容附加到邮件主体中
message.attach(part1)

#登录并发送
try:
    # SMTP服务器设置(地址,端口):
    server = smtplib.SMTP_SSL(mail_host, 465) 
    # server.set_debuglevel(1)
    # 连接SMTP服务器(发件人地址, 客户端授权密码)
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    print('Send success!')

except smtplib.SMTPException as e:
    print('Error',e)

finally:
    # 退出SMTP服务器
    server.quit()
```


```python
#=========================================================================
# 加密SMTP
#
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。  
#=========================================================================

    from email import encoders
    from email.header import Header
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr, formatdate
    
    import smtplib
    
    # return Alias_name <xxxx@example.com>
    
    
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    
    # 接收参数: 发件人地址
    from_addr = '你的邮箱地址'
    
    # 接收参数: 客户端授权密码
    passwd = '你的客户端授权密码'
    
    # 接收参数: 收件人地址,可多个
    to_addrs = ['ex@qq.com', 'ex@163.com', 'ex@gmail.com']
    
    # 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
    smtp_server = 'smtp.126.com'
    
    
    # 接收参数: 邮件主题
    subject = '人生苦短'
    
    # 接收参数: 邮件正文
    plain = '我用python!'
    
    # 带附件邮件
    # 指定subtype为alternative，同时支持html和plain格式
    msg = MIMEMultipart('alternative')
    # 邮件正文中显示图片，同时附件的图片将不再显示
    # plain = 'Hello world and hello me!'
    msg.attach(MIMEText(str(plain), 'plain', 'utf-8'))       # 纯文本
    # html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
    # msg.attach(MIMEText(html, 'html', 'utf-8'))         # HTML
    # 添加附件：即关联一个MIMEBase，图片为本地读取
    with open('/home/uxeix/Pictures/icon/favicon (Jianshu).ico', 'rb') as f:
        # 设置附件中的MIME和文件名
        mime = MIMEBase('image', 'jpeg', filename='hot.jpg')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment',
                        filename='hot.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        msg.attach(mime)
    
    # 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
    msg['From'] = _format_addr(from_addr)
    # msg['To'] = _format_addr(to_addrs)
    msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr)
                                 for to_addr in to_addrs])
    msg['Subject'] = Header(str(subject), 'utf-8').encode()
    msg['Date'] = formatdate()
    
    
    #=========================================================================
    # 发送邮件
    #=========================================================================
    try:
        # SMTP服务器设置(地址,端口):
        server = smtplib.SMTP_SSL(smtp_server, 465)
        # server.set_debuglevel(1)
        # 连接SMTP服务器(发件人地址, 客户端授权密码)
        server.login(from_addr, passwd)
    
        # 发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())
    
        print('邮件发送成功')
    
    except smtplib.SMTPException as e:
        print(e)
        print('邮件发送失败')
    
    finally:
        # 退出SMTP服务器
        server.quit()
```
