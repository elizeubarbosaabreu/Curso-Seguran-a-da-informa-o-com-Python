import phonenumbers, sys

from phonenumbers import geocoder

class PhoneFind:
    
    def find(self, tel):        
        self.tel = tel
        try:
            num_tel = phonenumbers.parse(tel)
        except:
            print('Telefone INVÁLIDO!!!!!')
            sys.exit()
        
        local = geocoder.description_for_number(num_tel, 'pt')
        if local == '':
            local = 'Localidade Indefinida ou o número digitado está incompleto!!!!'

        return f'O número de telefone <<{tel}>> aparentemente é de <<{local}>>...'
    
if __name__ == "__main__":
    phone = PhoneFind()    
    tel = input('Digite um número de telefone no formato +551112345678: ')
    print(phone.find(tel))
