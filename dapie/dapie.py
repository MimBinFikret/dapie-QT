# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton

import docker

class DockerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Konteynır Listesi")
        self.setGeometry(100, 100, 400, 350)

        self.docker_client = docker.from_env()
        self.container_list = QListWidget(self)
        self.container_list.setGeometry(10, 10, 380, 280)

        self.exit_button = QPushButton("Çıkış", self)
        self.exit_button.setGeometry(150, 300, 100, 30)
        self.exit_button.clicked.connect(self.exit_button_clicked)

        self.update_container_list()

    def update_container_list(self):
        self.container_list.clear()

        containers = self.docker_client.containers.list()
        for container in containers:
            self.container_list.addItem(container.name)

    def exit_button_clicked(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockerApp()
    window.show()
    sys.exit(app.exec_())
