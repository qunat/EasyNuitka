# This is a sample Python script.
import os
import sys
import threading

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication
import nuitka
import mainui
import subprocess
import shutil


class MainGui(mainui.Ui_MainWindow,	QtWidgets.QMainWindow):
	def __init__(self,parent=None):
		super(MainGui, self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle( "EasyNuitka")
		self.pushButton.clicked.connect(self.choose_main_py)
		self.pushButton_2.clicked.connect(self.set_output_path)
		self.pushButton_7.clicked.connect(self.Multithreading_command)
		self.pushButton_4.clicked.connect(self.nofollow_import_to)
		self.pushButton_12.clicked.connect(self.nofollow_import_to_remove)
		self.pushButton_20.clicked.connect(self.set_icon)
		self.pushButton_19.clicked.connect(self.remove_icon)
		self.chekbox_clicked_init()
		self.command_dict={}
		self.command_str=None
		self.main_name=None
		self.outputpath="./"
		self.nofollow_import_to_document_str=""
		self.iconname=""

	def choose_main_py(self):
		try:
			file = QtWidgets.QFileDialog.getOpenFileName(self,
														 "getOpenFileName", "./",
														 "All Files (*.py);;Text Files (*.py)")
			self.filenpath=file[0]
			self.lineEdit.setText(file[0])
			self.main_name=self.lineEdit.setText(file[0])
			self.filename=self.filenpath.split("/")[-1]
			self.filenpath=self.filenpath.replace(self.filename,"")
			self.dish=self.filenpath[0:2]

		except Exception as e:
			print(e)
	def set_output_path(self):
		try:
			directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
			self.outputpath=directory
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
			#print(self.command_dict)
		elif not self.checkBox.isChecked():
			self.lineEdit_3.setEnabled(True)
			self.lineEdit_4.setEnabled(True)
			self.checkBox_8.setEnabled(True)
			self.command_dict[self.checkBox] = ""
		#--nofollow-imports
		if self.checkBox_8.isChecked():
			self.checkBox.setEnabled(False)
			self.command_dict[self.checkBox_8] = "--nofollow-imports"
			#print(self.command_dict)
		elif not self.checkBox_8.isChecked():
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
			#print(self.command_dict)
		elif not self.checkBox_7.isChecked():
			self.checkBox_3.setEnabled(True)
			self.checkBox_4.setEnabled(True)
			self.checkBox_9.setEnabled(True)
			self.checkBox_17.setEnabled(True)
			self.lineEdit_3.setEnabled(True)
			self.lineEdit_4.setEnabled(True)
			self.lineEdit_5.setEnabled(True)
			self.lineEdit_8.setEnabled(True)
			if self.checkBox.isChecked():
				self.checkBox_8.setEnabled(False)
			if self.checkBox_8.isChecked():
				self.checkBox.setEnabled(False)

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
			self.command_dict[self.checkBox_2] = ""
		else:
			self.checkBox_10.setEnabled(True)
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
			self.checkBox_2.setEnabled(True)
			self.command_dict[self.checkBox_10] = ""
		#--include-plugin-pyqt5
		if self.checkBox_9.isChecked():
			self.command_dict[self.checkBox_9] = "--plugin-enable=pyqt5"
		else:
			self.command_dict[self.checkBox_9] = ""
		#--include-plugin-numpy
		if self.checkBox_17.isChecked():
			self.command_dict[self.checkBox_17] = "--plugin-enable=numpy"
		else:
			self.command_dict[self.checkBox_17] = ""
		#--include-plugin-torch
		if self.checkBox_20.isChecked():
			self.command_dict[self.checkBox_20] = "--plugin-enable=torch"
		else:
			self.command_dict[self.checkBox_20] = ""
		#--include-plugin-matplotlib
		if self.checkBox_11.isChecked():
			self.command_dict[self.checkBox_11] = "--plugin-enable=matplotlib"
		else:
			self.command_dict[self.checkBox_11] = ""
		#--include-plugin-pyqt6
		if self.checkBox_13.isChecked():
			self.command_dict[self.checkBox_13] = "--plugin-enable=pyqt6"
		else:
			self.command_dict[self.checkBox_13] = ""
		#--include-plugin-pyside2
		if self.checkBox_15.isChecked():
			self.command_dict[self.checkBox_15] = "--plugin-enable=pyside2"
		else:
			self.command_dict[self.checkBox_15] = ""
		#--include-plugin-pyside6
		if self.checkBox_12.isChecked():
			self.command_dict[self.checkBox_12] = "--plugin-enable=pyside6"
		else:
			self.command_dict[self.checkBox_12] = ""
		#--include-plugin-no-qt5
		if self.checkBox_18.isChecked():
			self.command_dict[self.checkBox_18] = "--plugin-enable=no-qt5"
		else:
			self.command_dict[self.checkBox_18] = ""
		#--include-plugin-upx
		if self.checkBox_22.isChecked():
			self.command_dict[self.checkBox_22] = "--plugin-enable=upx"
		else:
			self.command_dict[self.checkBox_22] = ""
		#--include-plugin-tensorflow
		if self.checkBox_19.isChecked():
			self.command_dict[self.checkBox_19] = "--plugin-enable=tensorflow"
		else:
			self.command_dict[self.checkBox_19] = ""
		#--include-plugin-pywebview
		if self.checkBox_25.isChecked():
			self.command_dict[self.checkBox_25] = "--plugin-enable=pywebview"
		else:
			self.command_dict[self.checkBox_25] = ""
		#--include-plugin-tk-inter
		if self.checkBox_24.isChecked():
			self.command_dict[self.checkBox_24] = "--plugin-enable=tk-inter"
		else:
			self.command_dict[self.checkBox_24] = ""
		#--include-plugin-trio
		if self.checkBox_23.isChecked():
			self.command_dict[self.checkBox_23] = "--plugin-enable=trio"
		else:
			self.command_dict[self.checkBox_23] = ""
		#--include-plugin-multiprocessing
		if self.checkBox_14.isChecked():
			self.command_dict[self.checkBox_14] = "--plugin-enable=multiprocessing"
		else:
			self.command_dict[self.checkBox_14] = ""
		#--windows-disable-console
		if self.radioButton.isChecked():
			self.command_dict[self.radioButton] = "--windows-disable-console"
		if self.radioButton_2.isChecked():
			self.command_dict[self.radioButton_2] = ""

	def Multithreading_command(self):
		t=threading.Thread(target=self.excute_command,args=())
		t.start()
	def excute_command(self):
		try:
			self.command_str="python -m nuitka "
			for command in self.command_dict.keys():
				if self.command_dict[command]=="":
					continue
				self.command_str+=self.command_dict[command]+" "

			self.command_str+="--output-dir="+self.outputpath+" "
			self.command_str+="--windows-icon-from-ico="+self.iocnname+" "
			self.command_str+=self.filename

			print(self.command_str)
			os.chdir(self.filenpath)
			os.system(self.command_str)

		except Exception as e:
			print(e)

	def chekbox_clicked_init(self):
		self.package_method=[]
		self.checkBox_dict = {self.checkBox: "--follow-imports", self.checkBox_8: "--nofollow-imports",
							  self.checkBox_7: "--module",
							  self.checkBox_3: "--standalone", self.checkBox_4: "--onefile",
							  self.checkBox_2: "--mingw64", self.checkBox_5: "--show-memory",
							  self.checkBox_6: "--show-progress", self.checkBox_10: "-msvc64",
							  self.checkBox_9: "--include-plugin-pyqt5",
							  self.checkBox_17: "--include-plugin-numpy",self.checkBox_20:"--include-plugin-torch",
							  self.checkBox_11:"--include-plugin-matplotlib",self.checkBox_13:"--include-plugin-pyqt6",
							  self.checkBox_15:"--include-plugin-pyside2",self.checkBox_12:"--include-plugin-pyside6",
							  self.checkBox_18:"--include-plugin-no-qt5",self.checkBox_22:"--include-plugin-upx",
							  self.checkBox_19:"--include-plugin-tensorflow",self.checkBox_25:"--include-plugin-pywebview",
							  self.checkBox_24:"--include-plugin-tk-inter",self.checkBox_23:"--include-plugin-trio",
							  self.checkBox_14:"--include-plugin-multiprocessing",self.radioButton:"--windows-disable-console",
							  self.radioButton_2:""}
		for check in self.checkBox_dict.keys():
			try:
				check.clicked.connect(self.get_package_method)
			except:
				pass

	def nofollow_import_to(self):
		try:
			directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
			self.nofollow_import_to_document = directory.split("/")[-1]
			self.nofollow_import_to_document_str+=self.nofollow_import_to_document+","
			self.lineEdit_4.setText(self.nofollow_import_to_document_str)
		except Exception as e:
			print(e)
			pass
	def nofollow_import_to_remove(self):
		try:
			self.lineEdit_4.setText("")
		except Exception as e:
			print(e)
			pass
	def set_icon(self):
		try:
			file = QtWidgets.QFileDialog.getOpenFileName(self,
														 "getOpenFileName", "./",
														 "All Files (*);;Text Files (*)")
			self.iconpath=file[0]
			self.lineEdit_6.setText(self.iconpath)
			src=self.iconpath
			dist=self.filenpath+src.split("/")[-1]
			try:
				shutil.copyfile(src,dist)
			except:
				pass
			finally:
				self.iocnname = src.split("/")[-1]


		except Exception as e:
			print(e)
	def remove_icon(self):
		self.lineEdit_6.setText("")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	win = MainGui()
	win.show()
	sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
