from email.header import Header
from email.mime.text import MIMEText
import smtplib
import csv

file ='data.csv'

print(file)
to_addr =  ''

with open(file, "r", encoding="ISO-8859-1") as csv_file:
    # 读取csv文件，返回的是迭代类型
    read = csv.reader((line.replace('\0','') for line in csv_file))
    # read对象，是一个列表的格式
    print(read)
    # read对象的一个迭代器，可以通过next()取出其中的元素
    print(next(read))
    # 也可以通过for循环取出所有元素
    for line in read:
        to_addr =line[1]


from_addr = '304951371@qq.com'
#邮箱的授权码
password = 'utkbnkaaatrhcadf'

print('recevier:' + to_addr)
#邮箱服务器地址
smtp_server = 'smtp.qq.com'

#设置邮件信息
msg = MIMEText('python培训考试作业','plain','utf-8')

msg['From'] =from_addr

msg['To'] = to_addr

msg['Subject'] = Header('读取CSV格式的通讯录，给自己发用邮件.','utf-8').encode()

#发送邮件
server = smtplib.SMTP_SSL(smtp_server,465)

#打印出和SMTP服务器交互的所有信息

server.set_debuglevel(1)

#登录SMTP服务器
server.login(from_addr,password)

#sendmail():发送邮件，
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print('邮件发送成功！')
