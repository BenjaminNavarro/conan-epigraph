from conans import ConanFile, CMake, tools
import os


class EpigraphConan(ConanFile):
    name = "epigraph"
    version = "0.4.2"
    license = "MIT"
    author = "Benjamin Navarro <navarro.benjamin13@gmail.com>"
    url = "https://github.com:BenjaminNavarro/conan-epigraph"
    description = "A modern C++ interface to formulate and solve linear, quadratic and second order cone problems"
    topics = ("numerical-optimization", "socp", "second-order-optimization",
              "quadratic-programming", "eigen-library", "qp", "eigen")
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False],
               "enable_osqp": [True, False],
               "enable_ecos": [True, False]}
    default_options = {"fPIC": True,
                       "enable_osqp": True,
                       "enable_ecos": True}
    generators = "cmake_find_package_multi"
    requires = "eigen/3.3.9"

    def requirements(self):
        if self.options.enable_osqp:
            self.requires("osqp/0.6.0@bnavarro/stable")
        if self.options.enable_ecos:
            self.requires("ecos/2.0.7@bnavarro/stable")

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/EmbersArc/Epigraph.git",
                  branch="v0.4.2", shallow=True)

    def configure(self):
        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        if self.options.enable_osqp:
            cmake.definitions["ENABLE_OSQP"] = True
        if self.options.enable_ecos:
            cmake.definitions["ENABLE_ECOS"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("LICENSE")
        self.copy("*", src="include", dst="include", keep_path=True)
        self.copy("*epigraph.lib", dst="lib", keep_path=False)
        self.copy("*epigraph.dll", dst="bin", keep_path=False)
        self.copy("*epigraph.so", dst="lib", keep_path=False)
        self.copy("*epigraph.dylib", dst="lib", keep_path=False)
        self.copy("*epigraph.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines = []
        if self.options.enable_osqp:
            self.cpp_info.defines.append("ENABLE_OSQP")
        if self.options.enable_ecos:
            self.cpp_info.defines.append("ENABLE_ECOS")
