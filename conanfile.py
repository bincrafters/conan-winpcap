#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
from conans import ConanFile, MSBuild, tools


class WinpcapConan(ConanFile):
    name = "winpcap"
    version = "4.1.3"
    settings = "os", "arch", "compiler", "build_type"
    url = "http://github.com/bincrafters/conan-winpcap"
    author = "Bincrafters <bincrafters@gmail.com>"
    homepage = "https://www.winpcap.org/"
    description = "The WinPcap packet capture library."
    license = "Muliple"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    exports = ["LICENSE.md"]
    exports_sources = [
        "CMakeLists.txt", 
        "Packet.vcproj.patch",
        "wpcap.vcproj.patch",
        "version.rc.patch",
        "pcap-int.h.patch",
    ]
    
    _source_subfolder = "source_subfolder"
    
    _packet_ntx_proj_dir =  "source_subfolder/packetNtx/Dll/Project"
    _packet_ntx_sln =  "source_subfolder/packetNtx/Dll/Project/Packet.sln"
    
    _winpcap_proj_dir =  "source_subfolder/wpcap/PRJ"
    _winpcap_sln =  "source_subfolder/wpcap/PRJ/wpcap.sln"
    
    _packet_ntx_rc_dir = "source_subfolder/packetNtx/Dll"
    _winpcap_rc_dir = "source_subfolder/wpcap/Win32-Extensions"
    _libpcap_dir = "source_subfolder/wpcap/libpcap"

    def source(self):
        tools.get(
            "http://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip", 
            md5="3a47076c5a437c023e76a58b77cfa890",
        )
        os.rename("winpcap", self._source_subfolder)

        tools.patch(self._packet_ntx_proj_dir, "Packet.vcproj.patch")
        tools.patch(self._packet_ntx_rc_dir, "version.rc.patch")
        tools.patch(self._winpcap_rc_dir, "version.rc.patch")
        tools.patch(self._libpcap_dir, "pcap-int.h.patch")

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("WinPcap is only supported for Windows. For other operating systems, look for libpcap.")

            
    def build(self):
        msbuild = MSBuild(self)
        msbuild.build(
            self._packet_ntx_sln,
            platforms={"x86": "Win32"},
        )
        
        msbuild.build(
            self._winpcap_sln,
            build_type=str(self.settings.build_type) + " - No AirPcap",
            platforms={"x86": "Win32"},
        )

    def package(self):
        self.copy(pattern="LICENSE.md", dst="licenses")
        self.copy(pattern="*.h", dst="include", src=self._libpcap_dir)
        self.copy(pattern="*.h", dst="include", src=os.path.join(self._libpcap_dir, "Win32", "Include"))
        
        self.copy(pattern="*wpcap.dll", dst="bin", src=self._winpcap_proj_dir, keep_path=False)
        self.copy(pattern="*wpcap.lib", dst="lib", src=self._winpcap_proj_dir, keep_path=False)
        self.copy(pattern="*Packet.dll", dst="bin", src=self._packet_ntx_proj_dir, keep_path=False)
        self.copy(pattern="*Packet.lib", dst="lib", src=self._packet_ntx_proj_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ws2_32", "wpcap", "Packet"]
