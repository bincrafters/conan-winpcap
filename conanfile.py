"""Conan.io recipe for pcap library
"""
import os
from conans import ConanFile, CMake, tools


class winpcapConan(ConanFile):
    """Donwload pcap library, build and create package
    """
    name = "winpcap"
    version = "4.1.3"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    url = "http://github.com/bincrafters/conan-winpcap"
    author = "Uilian Ries <uilianries@gmail.com>"
    description = "The WinPcap packet capture library."
    license = "https://github.com/the-tcpdump-group/libpcap/blob/master/LICENSE"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports = "LICENSE"
    exports_sources = "CMakeLists.txt"

    def source(self):
        tools.get("https://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip")

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("WinPcap is only supported for Windows. You are looking for libpcap/1.8.1@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=os.path.join("winpcap", "winpcap", "libpcap"))
        cmake.build()

    def package(self):
        self.copy("LICENSE", src=".", dst=".")
        self.copy(pattern="*.h", dst="include", src=os.path.join(self.name, "Include"))
        if self.settings.arch == "x86_64":
            self.copy(pattern="*.dll", dst="bin", src=os.path.join(self.name, "Lib", "x64"), keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=os.path.join(self.name, "Lib", "x64"), keep_path=False)
        else:
            self.copy(pattern="wpcap.dll", dst="bin", src=os.path.join(self.name, "Lib"), keep_path=False)
            self.copy(pattern="Packet.dll", dst="bin", src=os.path.join(self.name, "Lib"), keep_path=False)
            self.copy(pattern="wpcap.lib", dst="lib", src=os.path.join(self.name, "Lib"), keep_path=False)
            self.copy(pattern="Packet.lib", dst="lib", src=os.path.join(self.name, "Lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
