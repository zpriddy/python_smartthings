#! /usr/bin/python
import zp_smartthings

def init():
	global smartThings
	global allDevices

	smartThings = zp_smartthings.SmartThings()
	smartThings.load_settings()
	smartThings.request_endpoints()

	allDevices = smartThings.getAllDevices()

def getAllDeviceType(deviceType):
	global allDevices
	return allDevices[deviceType]

def getDevice(deviceType, deviceId):
	global allDevices
	return allDevices[deviceType][deviceId]

def getDeviceStatus(deviceType, deviceId, deviceStatus):
	global allDevices
	device = getDevice(deviceType,deviceId)
	return device[deviceStatus]


def updateAll():
	global allDevices
	global smartThings

	allDevices = smartThings.getAllDevices()

def updateSwitch():
	global allDevices
	global smartThings

	allDevices['switch'] = smartThings.updateSwitch()

def toggleSwitch(deviceId):
	global smartThings
	global allDevices
	newState = smartThings.command_switch(deviceId, 't')
	allDevices['switch'][deviceId]['state'] = newState
	allDevices['switch'] = smartThings.updateSwitch()


def getMode():
	global allDevices
	return allDevices['mode']['Mode']['mode']

def updateMode():
	global allDevices
	global smartThings

	allDevices['mode'] = smartThings.updateMode()

def setMode(mode):
	global allDevices
	global smartThings

	smartThings.command_mode(mode)


def updateDimmer():
	global allDevices
	global smartThings

	allDevices['dimmer'] = smartThings.updateDimmer()

def setDimmer(deviceId,level):
	global allDevices
	global smartThings

	smartThings.command_dimmer(deviceId,level)
	allDevices['dimmer'][deviceId]['level'] = level
	allDevices['dimmer'] = smartThings.updateDimmer()

def getWeather():
	global smartThings

	return smartThings.get_weather()

def updateWeather():
	global allDevices
	global smartThings

	allDevices['weather'] = smartThings.updateWeather()

def updateTemp():
	global allDevices
	global smartThings

	allDevices['temperature'] = smartThings.updateTemp()

