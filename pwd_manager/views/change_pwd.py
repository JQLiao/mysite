import os
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException, SSHException

class SSHRemoteHost(object):
    def __init__(self, hostname, port, user, passwd, cmd):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.passwd = passwd
        self.cmd = cmd

    def do_cmd(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.hostname,
            port=self.port,
            username=self.user,
            password=self.passwd)
            print("正在连接%s......." % (self.hostname))
            # 执行操作
            stdin, stdout, stderr = client.exec_command(self.cmd)
            # 获取命令执行的结果
            result = stdout.read().decode('utf-8')
            print(result)
        except NoValidConnectionsError as e:
            print("连接失败")
        except AuthenticationException as e:
            print("密码错误")
        finally:
            # 关闭连接
            client.close()


    def do_cmd(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=self.hostname,
            port=self.port,
            username=self.user,
            password=self.passwd)
            print("正在连接%s......." % (self.hostname))
            # 执行操作
            stdin, stdout, stderr = client.exec_command(self.cmd)
            # 获取命令执行的结果
            result = stdout.read().decode('utf-8')
            print(result)
        except NoValidConnectionsError as e:
            print("连接失败")
        except AuthenticationException as e:
            print("密码错误")
        finally:
            # 关闭连接
            client.close()

            # ssh.exec_command('echo "%s"|passwd --stdin root'%newpassword)

if __name__ == '__main__':
    host = '10.50.8.139'
    port = 22
    user = 'root'
    passwd = '***'
    cmd = 'ls'
    # newpassword = '*****'
    # cmd = f'echo "{newpassword}"|passwd --stdin root'

    clientObj = SSHRemoteHost(host, port, user, passwd, cmd)
    clientObj.do_cmd()