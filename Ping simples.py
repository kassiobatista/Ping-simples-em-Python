import os#os intregra os programas e recursos do S.O

print('\033[34m#\033[m'*60)
ip_ou_host = input('Digite o IP ou host a ser verificado: ')
print('\033[34m-\033[m' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host))
print('\033[34m-\033[m' * 60)