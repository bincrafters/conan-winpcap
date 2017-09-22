from conans import ConanFile, CMake


class WinpcapTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")

    def test(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.test()
