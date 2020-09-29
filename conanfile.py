import os
from conans import ConanFile, CMake, tools
import shutil

class VTKConan(ConanFile):
    name = "VTK-test"
    version = "9.0.1"
    source_version = "9.0.1"
    description = "Visualization Toolkit by Kitware"
    settings = "os", "compiler", "build_type", "arch"
    src_fldr = "VTK9"
    version_split = source_version.split('.')
    short_version = "%s.%s" % (version_split[0], version_split[1])

    def source(self):
        tools.get("https://www.vtk.org/files/release/{0}/VTK-{1}.tar.gz"
                  .format(self.short_version, self.source_version))
        extracted_dir = "VTK-{0}".format(self.source_version)
        shutil.move(extracted_dir, self.src_fldr)

    def build(self):
        self.output.info("Commence BUILD")
        cmake = CMake(self)
        cmake.configure(source_folder=self.src_fldr)
        cmake.build()