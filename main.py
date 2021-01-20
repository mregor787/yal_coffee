import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        cur = sqlite3.connect('coffee.sqlite').cursor()
        data = cur.execute('SELECT * FROM kind').fetchall()
        table = self.tableWidget
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
                table.resizeColumnsToContents()


def main():
    app = QApplication(sys.argv)
    e = Espresso()
    e.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
