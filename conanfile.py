#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans.errors import ConanInvalidConfiguration
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
    exports = ["LICENSE.md"]
    exports_sources = [
        "CMakeLists.txt",
        "Packet.vcproj.patch",
        "wpcap.vcproj.patch",
        "version.rc.patch",
        "pcap-int.h.patch"
    ]

    _source_subfolder = "source_subfolder"

    _packet_ntx_proj_dir =  "source_subfolder/packetNtx/Dll/Project"
    _packet_ntx_sln =  "source_subfolder/packetNtx/Dll/Project/Packet.sln"

    _winpcap_proj_dir =  "source_subfolder/wpcap/PRJ"
    _winpcap_sln =  "source_subfolder/wpcap/PRJ/wpcap.sln"

    _packet_ntx_rc_dir = "source_subfolder/packetNtx/Dll"
    _winpcap_rc_dir = "source_subfolder/wpcap/Win32-Extensions"
    _libpcap_dir = "source_subfolder/wpcap/libpcap"
    _common_include_dir = "source_subfolder/Common"

    def source(self):
        sha256 = "346a93f6b375ac4c1add5c8c7178498f1feed4172fb33383474a91b48ec6633a"
        tools.get("http://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip", sha256=sha256)
        os.rename("winpcap", self._source_subfolder)

        tools.patch(self._packet_ntx_proj_dir, "Packet.vcproj.patch")
        tools.patch(self._packet_ntx_rc_dir, "version.rc.patch")
        tools.patch(self._winpcap_rc_dir, "version.rc.patch")
        tools.patch(self._libpcap_dir, "pcap-int.h.patch")

    def configure(self):
        if self.settings.os != "Windows":
            raise ConanInvalidConfiguration("WinPcap is only supported for Windows. For other operating systems, look for libpcap.")

    def build(self):
        with tools.vcvars(self.settings, force=True):
            platforms = {"x86": "Win32", "x86_64": "x64"}
            msbuild = MSBuild(self)
            if self.settings.arch == "x86":
                msbuild.build_env.link_flags.append("/MACHINE:x86")
            else:
                msbuild.build_env.link_flags.append("/SAFESEH:NO /MACHINE:x64")
            
            msbuild.build(
                self._packet_ntx_sln,
                platforms=platforms,
                force_vcvars=True
            )

            msbuild.build(
                self._winpcap_sln,
                build_type=str(self.settings.build_type) + " - No AirPcap",
                platforms=platforms,
                force_vcvars=True
            )

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy(pattern="*.h", dst="include", src=self._common_include_dir)
        self.copy(pattern="*.h", dst="include", src=self._libpcap_dir)
        self.copy(pattern="*.h", dst="include", src=self._winpcap_rc_dir)

        self.copy(pattern="*wpcap.lib", dst="lib", src=self._winpcap_proj_dir, keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*Packet.lib", dst="lib", src=self._packet_ntx_proj_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ws2_32", "Iphlpapi", "wpcap", "Packet"]
        self.cpp_info.defines = ["WPCAP", "HAVE_REMOTE"]
        self.cpp_info.includedirs = [
            "include",
            "include/Win32/Include"
        ]
