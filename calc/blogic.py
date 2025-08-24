from random import randint as rd

def zagadaj(flg=False):

    if flg:
        return rd(1, 9)


def ugadaj(intval=0, zval=0):
    if zval == intval or zval !=0:
        return f'{intval} - это верный ответ'
    else:
        if 1<intval<zval:
            return f"попробуй еще раз но уже в интервале 1 - {intval}"
        elif zval<intval<9:
            return f"попробуй еще раз но уже в интервале {intval} - 9"

   
if __name__ == "__main__":

    print(zagadaj())
    
