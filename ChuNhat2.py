import Rectangle as rect

menu_options = {
    1: 'Them moi hinh chu nhat',
    2: 'Hinh thi dach sach hinh chu nhat',
    3: 'Tinh tong dien tich hinh chu nhat',
    4: 'Hien thi cac hinh chu nhat co chu vi nho nhat',
    'Others' : 'Thoan chuong trinh'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

dsHCN = []

while True:
    print_menu()
    try:
        userChoice = int(input('Nhap tuy chon: '))
    except:
        print("Nhap dinh dang sai, hay nhap lai....")
        continue

    if userChoice == 1:
        cr = float(input("Nhap chieu rong: "))
        cd = float(input("Nhap chieu dai: "))
        hcn = rect.Rectangle(cr, cd)
        dsHCN.append(hcn)
    elif userChoice == 2:
        for item in dsHCN:
            item.display()
    elif userChoice == 3:
        dienTich = 0
        for item in dsHCN:
            dienTich += item.area()

        print(f"Tong dien tich hcn: {dienTich}")
    elif userChoice == 4:
        if dsHCN.count == 0:
            print("Danh Sach Rong")
        else:
            chuvi = dsHCN[0].perimeter()
            for item in dsHCN:
                if item.perimeter() < chuvi:
                    chuvi = item.perimeter()
            for item in dsHCN:
                if item.perimeter() == chuvi:
                    item.display()
    else:
        print("Thoat chuong trinh Bye")
        break
