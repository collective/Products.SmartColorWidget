# -*- coding: utf-8 -*-

from Products.SmartColortWidget import LOG

def uninstall(self, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-Products.SmartColorWidget:uninstall')
        LOG.info("SmartColorWidget removed")