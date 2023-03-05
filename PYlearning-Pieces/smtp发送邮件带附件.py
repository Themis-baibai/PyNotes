from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart #发送多文件的包
from email.mime.application import MIMEApplication
import smtplib

# smtp服务器以及相关配置信息
smtp_server = 'smtp.163.com'
from_addr = 'raoaaanqi@163.com'
password = 'ANVQMHZVUYIZXZBI'   # 网易授权码,非邮箱登入密码.
to_addr = '1037103143@qq.com'    # 接收邮箱
title = '使用smtp库发送'
#邮件文本/html内容
content = 'This is a mail text from temisimoyuzhanghao!!!Testing!! '

# 1 创建邮箱(写好邮件内容 发送人 收件人和标题等)
msg = MIMEMultipart() #创建一个带附件的实例
msg['From'] = formataddr(('忒弥斯摸鱼账号', from_addr)) # 发件人昵称和邮箱
msg['To'] = formataddr(('接受者', to_addr))     # 收件人昵称和邮箱,可以写成(to_addr, to_addr)
msg['Subject'] = title #邮件标题

#邮件正文(文本)内容
msg.attach(MIMEText(content, 'plain', 'utf-8'))

# 构造附件1：.txt类型文件
txt_file='C:/Users/10371/Desktop/天官赐福(番外).txt'
att_txt = MIMEText(open(txt_file, 'rb').read(), 'base64', 'utf-8')
att_txt["Content-Type"] = 'application/octet-stream' #任意二进制文件
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att_txt["Content-Disposition"] = 'attachment; filename="天官赐福(番外).txt"'
msg.attach(att_txt) #将txt文件贴入邮件

# 构造附件2：.pdf类型文件 (不能太大！！！！)
pdf_file='C:/Users/10371/Desktop/testing.PDF'
att_pdf=MIMEApplication(open(pdf_file,'rb').read())
att_pdf.add_header('Content-Disposition', 'attachment', filename='testing.PDF') #√
msg.attach(att_pdf) #将pdf文件贴入邮件

# 构造附件3：.zip类型文件
zip_file='C:/Users/10371/Desktop/18343107-饶安琪-形势与政策作业.zip'
att_zip=MIMEApplication(open(zip_file,'rb').read(), _subtype='octet-stream')
att_zip.add_header('Content-Disposition', 'attachment', filename='18343107-饶安琪-形势与政策作业.zip') #√
msg.attach(att_zip) #将.zip文件贴入邮件

# 2 登入账号
# 明文传输端口号是25
#server = smtplib.SMTP(smtp_server, 25)

# TLS加密: 端口号是587，通信过程加密，邮件数据安全，使用正常的smtp端口。
# 对于TLS加密方式需要先建立SSL连接，然后再发送邮件。此处使用starttls()来建立安全连接
#server = smtplib.SMTP(smtp_server, 587)
#server.starttls()

# SSL加密: 端口号是465，通信过程加密，邮件数据安全。
server = smtplib.SMTP_SSL(smtp_server, 465)
server.connect(smtp_server)
server.login(from_addr, password)

# 3 发送邮件
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print("邮件发送成功.")
except Exception as e:
    print('邮件发送失败,错误代码为: %s' % e)
