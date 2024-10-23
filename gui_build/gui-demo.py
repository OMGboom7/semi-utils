import sys
from PyQt6.QtWidgets import QApplication,QWidget

def main():
    # 必须创建一个应用程序对象
    app = QApplication(sys.argv)

    '''
    QWidget小部件是PyQt6中所有用户界面对象的基类。
    我们为QWidget提供了默认构造函数。
    默认构造函数没有父级。没有父级的小部件称为窗口。
    resize 方法改变了小部件的尺寸，现在它 250 像素宽，150 像素高。
    move 方法把小部件移动到屏幕的指定坐标 (300，300)。
    使用 setWindowTitle 给窗口设置标题，标题显示在标题栏。
    show 方法是在屏幕上显示小部件的方法。显示一个部件的步骤是首先在内存里创建，然后在屏幕上显示。
    '''
    w=QWidget()
    w.resize(800,600)
    w.move(300,300)

    w.setWindowTitle('Demo')
    w.show()

    # sys.exit方法确保一个干净的退出。环境将被告知应用程序如何结束。
    sys.exit(app.exec())

if __name__ == '__main__':
    main()