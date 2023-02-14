# This is a sample Python script.
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication

import mainui


class MainGui(mainui.Ui_MainWindow,	QtWidgets.QMainWindow):
	def __init__(self,parent=None):
		super(MainGui, self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.choose_main_py)
		self.pushButton_2.clicked.connect(self.set_output_path)
		self.chekbox_clicked_init()
		self.command_dict={}
	def choose_main_py(self):
		try:
			file = QtWidgets.QFileDialog.getOpenFileName(self,
														 "getOpenFileName", "./",
														 "All Files (*);;Text Files (*.py)")
			self.filename=file[0]
			self.lineEdit.setText(file[0])
		except Exception as e:
			pass
	def set_output_path(self):
		try:
			directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
			self.outputpath=directory[0]
			self.lineEdit_2.setText(directory)
		except Exception as e:
			pass
	def get_package_method(self):
		#--follow-imports
		if self.checkBox.isChecked():
			self.lineEdit_3.setEnabled(False)
			self.lineEdit_4.setEnabled(False)
			self.checkBox_8.setEnabled(False)
			self.command_dict[self.checkBox]="--follow-imports"
			print(self.command_dict)
		elif not self.checkBox.isChecked():
			self.lineEdit_3.setEnabled(True)
			self.lineEdit_4.setEnabled(True)
			self.checkBox_8.setEnabled(True)
			self.command_dict[self.checkBox] = ""
		#--nofollow-imports
		if self.checkBox_8.isChecked():
			self.checkBox.setEnabled(False)
			self.command_dict[self.checkBox_8] = "--nofollow-imports"
			print(self.command_dict)
		elif not self.checkBox.isChecked():
			self.checkBox.setEnabled(True)
			self.command_dict[self.checkBox_8] = ""
		#--module
		if self.checkBox_7.isChecked():
			self.checkBox.setEnabled(False)
			self.checkBox_8.setEnabled(False)
			self.checkBox_3.setEnabled(False)
			self.checkBox_4.setEnabled(False)
			self.checkBox_9.setEnabled(False)
			self.checkBox_17.setEnabled(False)
			self.lineEdit_3.setEnabled(False)
			self.lineEdit_4.setEnabled(False)
			self.lineEdit_5.setEnabled(False)
			self.lineEdit_8.setEnabled(False)
			self.command_dict[self.checkBox_7] = "--module"
			print(self.command_dict)
		elif not self.checkBox_7.isChecked():
			self.checkBox.setEnabled(True)
			self.checkBox_8.setEnabled(True)
			self.checkBox_3.setEnabled(True)
			self.checkBox_4.setEnabled(True)
			self.checkBox_9.setEnabled(True)
			self.checkBox_17.setEnabled(True)
			self.lineEdit_3.setEnabled(True)
			self.lineEdit_4.setEnabled(True)
			self.lineEdit_5.setEnabled(True)
			self.lineEdit_8.setEnabled(True)
			self.command_dict[self.checkBox_7] = ""
		#--standalone
		if self.checkBox_3.isChecked():
			self.checkBox_4.setEnabled(False)
			self.checkBox_7.setEnabled(False)
			self.command_dict[self.checkBox_3] = "--standalone"
		else:
			self.checkBox_4.setEnabled(True)
			self.checkBox_7.setEnabled(True)
			self.command_dict[self.checkBox_3] = ""
		#--onefile
		if self.checkBox_4.isChecked():
			self.checkBox_3.setEnabled(False)
			self.checkBox_7.setEnabled(False)
			self.command_dict[self.checkBox_4] = "--onefile"
		else:
			self.checkBox_3.setEnabled(True)
			self.checkBox_7.setEnabled(True)
			self.command_dict[self.checkBox_4] = ""
		#--mingw64
		if self.checkBox_2.isChecked():
			self.checkBox_10.setEnabled(False)
			self.command_dict[self.checkBox_2] = "--mingw64"
		else:
			self.checkBox_10.setEnabled(False)
			self.command_dict[self.checkBox_2] = ""
		#--show-memory
		if self.checkBox_5.isChecked():
			self.command_dict[self.checkBox_5] = "--show-memory"
		else:
			self.command_dict[self.checkBox_5] = ""
		#--show-progress
		if self.checkBox_6.isChecked():
			self.command_dict[self.checkBox_6] = "--show-progress"
		else:
			self.command_dict[self.checkBox_6] = ""
		#-msvc64
		if self.checkBox_10.isChecked():
			self.checkBox_2.setEnabled(False)
			self.command_dict[self.checkBox_10] = "-msvc64"
		else:
			self.checkBox_2.setEnabled(False)
			self.command_dict[self.checkBox_10] = ""
		#--include-plugin-pyqt5
		if self.checkBox_9.isChecked():
			self.command_dict[self.checkBox_9] = "--include-plugin-pyqt5"
		else:
			self.command_dict[self.checkBox_9] = ""
		#--include-plugin-numpy
		if self.checkBox_17.isChecked():
			self.command_dict[self.checkBox_17] = "--include-plugin-numpy"
		else:
			self.command_dict[self.checkBox_17] = ""

















	def chekbox_clicked_init(self):
		self.package_method=[]
		self.checkBox_dict = {self.checkBox: "--follow-imports", self.checkBox_8: "--nofollow-imports",
							  self.checkBox_7: "--module",
							  self.checkBox_3: "--standalone", self.checkBox_4: "--onefile",
							  self.checkBox_2: "--mingw64", self.checkBox_5: "--show-memory",
							  self.checkBox_6: "--show-progress", self.checkBox_10: "-msvc64",
							  self.checkBox_9: "--include-plugin-pyqt5",
							  self.checkBox_17: "--include-plugin-numpy"}
		for check in self.checkBox_dict.keys():
			try:
				check.clicked.connect(self.get_package_method)
			except:
				pass







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	win = MainGui()
	win.show()
	sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
