# Import Python 3 compatibility functions
from libopensesame.py3compat import *
# Import the required modules.
import os
from StringIO import StringIO
import struct
from libopensesame.item import item
from libopensesame.generic_response import generic_response
from libqtopensesame.items.qtautoplugin import qtautoplugin
from openexp.canvas import canvas
from psychopy import core, visual

__author__ = "Hernandez-Sande Alberto"
__license__ = "GPLv3"

class HMD_plugin(item, generic_response):

	description = u'Setup for HMD devices'

	def reset(self):

		# Set default experimental variables and values
		self.var.HMDtype = u"Oculus DK1 (1280x800px)"
		self.var.duration = u"keypress"
		self.var.isVideo = u"No"
		self.var.stereoscopic = u"No (No 3D depth)"

	def prepare(self):

		# Call parent functions.
		item.prepare(self)
		# Prepare your plug-in here.
		generic_response.prepare(self)
		path = self.experiment.pool[self.var.media_src]
		self.c = canvas(self.experiment, background_color=self.var.background,
			color=self.var.foreground)
		if not os.path.isfile(path):
			raise osexception(
				u"Media file '%s' was not found."
				% (os.path.basename(path), self.name))
		if self.var.HMDtype == u"Oculus DK1 (1280x800px)" and self.var.stereoscopic == u"No (No 3D depth)" and self.var.isVideo == u"No":
                        self.c.image(path, x=-252, y=0.0)
                        self.c.image(path, x=252, y=0.0)
                elif self.var.HMDtype == u"Oculus DK1 (1280x800px)" and self.var.stereoscopic == u"Yes" and self.var.isVideo == u"No":
                        self.c.image(path, x=0, y=0.0)
                elif self.var.HMDtype == u"Oculus DK2 (1920x1080px)" and self.var.stereoscopic == u"No" and self.var.isVideo == u"No":
                        self.c.image(path, x=-378, y=0.0)
                        self.c.image(path, x=378, y=0.0)
                elif self.var.HMDtype == u"Oculus DK2 (1920x1080px)" and self.var.stereoscopic == u"Yes" and self.var.isVideo == u"No":
                        self.c.image(path, x=0, y=0.0)
                elif self.var.HMDtype == u"Oculus Rift 2016 (2160x1200px)" and self.var.stereoscopic == u"No" and self.var.isVideo == u"No":
                        self.c.image(path, x=-415.8, y=0.0)
                        self.c.image(path, x=415.8, y=0.0)
                elif self.var.HMDtype == u"Oculus Rift 2016 (2160x1200px)" and self.var.stereoscopic == u"Yes" and self.var.isVideo == u"No":
                        self.c.image(path, x=0, y=0.0)
                elif self.var.HMDtype == u"HTC Vive (2160x1200px)" and self.var.stereoscopic == u"No" and self.var.isVideo == u"No":
                        self.c.image(path, x=-415.8, y=0.0)
                        self.c.image(path, x=415.8, y=0.0)
                elif self.var.HMDtype == u"HTC Vive (2160x1200px)" and self.var.stereoscopic == u"Yes" and self.var.isVideo == u"No":
                        self.c.image(path, x=0, y=0.0)
	def run(self):

		# Record the timestamp of the plug-in execution.
		self.set_item_onset(self.c.show())
		# Run your plug-in here.
		self.set_sri()
		self.process_response()

	def var_info(self):

		"""
		Gives a list of dictionaries with variable descriptions.

		Returns:
		A list of (name, description) tuples.
		"""

		return item.var_info(self) + generic_response.var_info(self)


class qtHMD_plugin(HMD_plugin, qtautoplugin):

	def __init__(self, name, experiment, script=None):

		# Call parent constructors.
		HMD_plugin.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
