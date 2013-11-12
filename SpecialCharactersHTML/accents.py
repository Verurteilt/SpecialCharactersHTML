#encoding: utf-8
import sublime, sublime_plugin
import os
try:
	import simplejson as json
except ImportError:
	import json



class AccentsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		PACKAGE_DIR =  sublime.packages_path()
		PACKAGE_DIR = os.path.join(PACKAGE_DIR, "SpecialCharactersHTML")
		SETTINGS_DIR = os.path.join(PACKAGE_DIR, "Settings")
		SETTINGS_GENERAL = os.path.join(SETTINGS_DIR, "HTML.sublime-settings")
		SETTINGS_USUARIO = os.path.join(SETTINGS_DIR, "HTMLU.sublime-settings")
		JSON_SETTINGS_GENERAL = json.loads(open(SETTINGS_GENERAL, 'r+').read())
		JSON_SETTINGS_USUARIO = json.loads(open(SETTINGS_USUARIO, 'r+').read())
		caracters = {"á":'&acute;',"é":"&ecute;","í":"&icute;","ó":"&ocute;", "ú":"&ucute;",
		 			"Á":"&Acute;", "É":"&Ecute;","Í":"&Icute;","Ó":"&Ocute;", "Ú":"&Ucute;",
		 			"¿":"&iquest;", '¡':'&iexcl;', 'ñ':'&ntilde;', ">":"&gt;", "<":"&lt;"}
		for clave, valor in JSON_SETTINGS_USUARIO['include'][0].iteritems():
			clave = clave.encode('utf-8')
			valor = valor.encode('utf-8')
			caracters[clave] = valor
		if JSON_SETTINGS_GENERAL.has_key('exclude'):
			exclude = JSON_SETTINGS_GENERAL['exclude']
			for caracter_to_exclude in exclude:
				if caracters.has_key(caracter_to_exclude):
					del caracters[caracter_to_exclude]
		reg = sublime.Region(0, self.view.size())
		text = self.view.substr(reg).encode('utf-8')
		for region in range(reg.begin(), reg.end()):
			letra = self.view.substr(region).encode('utf-8')
			if letra in caracters:
				text = text.replace(letra, caracters[letra])
		self.view.replace(edit, reg, text)
