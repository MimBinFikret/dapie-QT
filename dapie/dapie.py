# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget

import docker

class DockerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Konteynır Listesi")
        self.setGeometry(100, 100, 400, 300)

        self.docker_client = docker.from_env()
        self.container_list = QListWidget(self)
        self.container_list.setGeometry(10, 10, 380, 280)

        self.update_container_list()

    def update_container_list(self):
        self.container_list.clear()

        containers = self.docker_client.containers.list()
        for container in containers:
            self.container_list.addItem(container.name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DockerApp()
    window.show()
    sys.exit(app.exec_())
