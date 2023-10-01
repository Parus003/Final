#Переделать все шаги негативных тестов на выполнение по SSH. Проверить работу.

'''

import paramiko

def execute_ssh_command(hostname, username, password, command):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")
        
        if error:
            output = error
        client.close()
        return output
    
    except paramiko.AuthenticationException:
        return "Authentication failed, please verify your credentials"
    
    except paramiko.SSHException as sshex:
        return "SSH connection failed: {}".format(sshex)
    
    except paramiko.ssh_exception.NoValidConnectionsError:
        return "Unable to connect to the SSH server"

# Пример использования функции для выполнения команды ssh
hostname = "192.168.1.100"
username = "your_username"
password = "your_password"
command = "ls"

result = execute_ssh_command(hostname, username, password, command)
print(result)

'''