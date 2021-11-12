#!/usr/bin/env python3

import os
import sys

from pbxproj import XcodeProject

proj = XcodeProject.load('../Signal.xcodeproj/project.pbxproj')

def mod_pbxproj_info(project, target):
    root_object_pointer = project["rootObject"]
    objects = project["objects"]
    root_object = objects[root_object_pointer]
    target_pointers = root_object["targets"]
    for target_pointer in target_pointers:
        target_object = objects[target_pointer]
        if target_object["name"] == target:
            buildConfiguration_list_pointer = target_object["buildConfigurationList"]
            buildConfiguration_list_object = objects[buildConfiguration_list_pointer]
            buildConfiguration_pointers = buildConfiguration_list_object["buildConfigurations"]
            for buildConfiguration_pointer in buildConfiguration_pointers:
                build_configuration_object = objects[buildConfiguration_pointer]
                build_settings = build_configuration_object["buildSettings"]
                #print(build_settings)
                build_settings["SUPPORTS_MACCATALYST"] = "YES"
                build_settings["DEVELOPMENT_TEAM"] = "736PPT2SQG"
                build_settings["IPHONEOS_DEPLOYMENT_TARGET[sdk=macosx*]"] = "15.0"
                build_settings["CODE_SIGN_STYLE"] = "Automatic"
                build_settings["CODE_SIGN_IDENTITY"] = "Apple Development"
                build_settings["CODE_SIGN_IDENTITY[sdk=macosx*]"] = "Apple Development"
                build_settings["CODE_SIGN_IDENTITY[sdk=iphoneos*]"] = "Apple Development"
                build_settings["PROVISIONING_PROFILE_SPECIFIER"] = ""
                build_settings["PROVISIONING_PROFILE_SPECIFIER[sdk=iphoneos*]"] = ""
                build_settings["PROVISIONING_PROFILE_SPECIFIER[sdk=macosx*]"] = ""



project = XcodeProject.load('../Signal.xcodeproj/project.pbxproj')
targets = (x.name for x in project.objects.get_targets())
for target in targets:
    print('[+] {}'.format(target))
    mod_pbxproj_info(project, target)
project.save()

