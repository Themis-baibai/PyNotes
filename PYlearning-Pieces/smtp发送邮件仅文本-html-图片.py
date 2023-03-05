from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #发送多文件的包
from email.mime.image import MIMEImage #发送图片的包
from email.utils import formataddr
import smtplib

# smtp服务器以及相关配置信息
smtp_server = 'smtp.163.com'
from_addr = 'raoaaanqi@163.com'
password = 'FGJLJLVYZNOIIXAS'   # 网易授权码,非邮箱登入密码.（到网易邮箱查）
to_addr = '1037103143@qq.com'    # 接收邮箱
title = '使用smtp库发送'
#邮件文本/html内容
text_content = "这是一个测试内容：附奶油美图！！！" #邮件正文纯文本内容
html_content= """ 
<p>Python 邮件发送测试balabala</p>
<p><a href="http://www.w3cschool.cn">这是一个链接</a></p>
<p>图片演示：</p>  
<p><img src="cid:image1",width='500',height='300'/></p>
"""  #html内容(这里是一个超链接)，并且贴上图片(宽高设置500*300，标签image1)

# 1 创建多内容邮箱(写好邮件内容 发送人 收件人和标题等)
msg=MIMEMultipart()
msg['From'] = formataddr(('忒弥斯摸鱼账号', from_addr))   # 发件人昵称和邮箱
msg['To'] = formataddr(('接受者', to_addr))    # 收件人昵称和邮箱,可以写成(to_addr, to_addr)
msg['Subject'] = title

#文本/html对象：
# textPart = MIMEText(text_content, 'plain', 'utf-8') # 其中plain表示纯文本内容
htmlPart= MIMEText(html_content, 'html', 'utf-8') # 发送html邮件
#msg.attach(textPart)
msg.attach(htmlPart)

#图片对象：
imageFile = 'C:/Users/10371/Desktop/HOBBY/cream1.jpg' #图片文件
imagePart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
#imagePart.add_header('Content-Disposition', 'attachment', filename='cream1') #附件图片形式
imagePart.add_header('Content-ID', '<image1>') #html图片
msg.attach(imagePart) #将图片贴入邮件(附件形式)

# 2 登入账号
# 明文传输端口号是25
# server = smtplib.SMTP(smtp_server, 25)

# TLS加密: 端口号是587，通信过程加密，邮件数据安全，使用正常的smtp端口。
# 对于TLS加密方式需要先建立SSL连接，然后再发送邮件。此处使用starttls()来建立安全连接
# server = smtplib.SMTP(smtp_server, 587)
# server.starttls()

# SSL加密: 端口号是465，通信过程加密，邮件数据安全。
server = smtplib.SMTP_SSL(smtp_server, 465)
server.login(from_addr, password)

# 3 发送邮件
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print("邮件发送成功.")
except Exception as e:
    print('邮件发送失败,错误代码为: %s' % e)
