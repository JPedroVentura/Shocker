# CVE-2014-6271

O Shellshock é uma vulnerabilidade crítica devido aos privilégios escalonados concedidos aos invasores, que lhes permitem comprometer os sistemas à vontade.
Embora a vulnerabilidade do ShellShock, CVE-2014-6271, tenha sido descoberta em 2014, sabe-se que ela ainda existe em um grande número de servidores no mundo.
A vulnerabilidade foi atualizada (CVE-2014-7169) logo após e foi modificada até 2018. 

O teste abaixo foi realizado em ambiente controlado e com as devidas permissões :wink:

python3 .\shocker.py -u http://███.█.█.███/ -c "ls" 

![image](https://user-images.githubusercontent.com/86115368/213880194-4715b4b1-bd45-416c-a4ed-172011f4165c.png)
