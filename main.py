# -*-coding:utf-8-*-

MAX = 10


class AddressBooks:
    def __init__(self):
        self.personArray = [self.Person(i) for i in range(10)]
        self.size = 0

    class Person:
        def __init__(self, i):
            self.i = i
            self.name = ""
            self.sex = ""
            self.age = 0
            self.phone_number = ""
            self.address = ""


def menu():
    print("**********************")
    print("***** 1.添加联系人 *****")
    print("***** 2.显示联系人 *****")
    print("***** 3.删除联系人 *****")
    print("***** 4.查找联系人 *****")
    print("***** 5.修改联系人 *****")
    print("***** 6.清空联系人 *****")
    print("***** 0.退出通讯录 *****")
    print("**********************")


def add_person(address_book):
    if address_book.size == MAX:
        print("通讯录已满，无法添加！")
        return
    else:
        address_book.personArray[address_book.size].name = input("Input name:")
        address_book.personArray[address_book.size].sex = input("Input sex(1-Male, 2-Female):")
        address_book.personArray[address_book.size].age = input("Input age:")
        address_book.personArray[address_book.size].phone_number = input("Input phone number:")
        address_book.personArray[address_book.size].address = input("Input address:")
        address_book.size += 1
        print("添加成功")


def show_person(address_book):
    if address_book.size == MAX:
        print("通讯录已满，无法添加！")
        return
    else:
        for i in range(address_book.size):
            print("姓名：{}\t性别：{}\t年龄：{}\t电话：{}\t住址：{}\n".format(
                address_book.personArray[address_book.size].name,
                address_book.personArray[address_book.size].sex,
                address_book.personArray[address_book.size].age,
                address_book.personArray[address_book.size].phone_number,
                address_book.personArray[address_book.size].address
            ))


def del_person(address_book):
    if address_book.size == MAX:
        print("通讯录已满，无法添加！")
        return
    else:
        name = input("请输入要删除的联系人:")
        flag = False
        for i in range(address_book.size):
            if address_book.personArray[i].name == name:
                flag = True
                print("Find it!")
                for j in range(i, address_book.size-1):
                    address_book.personArray[j] = address_book.personArray[j+1]
                address_book.size -= 1
        if not flag:
            print("查无此人！")


def find_person(address_book):
    if address_book.size == 0:
        print("通讯录为空！")
        return
    else:
        name = input("请输入要修改的联系人:")
        for i in range(address_book.size):
            if address_book.personArray[i].name == name:
                print("Find it!")
                print("姓名：{}\t性别：{}\t年龄：{}\t电话：{}\t住址：{}\n".format(
                    address_book.personArray[address_book.size].name,
                    address_book.personArray[address_book.size].sex,
                    address_book.personArray[address_book.size].age,
                    address_book.personArray[address_book.size].phone_number,
                    address_book.personArray[address_book.size].address
                ))
            else:
                print("查无此人!")


def modify_person(address_book):
    if address_book.size == 0:
        print("通讯录为空！")
        return
    else:
        name = input("请输入要修改的联系人:")
        flag = False
        for i in range(address_book.size):
            if address_book.personArray[i].name == name:
                flag = True
                print("Find it! Please input the updated info.")
                address_book.personArray[address_book.size].name = input("Input name:")
                address_book.personArray[address_book.size].sex = input("Input sex(1-Male, 2-Female):")
                address_book.personArray[address_book.size].age = input("Input age:")
                address_book.personArray[address_book.size].phone_number = input("Input phone number:")
                address_book.personArray[address_book.size].address = input("Input address:")
                print("修改成功")
        if not flag:
            print("查无此人!")


def clean_person(address_book):
    address_book.size = 0
    print("清空成功")


def main():
    address_book = AddressBooks()

    while True:
        menu()
        select = int(input("请选择:>"))
        if select == 1:
            add_person(address_book)
        elif select == 2:
            show_person(address_book)
        elif select == 3:
            del_person(address_book)
        elif select == 4:
            find_person(address_book)
        elif select == 5:
            modify_person(address_book)
        elif select == 6:
            clean_person(address_book)
        elif select == 0:
            print("欢迎下次使用")
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == '__main__':
    main()
