__author__ = "kvda-creator"

import string

class mainClass():
    def mainFunc(self):
        offset = 1
        print("---")
        print("Check Palindrome")
        print("---")
        Palengthdrome = input("Masukkan kata : ")
        print("---")
        print(" ")
        if(Palengthdrome == Palengthdrome[::-1]):
            print(Palengthdrome[0].upper()+Palengthdrome[1:])
            print("Kata yang anda masukkan adalah Palindrome.")
        else:
            print("Kata yang anda masukkan bukan Palindrome.")
        print("---")
        print("copyright 2021 kvda-creator")

if __name__ == '__main__':
    mainClass().mainFunc()