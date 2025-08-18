import Rectangle as rect


menu = {
    1: 'Doc du lieu tu file input.db',
    2: 'Them moi hinh chu nhat',
    3: 'Hien thi danh sach hinh chu nhat',
    4: 'Luu danh sach hinh chu nhat xuong file demo4output.db',
    'Others': 'Thoat'
}

def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])



while True:
    print_menu()
    try:
        chon =  int(input('Nhap tuy chon: '))
    except:
        print("Nhap sai dinh dang, hay nhap lai")

    if chon == 1:
        fr = open('input.db', mode = 'r', encoding = 'utf-8')
        listRectangle = []
        for line in fr:
            stripLine = line.strip("\n")
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cd, cr)
            listRectangle.append(hcn)
        fr.close
    elif chon == 2:
        cr = float(input("Nhap chieu rong: "))
        cd = float(input("Nhap chieu dai: "))
        hcn2 = rect.Rectangle(cr, cd)
        listRectangle.append(hcn2)
    elif chon == 3:
        if listRectangle.count == 0:
            print("Danh sach rong")
        else:
            for item in listRectangle:
                item.display()
    elif chon == 4:
        fw = open('outputdemo4.db', mode = 'w', encoding = 'utf-8')
        for item in listRectangle:
            fw.write(f"{item.width}, {item.length}, {item.perimeter()}, {item.area()}\n")
        fw.close
    else:
        print("Ket thuc chuong trinh")
        break
