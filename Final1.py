#Переделать все шаги позитивных тестов на выполнение по SSH. Проверить работу.
#Пример кода на языке Python, выполняющего шаги позитивных тестов по SSH:

import paramiko


# Функция для выполнения команды по SSH
def run_ssh_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output


# Шаги теста

# Подключение по SSH
hostname = 'example.com'
username = 'your_username'
password = 'your_password'

# Шаг 1. Проверка соединения с сервером
output = run_ssh_command(hostname, username, password, 'echo "Connection Successful"')
print(output)

# Шаг 2. Создание директории
output = run_ssh_command(hostname, username, password, 'mkdir test_directory')
print(output)

# Шаг 3. Переход в созданную директорию
output = run_ssh_command(hostname, username, password, 'cd test_directory')
print(output)

# Шаг 4. Создание файла внутри директории
output = run_ssh_command(hostname, username, password, 'touch test_file.txt')
print(output)

# Шаг 5. Проверка существования файла
output = run_ssh_command(hostname, username, password, 'ls test_file.txt')
print(output)

# Шаг 6. Удаление созданных файлов и директорий
output = run_ssh_command(hostname, username, password, 'rm test_file.txt')
print(output)

output = run_ssh_command(hostname, username, password, 'cd .. && rm -r test_directory')
print(output)

#Результат выполнения каждого шага будет выведен в консоль.
