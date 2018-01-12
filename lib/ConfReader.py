#!/usr/bin/python
#coding=UTF-8
#author=zhangjj

import configparser

class ConfReader:
	conffile=""
	def __init__(self,filepath):
		self.conffile=filepath

	def getAllSec(self):
		'Get all sections in config file'
		try:
			return self._readconf().sections()
		except Exception as e:
			return "Read section error",e

	def _readconf(self):
		cf = configparser.ConfigParser()
		cf.read(self.conffile)
		return cf

	def getOpt(self,section):
		'Get options under a known section'
		try:
			return self._readconf().options(section)
		except Exception as e:
			return "Read option error",e
	def getAllOpt(self):
		'Get all options in config file,it is a list'
		allOpt=list()
		try:
			for sec in self.getAllSec():
				for opt in self.getOpt(sec):
					allOpt.append(opt)
			return allOpt
		except Exception as e:
			return "Read all options error",e
	def getItem(self,section):
		'Get Items under a known section'
		try:
			return dict(self._readconf().items(section))
		except Exception as e:
			return "Read Item error",e

	def getKey(self,section,key):
		'Get value by  given section and key'
		try:
			if section in self.getAllSec():
				allkey=self.getItem(section)
			else:
				return "Section is wrong"
			if key in allkey:
				return allkey[key]
			else:
				return "Key is wrong"
		except Exception as e:
			return "Read key error",e
