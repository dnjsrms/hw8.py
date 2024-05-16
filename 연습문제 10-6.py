def buy(dic) :
    item = input('상품명? ')
    if item == '':
        return False
    else:
        num = int(input('수량은? '))
        shopping_bag[item]= num
        print(f'장바구니에 {item}가(이) {num}개가 담겼습니다.\n')
        print()
    
def show(dic):
    print()
    print(f'>>>장바구니 보기: {dic} \n')
    
def find(dic):
    print('[검색]')
    p = input('장바구니에서 확인하고자 하는 상품은? ')
    if p in dic:
        print(f'{p}은(는) {dic.get(p)}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {p}은(는) 없습니다.')

#주 프로그램부        
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
